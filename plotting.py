'''
Pretty plots files from ALMA data sets
Original Author John Tobin
Adapted by Nickalas Reynolds
April 2017
'''

# import libraries
from __future__ import print_function
import os
import glob
import aplpy

# make example
print("Making example file.")
with open("example_plot_sources.txt",'w') as f:
    f.write("image,outfilename,ra,dec,minpixval,maxpixval,size,scalebar,distance,name,pa,showoutflow,sigma,showcontours,showsources,imagestretch,colororgray,colormap,plotlabel,textcolor\n image,outfilename,ra,dec,minpixval,maxpixval,size,scalebar,distance,name,pa,showoutflow,sigma,showcontours,showsources,imagestretch,redimage,redstart,redinterval,rednoise,showredimage,blueimage,bluestart,blueinterval,bluenoise,showblueimage,colororgray,colormap,plotlabel,textcolor\n")
    f.write('Will plot a pretty image and then plot the moment map.\n')
    f.write("# capable of handling multiple sources, just begin the next source on the next line with no line break inbetween.\n")
    f.write("#^^^^^^^^ exclude these first few lines with # ^^^^^^^^\n")
    f.write("L1448IRS3B_cont_superuniform.fits\n") 
    f.write("L1448IRS3B_cont_superuniform_C17O_all.png\n")
    f.write("51.4016208333\n")
    f.write("30.7550666667\n")
    f.write("0.00014571\n")
    f.write("0.0361\n") 
    f.write("15.0\n")
    f.write("0.1\n")
    f.write("230.0\n")
    f.write("L1448 IRS3B Cont 870micron\n")
    f.write("25.0\n")
    f.write("n\n")
    f.write("00.00014571\n")
    f.write("n\n")
    f.write("n\n")
    f.write("linear\n")
    f.write("color\n")
    f.write("jet\n")
    f.write("\n")
    f.write("white\n")
    f.write("L1448IRS3B_C17O_image_taper1500k_r.fits\n")
    f.write("3\n")
    f.write("2\n")
    f.write("0.00231\n")
    f.write("y\n")
    f.write("L1448IRS3B_C17O_image_taper1500k_b.fits\n")
    f.write("3\n")
    f.write("2\n")
    f.write("0.00675\n")
    f.write("y\n")
    f.write("L1448IRS3B_cont_superuniform_C17O_mom0_all.png\n")
    f.write("L1448 IRS3B C17O")
    f.close()

# make arrays
iname=[]
oname=[]
cra=[]
cdec=[]
lpix=[]
upix=[]
sizearc=[]
scale=[]
dist=[]
label=[]
posang=[]
plotang=[]
sigma=[]
plotcont=[]
posans=[]
colorstretch=[]
colgrey=[]
colormap=[]
plotlabel=[]
textcolor=[]
redimage=[]
redstart=[]
redinterval=[]
rednoise=[]
showredimage=[]
blueimage=[]
bluestart=[]
blueinterval=[]
bluenoise=[]
showblueimage=[]
nname=[]
plotlabel2=[]

all_files = [f for f in glob.glob('plot_sources.txt') if os.path.isfile(f)]
if len(all_files) == 0:
    print("Please input filename in next prompt or make a file following the example file at example_plot_sources.txt and rename to plot_sources.txt")
    while True:
        try:
            totalcount=raw_input("Total Number of sources: ")
            totalanswer=raw_input("Make Moments maps too?(y n):")
            totalcount=int(totalcount)
            for i in range(totalcount):
                iname.append(raw_input("Input cont image name: ")) 
                oname.append(raw_input("image to create prettyplot(with ext): ")) 
                cra.append(float(raw_input("center RA (degrees): ")))
                cdec.append(float(raw_input("center Dec (degrees): ")))
                lpix.append(float(raw_input("lower pixel value: ")))
                upix.append(float(raw_input("upper pixel value: ")))
                sizearc.append(float(raw_input("size of the image to create in arcseconds: ")))
                scale.append(float(raw_input("scale bar size: ")))
                dist.append(float(raw_input("distance (in parsecs): ")))
                label.append(raw_input("cont image title: "))
                posang.append(float(raw_input("outflow position angle: ")))
                plotang.append(raw_input("plot it (y or n): ")) 
                sigma.append(float(raw_input("uncertainty of the image (noise level): ")))
                plotcont.append(raw_input("plot contours (y or n): ")) 
                posans.append(raw_input("show source positions (y or n): "))
                colorstretch.append(raw_input("color stretch: ")) 
                colgrey.append(raw_input("color or greyscale: ")) 
                colormap.append(raw_input("color map: ")) 
                plotlabel.append(raw_input("(Leave blank or specify another title): ")) 
                textcolor.append(raw_input("text color: "))
                if totalanswer == 'y':
                    redimage.append(raw_input("red image name: "))
                    redstart.append(float(raw_input("Red Contour start: ")))
                    redinterval.append(float(raw_input("Red contour interval: ")))
                    rednoise.append(float(raw_input("Red Image Noise: ")))
                    showredimage.append(raw_input("plot red image(y n): "))
                    blueimage.append(raw_input("Blue image name: "))
                    bluestart.append(float(raw_input("Blue Contour start: ")))
                    blueinterval.append(float(raw_input("Blue Contour Interval: ")))
                    bluenoise.append(float(raw_input("Blue Image Noise: ")))
                    showblueimage.append(raw_input("Plot Blue image(y n): "))
                    nname.append(raw_input("image to create prettymoment(with ext): "))
                    plotlabel2.append(raw_input("Moment map image title: "))
        except ValueError:
            continue
        if (totcalcount != ''):
            break
        else:
            print("Please input integer for number of sources.")
            continue
