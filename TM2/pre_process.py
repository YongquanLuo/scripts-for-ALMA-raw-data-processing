import glob
import os
import ast

config_file = "tclean_params.txt"
print("The config file is:", config_file)

params = {}
with open(config_file, 'r') as f:
    for line in f:
		
		line = line.strip()
		
		if not line or line.startswith("#"):
			continue
			
		if '=' in line:
			key, val = line.split('=', 1)
			key = key.strip()
			val = val.strip()
			try:
				params[key] = ast.literal_eval(val)  
			except Exception:
				params[key] = val.strip("'\"") 

array = params['array']
field = params['field']
print("The array configuration is:", array)
print("The splitting field is:", field)



spw = ""
spwname = ""

#### for observation of band6, may be changed for other band
if array == "ACA":
    spw = "16,18,20,22"
    spwname = "spw16_18_20_22"

if array == "TM1" or array == "TM2":
    spw = "25,27,29,31"
    spwname = "spw25_27_29_31"
####


filenames = sorted(glob.glob("../*.ms.split.cal"))

print("Start splitting", filenames)
##########   split the field
for i in range(len(filenames)):
    split(
        filenames[i],
        outputvis = os.path.basename(filenames[i]) + "." + field + "." + array + "." + spwname,
        spw = spw,
        datacolumn = 'data',
        field = field
    )

########  transform the frame to LSRK
filenames_split = sorted(
    glob.glob("./*." + field + "." + array + "." + spwname)
)

for i in range(len(filenames_split)):
    listobs(vis = filenames_split[i], listfile = filenames_split[i] + ".listobs.txt", overwrite = False)

for i in range(len(filenames_split)):
    mstransform(
        vis = filenames_split[i],
        outputvis = os.path.basename(filenames_split[i]) + ".LSRK",
        regridms=True,
        outframe='LSRK',
        datacolumn = 'data'
    )

filenames_LSRK = sorted(
    glob.glob("./*." + field + "." + array + "." + spwname + ".LSRK")
)

for i in range(len(filenames_LSRK)):
    listobs(vis = filenames_LSRK[i], listfile = filenames_LSRK[i] + ".listobs.txt", overwrite = False)


########  combine data
import shutil

concatvis = field + '.ms' + '.' + array + '.' + spwname
print("LSRK measurement sets:", filenames_LSRK)

if len(filenames_LSRK) == 0:
    raise RuntimeError(
        "No LSRK measurement sets were found. "
        "Please check the field, array, and SPW settings."
    )
elif len(filenames_LSRK) == 1:
    print("Only one measurement set was found; concat will be skipped.")

    inputvis = filenames_LSRK[0]

    #
    if os.path.abspath(inputvis) != os.path.abspath(concatvis):

        if os.path.exists(concatvis):
            raise RuntimeError(
                "Output measurement set already exists: {}".format(concatvis)
            )

        shutil.move(inputvis, concatvis)
else:
    print("Combining {} measurement sets.".format(len(filenames_LSRK)))

    if os.path.exists(concatvis):
        raise RuntimeError(
            "Output measurement set already exists: {}".format(concatvis)
        )

    concat(
        vis=filenames_LSRK,
        concatvis=concatvis,
        freqtol="1MHz"
    )

listobs(
    vis = concatvis,
    listfile = concatvis + ".listobs.txt",
    overwrite = True
)
