import numpy as np
import ast
import glob
import re
import os

print("The tclean params for continuum are at tclean_params.txt")
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

#### for observation of band6, may be changed for other band
aca = glob.glob("*.ACA.spw16_18_20_22")
tm1 = glob.glob("*.TM1.spw25_27_29_31")
tm2 = glob.glob("*.TM2.spw25_27_29_31")
####

assert len(aca) == 1 and len(tm1) == 1 and len(tm2) == 1, "Some required files are missing or not uniquely matched"

visnames = [aca[0], tm1[0], tm2[0]]
params['visnames'] = visnames

field = params['field']
width = params['width']
nchan = params['nchan']
threshold = params['threshold_mfs']
imsize = params['imsize']
cell = params['cell']
print("The tclean params for continuum are:", params)


def natural_key(filename):
    basename = os.path.basename(filename)
    numbers = re.findall(r'\d+', basename)
    return [int(num) for num in numbers]
filenames = sorted(glob.glob("./cont_freq/fitspec*.txt"), key=natural_key)
print("The continuum data are at", filenames)

def get_cont_freq(filenames):
    tmp = []
    for i in range(len(filenames)):
        tmp.append(np.genfromtxt(filenames[i], skip_header=1))
    return tmp

fitspec0_freq, fitspec1_freq, fitspec2_freq, fitspec3_freq = get_cont_freq(filenames)

for i in range(len(visnames)):
    ms.open(visnames[i])
    freq0 = ms.cvelfreqs(spwids=0, mode='channel', width=0, outframe='LSRK')/1E9
    freq1 = ms.cvelfreqs(spwids=1, mode='channel', width=0, outframe='LSRK')/1E9
    freq2 = ms.cvelfreqs(spwids=2, mode='channel', width=0, outframe='LSRK')/1E9
    freq3 = ms.cvelfreqs(spwids=3, mode='channel', width=0, outframe='LSRK')/1E9
    ms.close()
    
    fitspecs = ['0:', '1:', '2:', '3:']
    freq_lists = [fitspec0_freq, fitspec1_freq, fitspec2_freq, fitspec3_freq]
    freq_refs = [freq0, freq1, freq2, freq3]
    
    for idx, (freq_list, freq_ref) in enumerate(zip(freq_lists, freq_refs)):
        tmp = []
        for freql, freqr in freq_list:
            chan = [np.argmin(np.abs(freql - freq_ref)), np.argmin(np.abs(freqr - freq_ref))]
            chan = sorted(chan)
            tmp.append(f"{chan[0]}~{chan[1]}")
        fitspecs[idx] += ';'.join(tmp)
    fitspec0, fitspec1, fitspec2, fitspec3 = fitspecs
    
    if 'ACA' in visnames[i]:
        fitspec_ACA = fitspec0 + ',' + fitspec1 + ',' + fitspec2 + ',' + fitspec3
    if 'TM1' in visnames[i]:
        fitspec_TM1 = fitspec0 + ',' + fitspec1 + ',' + fitspec2 + ',' + fitspec3
    if 'TM2' in visnames[i]:
        fitspec_TM2 = fitspec0 + ',' + fitspec1 + ',' + fitspec2 + ',' + fitspec3



print("The fitting spws for ACA are:", fitspec_ACA)
print("The fitting spws for TM1 are:", fitspec_TM1)
print("The fitting spws for TM2 are:", fitspec_TM2)


tclean(vis = visnames
       ,field = field
       ,imagename = './continuum/' + field + '.ms' + '.concat.cont.mfs'
       ,restart = True
       ,specmode = 'mfs'
       ,deconvolver = 'mtmfs'
       ,nterms = 2
       ,scales = [0, 5, 15, 45]
       ,imsize = imsize
       ,cell = cell
       ,gridder = 'mosaic'
       ,mosweight = True
       ,usepointing = False
       ,weighting = 'briggs'
       ,robust = 0.5
       ,niter = 10000
       ,threshold = threshold
       ,interactive = False
       ,pbcor = True
       ,pblimit = 0.2
       ,nmajor = 5
       ,datacolumn = 'corrected'
       ,spw = [fitspec_ACA, fitspec_TM1, fitspec_TM2]
)