else:
    import disk_images_panel as prettyplot
    import disk_images_wmom0 as prettymom
    with open("plot_sources.txt",'r') as f:
        raw = f.read().splitlines()
        for i in range(len(raw)/32):
            iname.append(raw[32*i])
            oname.append(raw[32*i+1]) 
            cra.append(raw[32*i+2])
            cdec.append(raw[32*i+3])
            lpix.append(raw[32*i+4])
            upix.append(raw[32*i+5])
            sizearc.append(raw[32*i+6]) 
            scale.append(raw[32*i+7])
            dist.append(raw[32*i+8])
            label.append(raw[32*i+9])
            posang.append(raw[32*i+10])
            plotang.append(raw[32*i+11]) 
            sigma.append(raw[32*i+12])
            plotcont.append(raw[32*i+13]) 
            posans.append(raw[32*i+14])
            colorstretch.append(raw[32*i+15]) 
            colgrey.append(raw[32*i+16]) 
            colormap.append(raw[32*i+17]) 
            plotlabel.append(raw[32*i+18]) 
            textcolor.append(raw[32*i+19])
            redimage.append(raw[32*i+20])
            redstart.append(raw[32*i+21])
            redinterval.append(raw[32*i+22])
            rednoise.append(raw[32*i+23])
            showredimage.append(raw[32*i+24])
            blueimage.append(raw[32*i+25])
            bluestart.append(raw[32*i+26])
            blueinterval.append(raw[32*i+27])
            bluenoise.append(raw[32*i+28])
            showblueimage.append(raw[32*i+29])
            nname.append(raw[32*i+30])
            plotlabel2.append(raw[32*i+31])
            tmp0=raw[32*i]
            tmp1=raw[32*i+1]
            tmp2=float(raw[32*i+2])
            tmp3=float(raw[32*i+3])
            tmp4=float(raw[32*i+4])
            tmp5=float(raw[32*i+5])
            tmp6=float(raw[32*i+6])
            tmp7=float(raw[32*i+7])
            tmp8=float(raw[32*i+8])
            tmp9=raw[32*i+9]
            tmp10=float(raw[32*i+10])
            tmp11=raw[32*i+11]
            tmp12=float(raw[32*i+12])
            tmp13=raw[32*i+13]
            tmp14=raw[32*i+14]
            tmp15=raw[32*i+15]
            tmp16=raw[32*i+16]
            tmp17=raw[32*i+17]
            tmp18=raw[32*i+18]
            tmp19=raw[32*i+19]
            tmp100=raw[32*i+20]
            tmp101=float(raw[32*i+21])
            tmp102=float(raw[32*i+22])
            tmp103=float(raw[32*i+23])
            tmp104=raw[32*i+24]
            tmp105=raw[32*i+25]
            tmp106=float(raw[32*i+26])
            tmp107=float(raw[32*i+27])
            tmp108=float(raw[32*i+28])
            tmp109=raw[32*i+29]
            tmp110=raw[32*i+30]
            tmp111=raw[32*i+31]
            os.system("rm -vf " + tmp1 + " " + tmp110)
            prettyplot.main(tmp0,tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8,tmp9,tmp10,tmp11,tmp12,tmp13,tmp14,tmp15,tmp16,tmp17,tmp18,tmp19) 
            prettymom.main(tmp0,tmp110,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8,tmp111,tmp10,tmp11,tmp12,tmp13,tmp14,tmp15,tmp100,tmp101,tmp102,tmp103,tmp104,tmp105,tmp106,tmp107,tmp108,tmp109,tmp16,tmp17,tmp18,tmp19)

if len(all_files) == 0:
    for i in range(len(iname)):
        import disk_images_panel as prettyplot
        os.system('rm -vf ' + oname[i])
        prettyplot.main(iname[i],oname[i],cra[i],cdec[i],lpix[i],upix[i],sizearc[i],scale[i],dist[i],label[i],posang[i],plotang[i],sigma[i],plotcont[i],posans[i],colorstretch[i],colgrey[i],colormap[i],plotlabel[i],textcolor[i])
        if totalanswer == 'y':
            os.system('rm -vf ' + nname[i])
            import disk_images_wmom0 as prettymom
            prettymom.main(nname[i],oname[i],cra[i],cdec[i],lpix[i],upix[i],sizearc[i],scale[i],dist[i],label[i],posang[i],plotang[i],sigma[i],plotcont[i],posans[i],colorstretch[i],redimage[i],redstart[i],redinterval[i],rednoise[i],showredimage[i],blueimage[i],bluestart[i],blueinterval[i],bluenoise[i],showblueimage[i],colgrey[i],colormap[i],plotlabel[i],textcolor[i])
