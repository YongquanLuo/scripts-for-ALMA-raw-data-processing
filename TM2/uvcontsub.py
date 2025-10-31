import numpy as np
import glob
import ast
import re
import os

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
visname_contsub = params['visname_contsub']
print("The file used for uvcontsub is:", visname)

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


# fitspec0_freq = [(217.007088, 217.135018),
#                  (217.182869, 217.274666),
#                  (217.377205, 217.499764),
#                  (217.550057, 217.855232),
#                  (217.901131, 217.979744),
#                  (218.018318, 218.256599),
#                  (218.287849, 218.362556),
#                  (218.388924, 218.479255),
#                  (218.504158, 218.517341),
#                  (218.547127, 218.799080),
#                  (218.821052, 218.846443)
#                 ]
# fitspec1_freq = [(219.368253, 219.600186),
#                  (219.621183, 219.837003),
#                  (219.862393, 219.948331),
#                  (219.965909, 219.991300),
#                  (220.016202, 220.119717),
#                  (220.152921, 220.375577),
#                  (220.392667, 220.435635),
#                  (220.466397, 220.719815),
#                  (220.842373, 221.231533)
#                 ]
# fitspec2_freq = [(230.421720, 230.510098),
#                  (230.649259, 231.068204),
#                  (231.146329, 231.252774),
#                  (231.303067, 231.900234),
#                  (231.999844, 232.278164)
#                 ]
# fitspec3_freq = [(232.564133, 232.984055),
#                  (233.025559, 234.423507)
#                 ]



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

uvcontsub(vis = visname
          ,outputvis = visname_contsub
          ,fitspec = fitspec
          ,fitorder = 1
          ,datacolumn = 'data'

)

print("The continuum substracted file are:", visname_contsub)