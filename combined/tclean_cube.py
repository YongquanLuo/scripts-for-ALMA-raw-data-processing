import numpy as np
import ast

print("The tclean params for lines cube are at tclean_params.txt")
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

visname = params['concat_contsub']
field = params['field']
width = params['width']
nchan = params['nchan']
threshold = params['threshold_cube']
imsize = params['imsize']
cell = params['cell']
print("The tclean params for lines cube are:", params)


ms.open(field + ".ms.TM1.spw25_27_29_31.contsub")
freq0 = ms.cvelfreqs(spwids=0, mode='channel', width=0, outframe='LSRK')/1E6
freq1 = ms.cvelfreqs(spwids=1, mode='channel', width=0, outframe='LSRK')/1E6
freq2 = ms.cvelfreqs(spwids=2, mode='channel', width=0, outframe='LSRK')/1E6
freq3 = ms.cvelfreqs(spwids=3, mode='channel', width=0, outframe='LSRK')/1E6
ms.close()


tclean(vis = visname
       ,restart = True
       ,calcres = True
       ,calcpsf = True
       ,field = field
       ,imagename = './cube/' + visname + '.cube.spw0'
       ,datacolumn = 'corrected'
       ,spw = '0,4,8'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq0.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 1000000
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,50,150]
       ,gridder = 'mosaic'
       ,weighting = 'briggs'
       ,robust = 0.5
       ,pbcor = True
       ,pblimit = 0.2
      #  ,restroringbeam = 'common'
       ,usemask = 'auto-multithresh'
       ,sidelobethreshold = 2.0
       ,noisethreshold = 4.25
       ,minbeamfrac = 0.3
       ,lownoisethreshold = 1.5
      #  ,chanchunks = -1
       ,perchanweightdensity = True
       ,interactive = False
       ,parallel = True
       ,cycleniter = 2000
       ,nmajor = 5
       ,negativethreshold = 6
)

tclean(vis = visname
       ,restart = True
       ,calcres = True
       ,calcpsf = True
       ,field = field
       ,imagename = './cube/' + visname + '.cube.spw1'
       ,datacolumn = 'corrected'
       ,spw = '1,5,9'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq1.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 1000000
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,50,150]
       ,gridder = 'mosaic'
       ,weighting = 'briggs'
       ,robust = 0.5
       ,pbcor = True
       ,pblimit = 0.2
      #  ,restroringbeam = 'common'
       ,usemask = 'auto-multithresh'
       ,sidelobethreshold = 2.0
       ,noisethreshold = 4.25
       ,minbeamfrac = 0.3
       ,lownoisethreshold = 1.5
      #  ,chanchunks = -1
       ,perchanweightdensity = True
       ,interactive = False
       ,parallel = True
       ,cycleniter = 2000
       ,nmajor = 5
       ,negativethreshold = 6
       
)

tclean(vis = visname
       ,restart = True
       ,calcres = True
       ,calcpsf = True
       ,field = field
       ,imagename = './cube/' + visname + '.cube.spw2'
       ,datacolumn = 'corrected'
       ,spw = '2,6,10'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq2.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 1000000
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,50,150]
       ,gridder = 'mosaic'
       ,weighting = 'briggs'
       ,robust = 0.5
       ,pbcor = True
       ,pblimit = 0.2
      #  ,restroringbeam = 'common'
       ,usemask = 'auto-multithresh'
       ,sidelobethreshold = 2.0
       ,noisethreshold = 4.25
       ,minbeamfrac = 0.3
       ,lownoisethreshold = 1.5
      #  ,chanchunks = -1
       ,perchanweightdensity = True
       ,interactive = False
       ,parallel = True
       ,cycleniter = 2000
       ,nmajor = 5
       ,negativethreshold = 6
       
)

tclean(vis = visname
       ,restart = True
       ,calcres = True
       ,calcpsf = True
       ,field = field
       ,imagename = './cube/' + visname + '.cube.spw3'
       ,datacolumn = 'corrected'
       ,spw = '3,7,11'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq3.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 1000000
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,50,150]
       ,gridder = 'mosaic'
       ,weighting = 'briggs'
       ,robust = 0.5
       ,pbcor = True
       ,pblimit = 0.2
      #  ,restroringbeam = 'common'
       ,usemask = 'auto-multithresh'
       ,sidelobethreshold = 2.0
       ,noisethreshold = 4.25
       ,minbeamfrac = 0.3
       ,lownoisethreshold = 1.5
      #  ,chanchunks = -1
       ,perchanweightdensity = True
       ,interactive = False
       ,parallel = True
       ,cycleniter = 2000
       ,nmajor = 5
       ,negativethreshold = 6
       
)