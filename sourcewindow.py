'''
Creates file that lists times source is up
author: Nickalas Reynolds
Date: March 2017
'''

# import modules
from __future__ import print_function
import sys
import os
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, Galactic, SkyCoord
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils import iers     # improving precision if needed

#plt.style.use(astropy_mpl_style)
'''
# make example file
with open("example_all_sources.txt", "w") as f:
	f.write("2017-4-1\n")
	f.write("M33,M31,HD 131399,WL 16\n")
	f.write("apo\n")
	f.write("y")
	f.close()

# configuring date
locations = ["norman","apo","iram30","subaru","alma"]
instring = "all_sources.txt"
print("If you rather read from file then make file: " + instring + " example in: example_" + instring)
if os.path.exists(instring):
	with open(instring, "r") as f:
		raw = f.read().splitlines()
		Date = raw[0]
		source=raw[1]
		dst=raw[3]
		answer=raw[2]
	f.close()
else:
	while True:
		try:
			Date = raw_input("Input date (2017-4-1): ")
			source = raw_input("Please list sources comma separated e.g (m33,m31): ")
			answer = raw_input("Input desired location from [{0}] : ".format(", ".join(str(i) for i in locations)))
			dst = raw_input("Is daylight savings in effect in desired timezone (y,n): ")
			if len(Date.split("-")) == 3:
				break
		except ValueError:
			continue

utcoffset = 0
source=source.split(",")
if dst == "y":
	utcoffset = 1*u.hour
if answer == "apo":
	utcoffset = -7.*u.hour + utcoffset #not 6 since DST in effect
	answer = EarthLocation(lat='32d46m49s', lon='-105d49m13s', height=2788*u.m)
elif answer == "norman":
	utcoffset = -6*u.hour + utcoffset #not 6 since DST in effect
	answer = EarthLocation(lat='35d13m21.2s', lon='-97d26m22.1s', height=370*u.m)
elif answer == "iram30":
	utcoffset = 1*u.hour + utcoffset #not 6 since DST in effect
	answer = EarthLocation(lat='37d04m06.29s', lon='-03d23m55.51s', height=2850*u.m)
elif answer == "subaru":
	utcoffset = 1*u.hour + utcoffset #not 6 since DST in effect
	answer = EarthLocation(lat='19d49m32s', lon='-155d28m36s', height=4139*u.m)
midnight = Time(Date+' 00:00:00') - utcoffset
'''
def window(Date,name,source,answer,midnight,moon,IERSTABLE):

	iers.IERS.iers_table = IERSTABLE
	delta_midnight = np.linspace(-12, 12, 300)*u.hour
	# preparing file
	for numsource in range(len(source)):
		n=""
		print("Starting " + source[numsource] + " ...")
		outname = n.join(source[numsource].split(" ")) + "_time_" + str(Date) + "_window.txt"
		os.system("rm -f " + outname + "*")
		with open(outname,'a') as f,open(outname + ".bak",'a') as f1:
			# solving for gal positions
			f1.write("Fully lists the timeframe where " + source[numsource] + " will be at certain alt \n")
			f1.write("15 Minute intervals (0.25). Pairs times eg [0.0, 0.5, 11.0, 23.75] is 0000 to 0030 and 1100 to 2345 \n")
			f.write("Lists the timeframe where " + source[numsource] + " will be at certain alt \n")
			f.write("15 Minute intervals (0.25). Pairs times eg [0.0, 0.5, 11.0, 23.75] is 0000 to 0030 and 1100 to 2345 \n")
			f1.write("\n")
			f.write("\n")
			alttwenty = []
			altzero = []
			nalttwenty = []
			naltzero = []
			targcoord = SkyCoord.from_name(source[numsource])
			for i in range(96): #15 minute intervals
				frame_obs = AltAz(obstime=midnight+(i*0.25)*u.hour,location=answer)
				targaltaz = targcoord.transform_to(frame_obs)
				if targaltaz.alt > 20*u.degree:
					alttwenty.append(i*0.25)
					
				if targaltaz.alt > 0*u.degree:
					altzero.append(i*0.25)
			f1.seek(0)
			f1.write('Times at which ' + source[numsource] + ' is above an altitude of twenty degrees: \n')
			f1.seek(0)
			f1.write(str(alttwenty))
			f1.seek(0)
			f1.write('\nTimes at which ' + source[numsource] + ' is above the horizon: \n')
			f1.seek(0)
			f1.write(str(altzero))
			f1.seek(0)
			f1.write("\n")
			if alttwenty:
				nalttwenty.append(alttwenty[0])
				for i in range(len(alttwenty)-1):
					temp = alttwenty[i]
					if (temp + .25) != alttwenty[i+1]:
						nalttwenty.append(temp)
						nalttwenty.append(alttwenty[i+1])
					if i == len(alttwenty)-2:
						nalttwenty.append(alttwenty[i+1])
				alttwenty = nalttwenty
			if altzero:
				naltzero.append(altzero[0])
				for i in range(len(altzero)-1):
					temp = altzero[i]
					if (temp + .25) != altzero[i+1]:
						naltzero.append(temp)
						naltzero.append(altzero[i+1])
					if i == len(altzero)-2:
						naltzero.append(altzero[i+1])
				altzero = naltzero		
			f.seek(0)
			f.write('Times at which ' + source[numsource] + ' is above an altitude of twenty degrees: \n')
			f.seek(0)
			f.write(str(alttwenty))
			f.seek(0)
			f.write('\nTimes at which ' + source[numsource] + ' is above the horizon: \n')
			f.seek(0)
			f.write(str(altzero))
			f.seek(0)
			f.write("\n")
		# closing file
			f.close
			f1.close
		print("Finished " + source[numsource] + " ...")
		os.system("cat " + outname)

#############
# end of code