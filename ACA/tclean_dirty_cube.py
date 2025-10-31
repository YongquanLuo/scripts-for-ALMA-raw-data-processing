import ast

print("The tclean params for dirty cube are at tclean_params.txt")
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
print("The tclean params for dirty cube are:", params)
print("The file used for generating dirty cube is:", visname)


############### estimate cell size in CASA
# see more about at https://www.youtube.com/watch?v=g3iE_26j-bc
#  cell (arcsec) = 206265/ longest baseline in wavelengths / 5
# longest baseline in wavelengths can be got using plotms
#
# plotms(vis = your_visname, 
#        xaxis = 'UVwave', 
#        field = your_field, 
#        spw = spw_selected,  # such as '0'
#        avgtime = '1e6',
#        avgscan = True
#        )

#################  estimate cell size using AnalysisUtils
# cell size can be also use AnalysisUtils, but it does not accout for projection of baselines
# import sys
# sys.path.append("/luoyongquan/softwares/analysis_scripts")  # path of your AnalysisUtils
# import analysisUtils as au
# cell, imsize, t = au.pickCellSize(visname, imsize = True)

################   estimate synthesized beam using AnalysisUtils
# beam (arcsec) = au.estimateSynthesizedBeam(visname)



ms.open(visname)
freq0 = ms.cvelfreqs(spwids=0, mode='channel', width=0, outframe='LSRK')/1E6
freq1 = ms.cvelfreqs(spwids=1, mode='channel', width=0, outframe='LSRK')/1E6
freq2 = ms.cvelfreqs(spwids=2, mode='channel', width=0, outframe='LSRK')/1E6
freq3 = ms.cvelfreqs(spwids=3, mode='channel', width=0, outframe='LSRK')/1E6
ms.close()

# get dirty cube
tclean(vis = visname
       ,restart = True
       ,calcres = True
       ,calcpsf = True
       ,field = field
       ,imagename = './dirty_cube/' + visname + '.dirty_cube.spw0'
       ,datacolumn = 'corrected'
       ,spw = '0'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq0.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 0
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,45]
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
       ,imagename = './dirty_cube/' + visname + '.dirty_cube.spw1'
       ,datacolumn = 'corrected'
       ,spw = '1'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq1.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 0
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,45]
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
       ,imagename = './dirty_cube/' + visname + '.dirty_cube.spw2'
       ,datacolumn = 'corrected'
       ,spw = '2'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq2.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 0
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,45]
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
       ,imagename = './dirty_cube/' + visname + '.dirty_cube.spw3'
       ,datacolumn = 'corrected'
       ,spw = '3'
       ,specmode = 'cube'
       ,width = width
       ,start = str(freq3.min()) + 'MHz'
       ,outframe = 'LSRK'
       ,nchan = nchan
       ,threshold = threshold
       ,imsize = imsize
       ,cell = cell
       ,niter = 0
       ,deconvolver = 'multiscale'
       ,scales = [0,5,15,45]
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
