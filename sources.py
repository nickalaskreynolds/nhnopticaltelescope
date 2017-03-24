'''
Calls souceplots and sourcewindow
author: Nickalas Reynolds
Date: March 2017
'''

# import modules
from __future__ import print_function
import sys
import os
from sourceplots import plots
from sourcewindow import window
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, Galactic, SkyCoord
from astropy.utils import iers     # improving precision if needed
IERSTABLE = iers.IERS_A.open(iers.IERS_A_URL)

# make example file
with open("example_all_sources.txt", "w") as f:
    f.write("2017-4-1,2017-4-1\n")
    f.write("M33,M31,HD 131399,WL 16\n")
    f.write("apo\n")
    f.write("y\n")
    f.write("n")
    f.close()

# configuring date
locations = ["norman","apo","iram30","subaru","alma"]
instring = "all_sources.txt"
print("If you rather read from file then make file: " + instring + " example in: example_" + instring)
if os.path.exists(instring):
    with open(instring, "r") as f:
        raw = f.read().splitlines()
        date = raw[0]
        source=raw[1]
        dst=raw[3]
        answero=raw[2]
        moon=raw[4]
    f.close()
else:
    while True:
        try:
            date = raw_input("Input date (2017-4-1): ")
            source = raw_input("Please list sources comma separated e.g (m33,m31): ")
            answero = raw_input("Input desired location from [{0}] : ".format(", ".join(str(i) for i in locations)))
            dst = raw_input("Is daylight savings in effect in desired timezone (y,n): ")
            moon = raw_input("Do you want to plot the moon (y/n: ")
            if len(date.split("-")) == 3:
                break
        except ValueError:
            continue
utcoffset = 0
name = answero
source=source.split(",")
date_array = date.split(",")
print(date_array)
for Date in date_array:
    print(Date)
    if dst == "y":
        utcoffset = 1*u.hour
    if answero == "apo":
        utcoffset = -7.*u.hour + utcoffset #not 6 since DST in effect
        answer = EarthLocation(lat='32d46m49s', lon='-105d49m13s', height=2788*u.m)
    elif answero == "norman":
        utcoffset = -6*u.hour + utcoffset #not 6 since DST in effect
        answer = EarthLocation(lat='35d13m21.2s', lon='-97d26m22.1s', height=370*u.m)
    elif answero == "iram30":
        utcoffset = 1*u.hour + utcoffset #not 6 since DST in effect
        answer = EarthLocation(lat='37d04m06.29s', lon='-03d23m55.51s', height=2850*u.m)
    elif answero == "subaru":
        utcoffset = 1*u.hour + utcoffset #not 6 since DST in effect
        answer = EarthLocation(lat='19d49m32s', lon='-155d28m36s', height=4139*u.m)
    elif answero == "alma":
        utcoffset = -4*u.hour + utcoffset
        answer = EarthLocation(lat='-23d01m09s', lon='-67d45m12s', height=5050*u.m)
    midnight = Time(Date+' 00:00:00') - utcoffset

    window(Date,name,source,answer,midnight,moon,IERSTABLE)
    plots(Date,name,source,answer,midnight,moon,IERSTABLE)

print("Finished all")

#############
# end of code
