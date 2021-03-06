'''
Creates plots that shows times source is up
author: Nickalas Reynolds
Editions by Joesph Choi
Date: March 2017
'''

# import modules
from __future__ import print_function
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, FK5, get_sun, Galactic
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw as Draw
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
name = answer
source=source.split(",")
if dst == "y":
    utcoffset = 1*u.hour
if answer == "apo":
    utcoffset = -7.*u.hour + utcoffset
    answer = EarthLocation(lat='32d46m49s', lon='-105d49m13s', height=2788*u.m)
elif answer == "norman":
    utcoffset = -6*u.hour + utcoffset
    answer = EarthLocation(lat='35d13m21.2s', lon='-97d26m22.1s', height=370*u.m)
elif answer == "iram30":
    utcoffset = 1*u.hour + utcoffset
    answer = EarthLocation(lat='37d04m06.29s', lon='-03d23m55.51s', height=2850*u.m)
elif answer == "subaru":
    utcoffset = -10*u.hour + utcoffset
    answer = EarthLocation(lat='19d49m32s', lon='-155d28m36s', height=4139*u.m)
elif answer == "alma":
    utcoffset = -4*u.hour + utcoffset
    answer = EarthLocation(lat='-23d01m09s', lon='-67d45m12s', height=5050*u.m)
midnight = Time(Date+' 00:00:00') - utcoffset
'''

def plots(Date,name,source,answer,midnight,moon,IERSTABLE):

    iers.IERS.iers_table = IERSTABLE
    delta_midnight = np.linspace(-12, 12, 300)*u.hour
    times = midnight + delta_midnight

    # frame transformation
    frame_obs = AltAz(obstime=times,location=answer)
    sunaltaz = get_sun(times).transform_to(frame_obs)
    if moon == "y":
        from astropy.coordinates import get_moon
        moonaltaz = get_moon(times).transform_to(frame_obs)
    planets = ['sun','mercury','venus','earth-moon-barycenter','earth','moon','mars','jupiter','saturn','uranus','neptune','pluto']
    for i,j in enumerate(source):
        if j in planets:
            source[i] = planets[planets.index(j)]
            planet_answer = 'y'
    if planet_answer == 'y':
        from astropy.coordinates import solar_system_ephemeris, get_body
        solar_system_ephemeris.set('de432s')

    # iterating through sources
    for numsource,sourcename in enumerate(source):
        n=""
        print("Starting " + source[numsource] + " ...")
        outname = n.join(source[numsource].split(" ")) + "_time_" + str(Date) + "_plot.pdf"
        os.system("rm -f " + outname + "*")
        if sourcename in planets:
            targcoord = get_body(sourcename,times,answer)
        else:
            targcoord = SkyCoord.from_name(source[numsource])
        targaltaz = targcoord.transform_to(frame_obs)
        # plotting
        plt.figure(numsource + 1) #allows code to generate and display multiple different plots
        plt.plot(delta_midnight, sunaltaz.alt, color='r', label='Sun')
        if moon == "y":
            plt.plot(delta_midnight, moonaltaz.alt, color='y', label='Moon')
        plt.scatter(delta_midnight, targaltaz.alt, c=targaltaz.az, label=source[numsource], lw=0, s=8, cmap='jet')
        plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltaz.alt < -0*u.deg, color='0.5', zorder=0)
        plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltaz.alt < -18*u.deg, color='k', zorder=0)
        plt.colorbar().set_label('Azimuth [deg]')
        plt.legend(loc='upper left')
        plt.xlim(-12,12)
        plt.xticks(np.arange(13)*2 - 12)
        plt.ylim(0, 90)
        plt.title(source[numsource] + " at " + name + " on " + Date)
        plt.xlabel('Hours from Local Midnight')
        plt.ylabel('Altitude [deg]')
        plt.savefig(outname)
        Draw()
    plt.show()
#############
# end of code
