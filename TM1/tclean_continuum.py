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


visname = params['visname']
field = params['field']
width = params['width']
nchan = params['nchan']
threshold = params['threshold']
imsize = params['imsize']
cell = params['cell']
print("The tclean params for continuum are:", params)



ms.open(visname)
freq0 = ms.cvelfreqs(spwids=0, mode='channel', width=0, outframe='LSRK')/1E9
freq1 = ms.cvelfreqs(spwids=1, mode='channel', width=0, outframe='LSRK')/1E9
freq2 = ms.cvelfreqs(spwids=2, mode='channel', width=0, outframe='LSRK')/1E9
freq3 = ms.cvelfreqs(spwids=3, mode='channel', width=0, outframe='LSRK')/1E9
ms.close()

fitspec0 = '0:'
fitspec1 = '1:'
fitspec2 = '2:'
fitspec3 = '3:'

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



tmp = []
for i in fitspec0_freq:
    freql = i[0]
    freqr = i[1]
    chan = [np.argmin(np.abs(freql - freq0)), np.argmin(np.abs(freqr - freq0))]
    chan = sorted(chan)
    tmp.append("%i~%i"%(chan[0], chan[1]))
fitspec0 = fitspec0 + ';'.join(tmp)


tmp = []
for i in fitspec1_freq:
    freql = i[0]
    freqr = i[1]
    chan = [np.argmin(np.abs(freql - freq1)), np.argmin(np.abs(freqr - freq1))]
    chan = sorted(chan)
    tmp.append("%i~%i"%(chan[0], chan[1]))
fitspec1 = fitspec1 + ';'.join(tmp)


tmp = []
for i in fitspec2_freq:
    freql = i[0]
    freqr = i[1]
    chan = [np.argmin(np.abs(freql - freq2)), np.argmin(np.abs(freqr - freq2))]
    chan = sorted(chan)
    tmp.append("%i~%i"%(chan[0], chan[1]))
fitspec2 = fitspec2 + ';'.join(tmp)


tmp = []
for i in fitspec3_freq:
    freql = i[0]
    freqr = i[1]
    chan = [np.argmin(np.abs(freql - freq3)), np.argmin(np.abs(freqr - freq3))]
    chan = sorted(chan)
    tmp.append("%i~%i"%(chan[0], chan[1]))
fitspec3 = fitspec3 + ';'.join(tmp)


fitspec = fitspec0 + ',' + fitspec1 + ',' + fitspec2 + ',' + fitspec3

print("The fitting spws are:", fitspec)

tclean(vis = visname
       ,field = field
       ,imagename = './continuum/' + visname + '.cont.mfs'
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
       ,spw = fitspec
       
)
