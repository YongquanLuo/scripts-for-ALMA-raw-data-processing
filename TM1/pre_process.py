import glob
import os
import ast


print("The config file is:", 'tclean_params.txt')
params = {}
with open('tclean_params.txt', 'r') as f:
    for line in f:
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

filenames = glob.glob("../*.ms.split.cal")
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
filenames_split = glob.glob("./*" + "." + field + "." + array + "." + spwname)

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

filenames_LSRK = glob.glob("./*" + "." + field + "." + array + "." + spwname + ".LSRK")
for i in range(len(filenames_LSRK)):
    listobs(vis = filenames_LSRK[i], listfile = filenames_LSRK[i] + ".listobs.txt", overwrite = False)


########  combine data

concatvis = field + '.ms' + '.' + array + '.' + spwname

concat(vis = filenames_LSRK,
       concatvis = field + '.ms' + '.' + array + '.' + spwname,
       freqtol = '1MHz'
       )

listobs(vis = concatvis, listfile = concatvis + ".listobs.txt", overwrite = False)
