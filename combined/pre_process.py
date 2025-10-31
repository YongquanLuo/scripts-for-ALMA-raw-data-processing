import ast
import glob

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

concat_contsub = params['concat_contsub']

aca_contsub = glob.glob('./*ACA*.contsub')
tm1_contsub = glob.glob('./*TM1*.contsub')
tm2_contsub = glob.glob('./*TM2*.contsub')

assert len(aca_contsub) == 1 and len(tm1_contsub) == 1 and len(tm2_contsub) == 1, "Some required files are missing or not uniquely matched"

visnames_contsub = [aca_contsub[0], tm1_contsub[0], tm2_contsub[0]]
visnames_contsub_LSRK = [item + '.LSRK' for item in visnames_contsub]

for i in range(len(visnames_contsub)):
    mstransform(vis = visnames_contsub[i], outputvis = visnames_contsub_LSRK[i], regridms=True, outframe='LSRK', datacolumn = 'data')
    listobs(visnames_contsub_LSRK[i], listfile = visnames_contsub_LSRK[i] + '.listobs.txt')

concat(vis = visnames_contsub_LSRK, concatvis = concat_contsub)
print("The concat uvcontsub file is:", concat_contsub)

listobs(concat_contsub, listfile = concat_contsub + '.listobs.txt')