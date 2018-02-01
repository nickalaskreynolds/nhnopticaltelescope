'''
Figures out the time between dates
Nickalas Reynolds
2017 March 25
'''

# import libraries
from __future__ import print_function
from astropy.time import Time
from astropy.time import TimeDelta
import datetime
now = datetime.datetime.now()

# define variables
while True:
    try:
        print("Iso format: 2010-01-01 00:00:00")
        time_init = raw_input("Input date first in iso or [RET] to do today: ")
        time_fin = raw_input("Input final date in iso: ")
        t_fin = Time(time_fin,format='iso')
    except ValueError:
        continue
    if time_fin != "":
        break
if time_init == "":
    t_init = Time(now.isoformat())
else:
    t_init = Time(time_init,format='iso')

dt = t_init - t_fin
print(dt.iso)

#############
# end of code