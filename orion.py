#!/usr/bin/env python
# start of code
# nickalas reynolds
# reduce orion data
###################

# libraries
import sys
from pyraf import iraf
import os
import fnmatch

# warning
print("##############################################")
print("!!!!!!!!!!!!PLEASE BACKUP DATA FIRST!!!!!!!!!!")
print("##############################################")

# define functions
def run_imstat(input):
    iraf.images()
    for image in input:
        iraf.imstat(image) 


# current directory
f = []
forig = []
mypath = raw_input("Input /full/path/to/files/ : ")
for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)
    forig.extend(filenames)
    break

# so ecl will handle files    
f = [j.replace('.','_') for j in f]
f = [j.replace('_FIT','.fits') for j in f]
f = [j.replace('_fits','.fits') for j in f]
f = [j.replace('_FLAT.','.') for j in f]
f = [j.replace('_DARK.','.') for j in f]

# defining arrays to split data sets
print("Assuming data is of the form: 'dark_10sec_.00000001.Dark.FIT' or 'orion_2_5sec_.00000001.FIT'")
time = raw_input("Please input exposure times in csv eg '10,2.5' (in seconds): ")
time = time.split(",")
time = [t.replace('.','_') for t in time]
fname = raw_input("Please input science target found in file name eg orion or source: ")
print("Also, assuming you have darks and flats.Also cannot handle file numbers > 99999999.")
filetypes=["dark","flat"]
filetypes.append(fname)

# LAST warning
print("################################################")
print("!!!!!!!!!!!!LAST CHANCE TO BACKUP DATA!!!!!!!!!!")
print("################################################")

adark=[]
aflat=[]
ascience=[]
adark = fnmatch.filter(f, 'dark*')
aflat = fnmatch.filter(f, 'flat*')
ascience = fnmatch.filter(f, fname + '*')
print("Total number of: darks ",str(len(adark)),", flats ",str(len(aflat)),", and ",fname," ",str(len(ascience)),".")
size=[str(len(adark)),str(len(aflat)),str(len(ascience))]
# moving files to appropriates names
print('Moving Files...')
for i in range(len(f)):
    os.system('mv -v '+ mypath + forig[i] + ' ' + mypath + f[i])

# open file for imstat logging
orig_stdout = sys.stdout
filestat = file(mypath + 'totalimstat.txt', 'w')
sys.stdout = filestat
iraf.imstat(mypath + "*.fits")
sys.stdout = orig_stdout
filestat.close()

# iterating through with imarith to combine flats darks
for num2 in range(2)
    for num1 in range(len(time)):
        tfile = fnmatch.filter(f, filetypes[num2] + "*" + time[num1] + "*")
        tfilename = mypath + filetypes[num2] + "_" + time[num1] + "_combine.fits"
        open(tfilename, 'w').close()
        for num in range(len(tfile))
            tmpfile = iraf.imarith(tfilename + " + " + tfile[num] + " " + tfilename)

# open file for imstat logging
orig_stdout = sys.stdout
filestat = file(mypath + 'dark_combine_imstat.txt', 'w')
sys.stdout = filestat
iraf.imstat(mypath + "dark*combine.fits")
sys.stdout = orig_stdout
filestat.close()

# open file for imstat logging
orig_stdout = sys.stdout
filestat = file(mypath + 'flat_combine_imstat.txt', 'w')
sys.stdout = filestat
iraf.imstat(mypath + "flat*combine.fits")
sys.stdout = orig_stdout
filestat.close()


#############
# end of code