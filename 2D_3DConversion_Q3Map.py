# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:17:50 2021

@author: snowy
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import csv
from KeckIntensityStep2 import New_INTSQ3

#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
uranus_seangleK = (5.075900 + 5.065686)/2
uranus_seangleI = (35.784010 + 35.773649)/2
#stretch yy to become a sphere
flattening =0.0229
uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
uranus_seangleI_Rads = (uranus_seangleI*np.pi)/180
losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
eq_po_ratioK=1-losflattening

y_Keck = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]

y_Keckadj = y_Keck/eq_po_ratioK

losflattening=flattening*(1-np.sin((uranus_seangleI/180)*np.pi))
eq_po_ratioI=1-losflattening

y1_IRTF = -0.89263
y2_IRTF = 0.89263

y1_IRTFadj = y1_IRTF/eq_po_ratioI
y2_IRTFadj = y2_IRTF/eq_po_ratioI
#%% First lets confirm the middle from a total of Q1
# =============================================================================
# with open('MiddlePointData.csv', 'r') as file: #This reads in the file from 
#     MidP = file.read().replace('\n', ' ')
# file.close()
# 
# Middle_Points = np.fromstring(MidP, dtype=float, count=-1, sep= ' ')
# 
# for a in range(27):
#     Example_Keck = Keck_DataABBA[a*2] + Keck_DataABBA[(a*2)+1]
#     fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
#     ax.imshow(Example_Keck, cmap='gist_gray')
#     Ells = Ellipse((141.996, ((Middle_Points[4*a]+Middle_Points[2*a])/2)), 22.41004051808411, (22.41004051808411/eq_po_ratioK), angle=0, linewidth=1, fill=False)
#     ax.add_artist(Ells)
# 
# =============================================================================
#%% Now that Keck and IRTF are adjusted with y for flattening we can then start mapping latitude and longitude
#First Keck

x1_Keck = -0.68240
x2_Keck = 0.68240
r1_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[0]**2)
r11_Keck= np.sqrt(x1_Keck**2 + y_Keckadj[22]**2)
r2_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[0]**2)
r21_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[22]**2)

x_IRTF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
r1_IRTF = np.sqrt(x_IRTF[0]**2 + y1_IRTF**2)
r11_IRTF = np.sqrt(x_IRTF[21]**2 + y1_IRTF**2)
r2_IRTF = np.sqrt(x_IRTF[0]**2 + y2_IRTF**2)
r21_IRTF = np.sqrt(x_IRTF[21]**2 + y2_IRTF**2)

pheta1_Keck = math.asin(r1_Keck/11.491436449930903)
pheta2_Keck = math.asin(r2_Keck/11.491436449930903)
pheta1_IRTF = math.asin(r1_IRTF/11.25)
pheta2_IRTF = math.asin(r2_IRTF/11.25)

Contents1_Keck = (x1_Keck*np.sin(pheta1_Keck))
Contents1_Keck = Contents1_Keck/((r1_Keck*np.cos(pheta1_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[0]*np.sin(uranus_seangleK_Rads)*np.sin(pheta1_Keck)))
Long1_Keck = 0 - math.atan(Contents1_Keck)

Contents2_Keck = (np.cos(pheta1_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[0]*np.sin(pheta1_Keck)*np.cos(uranus_seangleK_Rads))/r1_Keck)
Lat1_Keck = math.asin(Contents2_Keck)

#%%So now lets get a grid of latitudes and longitudes
b = 0
LongitudeK1 = []
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck)

b = 0
LatitudeK1 = []

for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
        
plt.figure()
plt.plot(LongitudeK1, LatitudeK1, 'bo', label='First ABBA set')
plt.xlabel('Uranian Longitude (ULS) (Degrees)', fontsize=15)
plt.ylabel('Uranian Latitude (Degrees)', fontsize=15)
plt.title('Approximate Mapping of Pixel Corners over a 2D Uranian Map', fontsize=20)

