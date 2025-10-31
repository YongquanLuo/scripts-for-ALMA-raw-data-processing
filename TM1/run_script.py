######### Part1 ##################################################
# Run the Part1 firstly and check the listobs information
# print("Start preprocessing...")
# execfile("pre_process.py")

######## Part2 ###################################################
# To determine a suitable threshold for tclean, it is recommended to run Part2 and obtain the noise estimate from the dirty cube before running Part3.  
print("Start generating dirty cube...")
execfile("tclean_dirty_cube.py")

print("Start substracting continuum...")  # The line-free channels can be obtained from dirty cube
execfile("uvcontsub.py")

########## Part3 ################################################
print("Start creating continuum...")
execfile("tclean_continuum.py")

print("Start creating lines cube...")
execfile("tclean_cube.py")
