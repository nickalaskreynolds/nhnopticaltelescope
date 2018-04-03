'''
Converts radec back and forth
Nickalas Reynolds
'''
from collections import Iterable

def typecheck(obj): 
    '''
    Checks if object is iterable (array,list,tuple) and not string
    '''
    return not isinstance(obj, str) and isinstance(obj, Iterable)

def checkconv(coord):
    '''
    will take a coord convert to a list
    return the decimal conversion
    '''
    delimiters = [':',' ',',']
    failed = False
    orig = coord
    # if a string, handle
    if type(coord) == float:
        return coord
    if type(coord) == str:
        # check if float hidden as string
        try:
            return float(coord)
        except:
            # handle string proper by going through all delimiters
            count = 0
            while not typecheck(coord):
                #print(count)
                coord = coord.split(delimiters[count])
                if len(coord) == 1:
                    coord = coord[0]
                if count == len(delimiters) - 1:
                    failed = True
                    break
                count += 1
    # try with different scheme
    if failed == True:
        hold = coord
        sp = 'h'
        t0 = hold.split(sp)[0]
        if t0 == hold:
            sp = 'd'
            t0 = hold.split(sp)[0]


        if len([x for x in hold.split(sp) if x != '']) == 1:
            coord = [t0]
        else:
            t1 = hold.split(sp)[1].split('m')[0]
            if len(t1.split('.')) == 1:
                t2 = hold.split(sp)[1].split('m')[1].strip('s')
            else:
                t2 = ''
            hold = [t0,t1,t2]
            hold = [x for x in hold if ((x != '' )and (type(x) == str))]
            coord = hold

    # if list, make to float, final form
    #print(len(coord),orig)
    if typecheck(coord):
        if len(coord) == 3:
            temp0,temp1,temp2 = map(float,coord)
            total = abs(temp0) + temp1/60. + temp2/3600
        elif len(coord) == 2:
            temp0,temp1 = map(float,coord)
            temp2 = temp1/60. - temp1
            total = abs(temp0) + temp1/60. + temp2/3600
        elif len(coord) == 1:
            # if an iterable of len one with float
            try:
                return float(coord[0])
            except:
                return checkconv(coord[0])
        if temp0 < 0.:
            total = total * -1
    return total

def icrs_hr(icrs):
    tmp0 = float(icrs[0])
    tmp01 = tmp0
    if tmp01 < 0:
        tmp0 = abs(tmp0)
    tmp1 = abs(float(icrs[1])/60.)
    tmp2 = abs(float(icrs[2])/3600.)
    icrs = tmp0 + tmp1 + tmp2
    if tmp01 < 0:
        icrs = icrs * -1.
    return icrs
def hr_icrs(hr):
    tmp0 = int(hr)
    tmp1 = int((hr - float(tmp0))*60.)
    tmp2 = float(((hr - float(tmp0))*60. - tmp1)*60.)
    icrs = str(tmp0) + ":" + str(abs(tmp1)) + ":" + "{0:.2f}".format(round(abs(tmp2),2))
    return icrs

if __name__ == "__main__":
    while True:
        try:
            ra_orig = raw_input('Input RA in any standard format: ')
            dec_orig = raw_input('Input DEC in any standard format: ')
            radecformat = raw_input('Input RA DEC format (deg, hourangle, icrs): ')
            ra_fin = float(ra_orig)
            dec_fin = float(dec_orig)
        except ValueError:
            try:
                ra_fin = ra_orig.split(':')
                dec_fin = dec_orig.split(':')
                if len(ra_fin) == 1:
                    ra_fin =  ra_orig.split(' ')            
                if len(dec_fin) == 1:
                    dec_fin =  dec_orig.split(' ')
                if ((len(dec_fin) == 3) and (len(ra_fin) == 3)):
                    break
                else:
                    continue
            except ValueError:
                continue
            continue
        if radecformat in ['deg', 'hourangle', 'icrs']:
            break
        else:
            print("Please input valid format.")
            continue

    print('Capable of converting hhmmss to decimal degrees and vice versa')
    print('Formats:')
    print('ircs: 06:04:04 -10:04:28 or 06 04 04 -10 04 28')
    print('deg: 91.0167 -10.0744')
    print('hourangle: 6.067778 -10.0744')

    print(map(float,ra_fin),radecformat)

    if (type(ra_fin) is float) and (radecformat == 'deg'):
        ra_temp = ra_fin/15.
        dec_temp = dec_fin
        print('converting to hourangle:')
        print('RA:  ' + str(ra_temp))
        print('DEC: ' + str(dec_temp))
        print('converting to icrs:')
        print('RA:  ' + hr_icrs(ra_temp))
        print('DEC: ' + hr_icrs(dec_temp))
    elif (type(ra_fin) is float) and (radecformat == 'hourangle'):
        ra_temp = ra_fin*15.
        dec_temp = dec_fin
        print('converting to deg:')
        print('RA:  ' + str(ra_temp))
        print('DEC: ' + str(dec_temp))
        print('converting to icrs:')
        print('RA:  ' + hr_icrs(ra_fin))
        print('DEC: ' + hr_icrs(dec_fin))
    elif (type(ra_fin) is list) and (radecformat == 'icrs'):
        print('converting to hourangle:')
        print('RA:  ' + str(icrs_hr(ra_fin)))
        print('DEC: ' + str(icrs_hr(dec_fin)))
        print('converting to deg:')
        print('RA:  ' + str(icrs_hr(ra_fin)*15.))
        print('DEC: ' + str(icrs_hr(dec_fin)))
        # convert to 