b = 0
LongitudeK = []
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.03644498805576447 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.03644498805576447 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0.03644498805576447 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        
plt.plot(LongitudeK, LatitudeK, 'ro', label='Second ABBA set')

b = 0
LongitudeK = []
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 2.150251886735736 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 2.150251886735736 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (2.150251886735736 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 22:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)

plt.plot(LongitudeK, LatitudeK, 'go', label='Last ABBA set')

b = 0
LongitudeK = []
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.21866987597470938 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.21866987597470938 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0.21866987597470938 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        
plt.plot(LongitudeK, LatitudeK, 'ko', label='Next Coadded Set')
plt.legend(loc='best')

print(LatitudeK)
print(len(LatitudeK))

#%% Now lets work out 42 Latitudes and Longitudes along over 54 sets
#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
LONGs = []
LATs = []
Places_List = [3, 9, 15, 21, 27, 33, 40, 45, 52, 58, 64, 71, 77, 83, 89, 96, 102, 108, 113, 123, 131, 139, 146, 153, 158, 164, 170, 177, 183, 209, 215, 223, 228, 234, 240, 248, 254, 261, 266, 273, 279, 285, 291, 297, 303, 309, 315, 321, 328, 334, 340, 346, 351, 357]

with open('DataKeck06.txt', 'r') as file: #This reads in the file 
    for row in file:
        Data = row.rstrip("\n").split('   ')
        LONGs.append(Data[1])
        LATs.append(Data[2])

Longs = []
Lats = []
for a in range(54):
    b = Places_List[a]
    Longs.append(float(LONGs[b]))
    Lats.append(float(LATs[b]))

LongitudeK = []
LatitudeK = []
Extra = ((4/60)/17.24)*360

for m in range(54):
    uranus_seangleK = -1*Lats[m]
    flattening = 0.0229
    uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
    losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
    eq_po_ratioK=1-losflattening
    y_Keck = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
    y_Keckadj = y_Keck/eq_po_ratioK
    x1_Keck = -0.68240
    x2_Keck = 0.68240
    b = 0
    for a in range(46):
        if b < 1 and a < 22:
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
            Lat_Keck = math.asin(Contents2_Keck)
            Lat_Keck = (Lat_Keck*180)/np.pi
            LatitudeK.append(Lat_Keck)
            Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
            Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
            if Longs[m] > 300:
                Long_Keck = (Longs[m] - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
            else:
                Long_Keck = (Longs[m] + 360 - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
        elif b == 0 and a == 22:
             r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
             pheta_Keck = math.asin(r_Keck/11.491436449930903)
             Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
             Lat_Keck = math.asin(Contents2_Keck)
             Lat_Keck = (Lat_Keck*180)/np.pi
             LatitudeK.append(Lat_Keck)
             Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
             Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
             if Longs[m] > 300:
                Long_Keck = (Longs[m] - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
             else:
                Long_Keck = (Longs[m] + 360 - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180  - math.atan(Contents1_Keck)
                LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
             b = 1
        elif b == 1 and a >= 23:
            c = a - 23
            r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
            Lat_Keck = math.asin(Contents2_Keck)
            Lat_Keck = (Lat_Keck*180)/np.pi
            LatitudeK.append(Lat_Keck)
            Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
            Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
            if Longs[m] > 300:
                Long_Keck = (Longs[m] - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append((Long_Keck*180)/np.pi)
            else:
                Long_Keck = (Longs[m] + 360 - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append((Long_Keck*180)/np.pi)
                
#%% Now to calculate 108 lines (Latitudes are all the same so same 2 lines repeated)
#So work out all 1 degree positions 
from PIL import Image, ImageDraw

polygon = [(54.79048937158515, LatitudeK[0]+90), (0, LatitudeK[23]+90), (18.378874127804103, LatitudeK[1]+90), (36.41161524378105, LatitudeK[24]+90)]
polygon2 = [(LongitudeK[1]+27.395244685792576, LatitudeK[1]+90), (LongitudeK[24]+27.395244685792576, LatitudeK[24]+90), (LongitudeK[25]+27.395244685792576, LatitudeK[2]+90), (LongitudeK[2]+27.395244685792576, LatitudeK[25]+90)]
width = 360
height = 180

img = Image.new('L', (width, height), 0)
for i in range(22):
    polygon = [(LongitudeK[i]+27.395244685792576, LatitudeK[i]+90), (LongitudeK[23+i]+27.395244685792576, LatitudeK[23+i]+90), (LongitudeK[24+i]+27.395244685792576, LatitudeK[1+i]+90), (LongitudeK[1+i]+27.395244685792576, LatitudeK[24+i]+90)]
    ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
        
#ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
#ImageDraw.Draw(img).polygon(polygon2, outline=1, fill=1)
Slit0 = np.flipud(np.array(img))

plt.figure()
plt.imshow(Slit0)

img2 = Image.new('L', (width, height), 0)
for i in range(22):
    ii = i + 46
    polygon = [(LongitudeK[ii]+27.395244685792576, LatitudeK[ii]+90), (LongitudeK[23+ii]+27.395244685792576, LatitudeK[23+ii]+90), (LongitudeK[24+ii]+27.395244685792576, LatitudeK[1+ii]+90), (LongitudeK[1+ii]+27.395244685792576, LatitudeK[24+ii]+90)]
    ImageDraw.Draw(img2).polygon(polygon, outline=1, fill=1)

Slit1 = np.flipud(np.array(img2))
plt.figure()
plt.imshow(Slit1)

#Now lets times the mask over the first slit values
Filler = np.zeros(156)
Test = []
Limits = []
for a in range(54):
    Limits.append(round(LongitudeK[(a*23)] + LongitudeK[0]))
    Limits.append(round(LongitudeK[(a*23)+23] + LongitudeK[0]))

#%% So now to make 54 images of each slit 
SLITS = []
SLITShapes = []

for A in range(54):
    width = 181
    height = 181
    img = Image.new('L', (width, height), 0)
    if A >= 27 and A <= 35:
        for i in range(22):
            xx = A*46
            polygon = [(LongitudeK[xx+i]+27.395244685792576, LatitudeK[xx+i]+90), (LongitudeK[23+xx+i]+27.395244685792576, LatitudeK[23+xx+i]+90), (LongitudeK[24+xx+i]+27.395244685792576, LatitudeK[1+xx+i]+90), (LongitudeK[1+xx+i]+27.395244685792576, LatitudeK[24+xx+i]+90)]
            ImageDraw.Draw(img).polygon(polygon, outline=0, fill=0)
    else:
        for i in range(22):
            xx = A*46
            polygon = [(LongitudeK[xx+i]+27.395244685792576, LatitudeK[xx+i]+90), (LongitudeK[23+xx+i]+27.395244685792576, LatitudeK[23+xx+i]+90), (LongitudeK[24+xx+i]+27.395244685792576, LatitudeK[1+xx+i]+90), (LongitudeK[1+xx+i]+27.395244685792576, LatitudeK[24+xx+i]+90)]
            ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
    Slit = np.flipud(np.array(img))
    for ii in range(181):
        if ii == 0:
            for iii in range(156):
                vi = 83 - iii
                d = A
                if vi == 83:
                    Tests = New_INTSQ3[21,d]
                elif vi < 83 and vi > 68:
                    Tests = np.append(Tests, (New_INTSQ3[21,d]))             
                elif vi <= 68 and vi > 58:
                    Tests = np.append(Tests, (New_INTSQ3[20,d]))
                elif vi <= 58 and vi > 50:
                    Tests = np.append(Tests, (New_INTSQ3[19,d]))
                elif vi <= 50 and vi > 44:
                    Tests = np.append(Tests, (New_INTSQ3[18,d]))
                elif vi <= 44 and vi > 37:
                    Tests = np.append(Tests, (New_INTSQ3[17,d]))
                elif vi <= 37 and vi > 31:
                    Tests = np.append(Tests, (New_INTSQ3[16,d]))
                elif vi <= 31 and vi > 26:
                    Tests = np.append(Tests, (New_INTSQ3[15,d]))
                elif vi <= 26 and vi > 21:
                    Tests = np.append(Tests, (New_INTSQ3[14,d]))
                elif vi <= 21 and vi > 15:
                    Tests = np.append(Tests, (New_INTSQ3[13,d]))
                elif vi <= 15 and vi > 10:
                    Tests = np.append(Tests, (New_INTSQ3[12,d]))
                elif vi <= 10 and vi > 5:
                    Tests = np.append(Tests, (New_INTSQ3[11,d]))
                elif vi <= 5 and vi > 0:
                    Tests = np.append(Tests, (New_INTSQ3[10,d]))
                elif vi <= 0 and vi > -5:
                    Tests = np.append(Tests, (New_INTSQ3[9,d]))
                elif vi <= -5 and vi > -10:
                    Tests = np.append(Tests, (New_INTSQ3[8,d]))
                elif vi <= -10 and vi > -16:
                    Tests = np.append(Tests, (New_INTSQ3[7,d]))
                elif vi <= -16 and vi > -21:
                    Tests = np.append(Tests, (New_INTSQ3[6,d]))
                elif vi <= -21 and vi > -27:
                    Tests = np.append(Tests, (New_INTSQ3[5,d]))
                elif vi <= -27 and vi > -33:
                    Tests = np.append(Tests, (New_INTSQ3[4,d]))
                elif vi <= -33 and vi > -40:
                    Tests = np.append(Tests, (New_INTSQ3[3,d]))
                elif vi <= -40 and vi > -48:
                    Tests = np.append(Tests, (New_INTSQ3[2,d]))
                elif vi <= -48 and vi > -58:
                    Tests = np.append(Tests, (New_INTSQ3[1,d]))
                elif vi <= -58 and vi >= -73:
                    Tests = np.append(Tests, (New_INTSQ3[0,d]))
            Test_1 = np.array(Tests)
        elif ii > 0 and ii <= 181:
            for iii in range(156):
                vi = 83 - iii     
                if vi == 83:
                    Tests = New_INTSQ3[21,d]
                elif vi < 83 and vi > 68:
                    Tests = np.append(Tests, (New_INTSQ3[21,d]))             
                elif vi <= 68 and vi > 58:
                    Tests = np.append(Tests, (New_INTSQ3[20,d]))
                elif vi <= 58 and vi > 50:
                    Tests = np.append(Tests, (New_INTSQ3[19,d]))
                elif vi <= 50 and vi > 44:
                    Tests = np.append(Tests, (New_INTSQ3[18,d]))
                elif vi <= 44 and vi > 37:
                    Tests = np.append(Tests, (New_INTSQ3[17,d]))
                elif vi <= 37 and vi > 31:
                    Tests = np.append(Tests, (New_INTSQ3[16,d]))
                elif vi <= 31 and vi > 26:
                    Tests = np.append(Tests, (New_INTSQ3[15,d]))
                elif vi <= 26 and vi > 21:
                    Tests = np.append(Tests, (New_INTSQ3[14,d]))
                elif vi <= 21 and vi > 15:
                    Tests = np.append(Tests, (New_INTSQ3[13,d]))
                elif vi <= 15 and vi > 10:
                    Tests = np.append(Tests, (New_INTSQ3[12,d]))
                elif vi <= 10 and vi > 5:
                    Tests = np.append(Tests, (New_INTSQ3[11,d]))
                elif vi <= 5 and vi > 0:
                    Tests = np.append(Tests, (New_INTSQ3[10,d]))
                elif vi <= 0 and vi > -5:
                    Tests = np.append(Tests, (New_INTSQ3[9,d]))
                elif vi <= -5 and vi > -10:
                    Tests = np.append(Tests, (New_INTSQ3[8,d]))
                elif vi <= -10 and vi > -16:
                    Tests = np.append(Tests, (New_INTSQ3[7,d]))
                elif vi <= -16 and vi > -21:
                    Tests = np.append(Tests, (New_INTSQ3[6,d]))
                elif vi <= -21 and vi > -27:
                    Tests = np.append(Tests, (New_INTSQ3[5,d]))
                elif vi <= -27 and vi > -33:
                    Tests = np.append(Tests, (New_INTSQ3[4,d]))
                elif vi <= -33 and vi > -40:
                    Tests = np.append(Tests, (New_INTSQ3[3,d]))
                elif vi <= -40 and vi > -48:
                    Tests = np.append(Tests, (New_INTSQ3[2,d]))
                elif vi <= -48 and vi > -58:
                    Tests = np.append(Tests, (New_INTSQ3[1,d]))
                elif vi <= -58 and vi >= -73:
                    Tests = np.append(Tests, (New_INTSQ3[0,d]))
            Test_1 = np.hstack((Test_1, Tests))
        else:
            pass
    Mapping_Q3 = np.reshape(Test_1, (181, 156))
    Mapping_Q3 = Mapping_Q3.transpose()
    Mapping_Q3 = np.flipud(Mapping_Q3)
    Blank = np.zeros((8, 181))
    Blank3 = np.zeros((17, 181))
    Mapping_Q3 = np.vstack((Blank, Mapping_Q3))
    Mapping_Q3 = np.vstack((Mapping_Q3, Blank3))

    FIN_SLIT = Slit*Mapping_Q3*(10**6)
# =============================================================================
#     plt.figure()
#     plt.imshow(FIN_SLIT, cmap='nipy_spectral')
#     cbar = plt.colorbar()
#     cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(0.08)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=17.5) 
#     plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$', pad = 45, fontsize = 20)
#     plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
#     plt.ylabel('Latitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
#     plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
#     plt.xticks(np.arange(0, 181, 20), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=11)
#     plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=11)
#     #plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
#     plt.vlines((0, 20, 40, 600, 80, 100, 120, 140, 160, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.4)
#     plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.4)
#     plt.ylim(181, 0) #1801, -1
#     plt.xlim(0, 181) #0, 3601
# =============================================================================
    SLITS.append(FIN_SLIT)
    SLITShapes.append(Slit)

#%% Now we need to make two arrays (One that lets us know how many pixels intersect and the other to just keep adding the values together)
#First lets focus on the number

Slits_Mask = np.zeros((181,181))
FINAL_MAP = np.zeros((181,181))

for a in range(54):
    Slits_Mask = Slits_Mask + SLITShapes[a]
    FINAL_MAP = FINAL_MAP + SLITS[a]

#Slits_Mask[61:121, 94][Slits_Mask[61:121, 94] == 0] = 1
Slits_Mask[Slits_Mask == 0] = 0
plt.figure()
plt.imshow(Slits_Mask)

#Now to add all FIN_SLITS together and divide it by Slits Mask
KECK_06_MAP = (FINAL_MAP)/Slits_Mask
KECK_06_MAP[KECK_06_MAP <= 0] = np.nan
#KECK_06_MAP[KECK_06_MAP > 0.8] = np.nan

plt.figure()
plt.imshow(KECK_06_MAP, cmap='nipy_spectral')
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(0.07)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
cbar.ax.tick_params(labelsize=15)
#plt.title(r'Intensity above Mean of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
plt.xticks(np.arange(0, 361, 20), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 361, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$', '210$^\circ$', '240$^\circ$', '270$^\circ$', '300$^\circ$', '330$^\circ$', '360$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
#plt.hlines((0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360), 0, 360, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(0, 180) #0, 3601
#plt.xlim(0, 360) #0, 3601

np.save('Step5ConversionQ3.npy', KECK_06_MAP)