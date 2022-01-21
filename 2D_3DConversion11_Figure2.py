# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:17:50 2021

@author: snowy
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from KeckIntensityStep_h3ppy import New_IntQ1B, New_IntQ3B, New_CD, New_Temp, New_TE
from KeckIntensityStep1 import Keck_DataABBA

#%%#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
uranus_seangleK = (5.075900 + 5.065686)/2
uranus_seangleI = (35.784010 + 35.773649)/2
#stretch yy to become a sphere
flattening =0.0229
uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
uranus_seangleI_Rads = (uranus_seangleI*np.pi)/180
losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
eq_po_ratioK=1-losflattening

y_Keck = [11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11]

y_Keckadj = y_Keck/eq_po_ratioK

losflattening=flattening*(1-np.sin((uranus_seangleI/180)*np.pi))
eq_po_ratioI=1-losflattening

y1_IRTF = -0.89263
y2_IRTF = 0.89263

y1_IRTFadj = y1_IRTF/eq_po_ratioI
y2_IRTFadj = y2_IRTF/eq_po_ratioI

#%% Now that Keck and IRTF are adjusted with y for flattening we can then start mapping latitude and longitude
#First Keck

x1_Keck = -0.68240
x2_Keck = 0.68240
r1_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[0]**2)
r11_Keck= np.sqrt(x1_Keck**2 + y_Keckadj[10]**2)
r2_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[0]**2)
r21_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[10]**2)

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
Extra = ((27/60)/17.24)*360
#First lets sort Latitudes
for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck+Extra)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck)

b = 0
LatitudeK1 = []

for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
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
for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.1457799347697654 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.1457799347697654 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0.1457799347697654 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        
plt.plot(LongitudeK, LatitudeK, 'ro', label='Second ABBA set')

b = 0
LongitudeK = []
Extra = ((27/60)/17.24)*360
#First lets sort Latitudes
for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 1.9741013903855542 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 1.9741013903855542 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (1.9741013903855542 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(24):
    if b < 1 and a < 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif b == 0 and a == 11:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a >= 12:
        c = a - 12
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)

plt.plot(LongitudeK, LatitudeK, 'go', label='Last ABBA set')

# =============================================================================
# b = 0
# LongitudeK = []
# #First lets sort Latitudes
# for a in range(21):
#     if b < 1 and a < 10:
#         r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
#         Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
#         Long_Keck = 0.21866987597470938 - math.atan(Contents1_Keck)
#         Long_Keck = (Long_Keck*180)/np.pi
#         LongitudeK.append(Long_Keck)
#     elif b == 0 and a == 10:
#         r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
#         Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
#         Long_Keck = 0.21866987597470938 - math.atan(Contents1_Keck)
#         Long_Keck =(Long_Keck*180)/np.pi
#         LongitudeK.append(Long_Keck)
#         b = 1
#     elif b == 1 and a >= 11:
#         c = a - 11
#         r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
#         Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
#         Long_Keck = (0.21866987597470938 - math.atan(Contents1_Keck))
#         Long_Keck = (Long_Keck*180)/np.pi
#         LongitudeK.append(Long_Keck)
# 
# b = 0
# LatitudeK = []
# 
# for a in range(21):
#     if b < 1 and a <10:
#         r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
#         Lat_Keck = math.asin(Contents2_Keck)
#         Lat_Keck = (Lat_Keck*180)/np.pi
#         LatitudeK.append(Lat_Keck)
#     elif b == 0 and a == 10:
#         r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
#         Lat_Keck = math.asin(Contents2_Keck)
#         Lat_Keck = (Lat_Keck*180)/np.pi
#         LatitudeK.append(Lat_Keck)
#         b = 1
#     elif b == 1 and a >= 11:
#         c = a - 11
#         r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
#         pheta_Keck = math.asin(r_Keck/11.491436449930903)
#         Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[c]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
#         Lat_Keck = math.asin(Contents2_Keck)
#         Lat_Keck = (Lat_Keck*180)/np.pi
#         LatitudeK.append(Lat_Keck)
#         
# plt.plot(LongitudeK, LatitudeK, 'ko', label='Next Coadded Set')
# =============================================================================
plt.legend(loc='best')

print(LatitudeK)
print(len(LatitudeK))

#%% Now lets work out 42 Latitudes and Longitudes along over 54 sets
#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
LONGs = []
LATs = []
Places_List = [11, 35, 61, 85, 112, 141, 167, 202, 237, 263, 287, 311, 337]

with open('DataKeck06.txt', 'r') as file: #This reads in the file 
    for row in file:
        Data = row.rstrip("\n").split('   ')
        LONGs.append(Data[1])
        LATs.append(Data[2])

Longs = []
Lats = []
for a in range(13):
    b = Places_List[a]
    Longs.append(float(LONGs[b]))
    Lats.append(float(LATs[b]))

LongitudeK = []
LatitudeK = []

for m in range(13):
    uranus_seangleK = -1*Lats[m]
    flattening = 0.0229
    uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
    losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
    eq_po_ratioK=1-losflattening
    y_Keck = [11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11]
    y_Keckadj = y_Keck/eq_po_ratioK
    x1_Keck = -0.68240
    x2_Keck = 0.68240
    b = 0
    for a in range(24):
        if b < 1 and a < 11:
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
        elif b == 0 and a == 11:
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
        elif b == 1 and a >= 12:
            c = a - 12
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

# =============================================================================
# polygon = [(54.79195714973601, LatitudeK[0]+90), (0, LatitudeK[23]+90), (20.93325239054063, LatitudeK[1]+90), (33.858704759195376, LatitudeK[24]+90)]
# polygon2 = [(LongitudeK[1]+27.395244685792576, LatitudeK[1]+90), (LongitudeK[24]+27.395244685792576, LatitudeK[24]+90), (LongitudeK[25]+27.395244685792576, LatitudeK[2]+90), (LongitudeK[2]+27.395244685792576, LatitudeK[25]+90)]
# =============================================================================
width = 360
height = 180

img = Image.new('L', (width, height), 0)
for i in range(11):
    polygon = [(LongitudeK[i]+27.395978574868003, LatitudeK[i]+90), (LongitudeK[12+i]+27.395978574868003, LatitudeK[12+i]+90), (LongitudeK[13+i]+27.395978574868003, LatitudeK[1+i]+90), (LongitudeK[1+i]+27.395978574868003, LatitudeK[13+i]+90)]
    ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
        
#ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
#ImageDraw.Draw(img).polygon(polygon2, outline=1, fill=1)
Slit0 = np.flipud(np.array(img))

plt.figure()
plt.imshow(Slit0)

img2 = Image.new('L', (width, height), 0)
for i in range(11):
    ii = i + 24
    polygon = [(LongitudeK[ii]+27.395978574868003, LatitudeK[ii]+90), (LongitudeK[12+ii]+27.395978574868003, LatitudeK[12+ii]+90), (LongitudeK[13+ii]+27.395978574868003, LatitudeK[1+ii]+90), (LongitudeK[1+ii]+27.395978574868003, LatitudeK[13+ii]+90)]
    ImageDraw.Draw(img2).polygon(polygon, outline=1, fill=1)

Slit1 = np.flipud(np.array(img2))
plt.figure()
plt.imshow(Slit1)

#Now lets times the mask over the first slit values
Filler = np.zeros(157)
Test = []
# =============================================================================
# Limits = []
# # =============================================================================
# # for a in range(54):
# #     Limits.append(round(LongitudeK[(a*23)] + LongitudeK[0]))
# #     Limits.append(round(LongitudeK[(a*23)+23] + LongitudeK[0]))
# # =============================================================================
# =============================================================================

#%% So now to make 54 images of each slit 
SLITSQ1 = []
SLITSQ3 = []
SLITSTemp = []
SLITSCD = []
SLITSE = []
SLITShapes = []

for A in range(13):
    width = 181
    height = 181
    img = Image.new('L', (width, height), 0)
    for i in range(11):
        xx = A*24
        polygon = [(LongitudeK[xx+i]+27.395978574868003, LatitudeK[xx+i]+90), (LongitudeK[12+xx+i]+27.395978574868003, LatitudeK[12+xx+i]+90), (LongitudeK[13+xx+i]+27.395978574868003, LatitudeK[1+xx+i]+90), (LongitudeK[1+xx+i]+27.395978574868003, LatitudeK[13+xx+i]+90)]
        if A == 7 or A == 8:
            ImageDraw.Draw(img).polygon(polygon, outline=0, fill=0)
        else:
            ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
    Slit = np.flipud(np.array(img))
    for ii in range(181):
        if ii == 0:
            for iii in range(156):
                vi = 83 - iii
                d = A
                if vi == 83:
                    Tests = New_IntQ1B[10,d]
                    Tests1 = New_CD[10,d]
                    Tests2 = New_Temp[10,d]
                    Tests3 = New_IntQ3B[10,d]
                    Tests4 = New_TE[10,d]
                elif vi < 83 and vi > 58:
                    Tests = np.append(Tests, New_IntQ1B[10,d])
                    Tests1 = np.append(Tests1, New_CD[10,d])
                    Tests2 = np.append(Tests2, New_Temp[10,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[10,d])
                    Tests4 = np.append(Tests4, New_TE[10,d])
                elif vi <= 58 and vi > 44:
                    Tests = np.append(Tests, New_IntQ1B[9,d])
                    Tests1 = np.append(Tests1, New_CD[9,d])
                    Tests2 = np.append(Tests2, New_Temp[9,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[9,d])
                    Tests4 = np.append(Tests4, New_TE[9,d])
                elif vi <= 44 and vi > 31:
                    Tests = np.append(Tests, New_IntQ1B[8,d])
                    Tests1 = np.append(Tests1, New_CD[8,d])
                    Tests2 = np.append(Tests2, New_Temp[8,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[8,d])
                    Tests4 = np.append(Tests4, New_TE[8,d])
                elif vi <= 31 and vi > 21:
                    Tests = np.append(Tests, New_IntQ1B[7,d])
                    Tests1 = np.append(Tests1, New_CD[7,d])
                    Tests2 = np.append(Tests2, New_Temp[7,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[7,d])
                    Tests4 = np.append(Tests4, New_TE[7,d])
                elif vi <= 21 and vi > 10:
                    Tests = np.append(Tests, New_IntQ1B[6,d])
                    Tests1 = np.append(Tests1, New_CD[6,d])
                    Tests2 = np.append(Tests2, New_Temp[6,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[6,d])
                    Tests4 = np.append(Tests4, New_TE[6,d])
                elif vi <= 10 and vi > 0:
                    Tests = np.append(Tests, New_IntQ1B[5,d])
                    Tests1 = np.append(Tests1, New_CD[5,d])
                    Tests2 = np.append(Tests2, New_Temp[5,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[5,d])
                    Tests4 = np.append(Tests4, New_TE[5,d])
                elif vi <= 0 and vi > -10:
                    Tests = np.append(Tests, New_IntQ1B[4,d])
                    Tests1 = np.append(Tests1, New_CD[4,d])
                    Tests2 = np.append(Tests2, New_Temp[4,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[4,d])
                    Tests4 = np.append(Tests4, New_TE[4,d])
                elif vi <= -10 and vi > -21:
                    Tests = np.append(Tests, New_IntQ1B[3,d])
                    Tests1 = np.append(Tests1, New_CD[3,d])
                    Tests2 = np.append(Tests2, New_Temp[3,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[3,d])
                    Tests4 = np.append(Tests4, New_TE[3,d])
                elif vi <= -21 and vi > -33:
                    Tests = np.append(Tests, New_IntQ1B[2,d])
                    Tests1 = np.append(Tests1, New_CD[2,d])
                    Tests2 = np.append(Tests2, New_Temp[2,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[2,d])
                    Tests4 = np.append(Tests4, New_TE[2,d])
                elif vi <= -33 and vi > -48:
                    Tests = np.append(Tests, New_IntQ1B[1,d])
                    Tests1 = np.append(Tests1, New_CD[1,d])
                    Tests2 = np.append(Tests2, New_Temp[1,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[1,d])
                    Tests4 = np.append(Tests4, New_TE[1,d])
                elif vi <= -48 and vi >= -72:
                    Tests = np.append(Tests, New_IntQ1B[0,d])
                    Tests1 = np.append(Tests1, New_CD[0,d])
                    Tests2 = np.append(Tests2, New_Temp[0,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[0,d])
                    Tests4 = np.append(Tests4, New_TE[0,d])
            Test_1 = np.array(Tests)
            Test_CD = np.array(Tests1)
            Test_T = np.array(Tests2)
            Test_3 = np.array(Tests3)
            Test_E = np.array(Tests4)
        elif ii > 0 and ii <= 181:
            for iii in range(156):
                vi = 83 - iii     
                if vi == 83:
                    Tests = New_IntQ1B[10,d]
                    Tests1 = New_CD[10,d]
                    Tests2 = New_Temp[10,d]
                    Tests3 = New_IntQ3B[10,d]
                    Tests4 = New_TE[10,d]
                elif vi < 83 and vi > 58:
                    Tests = np.append(Tests, New_IntQ1B[10,d])
                    Tests1 = np.append(Tests1, New_CD[10,d])
                    Tests2 = np.append(Tests2, New_Temp[10,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[10,d])
                    Tests4 = np.append(Tests4, New_TE[10,d])
                elif vi <= 58 and vi > 44:
                    Tests = np.append(Tests, New_IntQ1B[9,d])
                    Tests1 = np.append(Tests1, New_CD[9,d])
                    Tests2 = np.append(Tests2, New_Temp[9,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[9,d])
                    Tests4 = np.append(Tests4, New_TE[9,d])
                elif vi <= 44 and vi > 31:
                    Tests = np.append(Tests, New_IntQ1B[8,d])
                    Tests1 = np.append(Tests1, New_CD[8,d])
                    Tests2 = np.append(Tests2, New_Temp[8,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[8,d])
                    Tests4 = np.append(Tests4, New_TE[8,d])
                elif vi <= 31 and vi > 21:
                    Tests = np.append(Tests, New_IntQ1B[7,d])
                    Tests1 = np.append(Tests1, New_CD[7,d])
                    Tests2 = np.append(Tests2, New_Temp[7,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[7,d])
                    Tests4 = np.append(Tests4, New_TE[7,d])
                elif vi <= 21 and vi > 10:
                    Tests = np.append(Tests, New_IntQ1B[6,d])
                    Tests1 = np.append(Tests1, New_CD[6,d])
                    Tests2 = np.append(Tests2, New_Temp[6,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[6,d])
                    Tests4 = np.append(Tests4, New_TE[6,d])
                elif vi <= 10 and vi > 0:
                    Tests = np.append(Tests, New_IntQ1B[5,d])
                    Tests1 = np.append(Tests1, New_CD[5,d])
                    Tests2 = np.append(Tests2, New_Temp[5,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[5,d])
                    Tests4 = np.append(Tests4, New_TE[5,d])
                elif vi <= 0 and vi > -10:
                    Tests = np.append(Tests, New_IntQ1B[4,d])
                    Tests1 = np.append(Tests1, New_CD[4,d])
                    Tests2 = np.append(Tests2, New_Temp[4,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[4,d])
                    Tests4 = np.append(Tests4, New_TE[4,d])
                elif vi <= -10 and vi > -21:
                    Tests = np.append(Tests, New_IntQ1B[3,d])
                    Tests1 = np.append(Tests1, New_CD[3,d])
                    Tests2 = np.append(Tests2, New_Temp[3,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[3,d])
                    Tests4 = np.append(Tests4, New_TE[3,d])
                elif vi <= -21 and vi > -33:
                    Tests = np.append(Tests, New_IntQ1B[2,d])
                    Tests1 = np.append(Tests1, New_CD[2,d])
                    Tests2 = np.append(Tests2, New_Temp[2,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[2,d])
                    Tests4 = np.append(Tests4, New_TE[2,d])
                elif vi <= -33 and vi > -48:
                    Tests = np.append(Tests, New_IntQ1B[1,d])
                    Tests1 = np.append(Tests1, New_CD[1,d])
                    Tests2 = np.append(Tests2, New_Temp[1,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[1,d])
                    Tests4 = np.append(Tests4, New_TE[1,d])
                elif vi <= -48 and vi >= -72:
                    Tests = np.append(Tests, New_IntQ1B[0,d])
                    Tests1 = np.append(Tests1, New_CD[0,d])
                    Tests2 = np.append(Tests2, New_Temp[0,d])
                    Tests3 = np.append(Tests3, New_IntQ3B[0,d])
                    Tests4 = np.append(Tests4, New_TE[0,d])
            Test_1 = np.hstack((Test_1, Tests))
            Test_CD = np.hstack((Test_CD, Tests1))
            Test_T = np.hstack((Test_T, Tests2))
            Test_3 = np.hstack((Test_3, Tests3))
            Test_E = np.hstack((Test_E, Tests4))
        else:
            pass
    Mapping_Q1 = np.reshape(Test_1, (181, 156))
    Mapping_Q1 = Mapping_Q1.transpose()
    Mapping_Q1 = np.flipud(Mapping_Q1)
    Blank = np.zeros((7, 181))
    Blank3 = np.zeros((18, 181))
    Mapping_Q1 = np.vstack((Blank, Mapping_Q1))
    Mapping_Q1 = np.vstack((Mapping_Q1, Blank3))
    
    Mapping_Q3 = np.reshape(Test_3, (181, 156))
    Mapping_Q3 = Mapping_Q3.transpose()
    Mapping_Q3 = np.flipud(Mapping_Q3)
    Mapping_Q3 = np.vstack((Blank, Mapping_Q3))
    Mapping_Q3 = np.vstack((Mapping_Q3, Blank3))
    
    Mapping_Temp = np.reshape(Test_T, (181, 156))
    Mapping_Temp = Mapping_Temp.transpose()
    Mapping_Temp = np.flipud(Mapping_Temp)
    Mapping_Temp = np.vstack((Blank, Mapping_Temp))
    Mapping_Temp = np.vstack((Mapping_Temp, Blank3))

    Mapping_CD = np.reshape(Test_CD, (181, 156))
    Mapping_CD = Mapping_CD.transpose()
    Mapping_CD = np.flipud(Mapping_CD)
    Mapping_CD = np.vstack((Blank, Mapping_CD))
    Mapping_CD = np.vstack((Mapping_CD, Blank3))
    
    Mapping_TE = np.reshape(Test_E, (181, 156))
    Mapping_TE = Mapping_TE.transpose()
    Mapping_TE = np.flipud(Mapping_TE)
    Mapping_TE = np.vstack((Blank, Mapping_TE))
    Mapping_TE = np.vstack((Mapping_TE, Blank3))

    FIN_SLITQ1 = Slit*Mapping_Q1*10e5
    FIN_SLITQ3 = Slit*Mapping_Q3*10e5
    FIN_SLITTemp = Slit*Mapping_Temp
    FIN_SLITCD = Slit*Mapping_CD
    FIN_SLITTE = Slit*Mapping_TE*10e5
# =============================================================================
#     plt.figure()
#     plt.imshow(FIN_SLITTemp, cmap='nipy_spectral')
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
    SLITSQ1.append(FIN_SLITQ1)
    SLITSQ3.append(FIN_SLITQ3)
    SLITSTemp.append(FIN_SLITTemp)
    SLITSCD.append(FIN_SLITCD)
    SLITSE.append(FIN_SLITTE)
    SLITShapes.append(Slit)

#%% Now we need to make two arrays (One that lets us know how many pixels intersect and the other to just keep adding the values together)
#First lets focus on the number

Slits_Mask = np.zeros((181,181))
FINAL_MAPQ1 = np.zeros((181,181))
FINAL_MAPQ3 = np.zeros((181,181))
FINAL_MAPT = np.zeros((181,181))
FINAL_MAPCD = np.zeros((181,181))
FINAL_MAPTE = np.zeros((181, 181))

for a in range(13):
    Slits_Mask = Slits_Mask + SLITShapes[a]
    FINAL_MAPQ1 = FINAL_MAPQ1 + SLITSQ1[a]
    FINAL_MAPQ3 = FINAL_MAPQ3 + SLITSQ3[a]
    FINAL_MAPT = FINAL_MAPT + SLITSTemp[a]
    FINAL_MAPCD = FINAL_MAPCD + SLITSCD[a]
    FINAL_MAPTE = FINAL_MAPTE + SLITSE[a]
    plt.imshow(FINAL_MAPTE)

#Slits_Mask[61:121, 94][Slits_Mask[61:121, 94] == 0] = 1
#Slits_Mask[Slits_Mask == 0] = 0
plt.figure()
plt.imshow(Slits_Mask)

#Now to add all FIN_SLITS together and divide it by Slits Mask
KECK_06_MAP_11 = (FINAL_MAPQ1)/Slits_Mask
KECK_06_MAP_11[KECK_06_MAP_11 == 0] = np.nan
#KECK_06_MAP_11[KECK_06_MAP_11 == np.nan] = 0

KECK_06_MAP_11_Q3 = (FINAL_MAPQ3)/Slits_Mask
KECK_06_MAP_11_Q3[KECK_06_MAP_11_Q3 == 0] = np.nan
#KECK_06_MAP_11_Q3[KECK_06_MAP_11_Q3 == np.nan] = 0

KECK_06_MAP_11_T = (FINAL_MAPT)/Slits_Mask
KECK_06_MAP_11_T[KECK_06_MAP_11_T == 0] = np.nan

KECK_06_MAP_11_CD = (FINAL_MAPCD)/Slits_Mask
KECK_06_MAP_11_CD[KECK_06_MAP_11_CD == 0] = np.nan

KECK_06_MAP_11_TE = (FINAL_MAPTE)/Slits_Mask
KECK_06_MAP_11_TE[KECK_06_MAP_11_TE == 0] = np.nan

#%%
plt.figure()
plt.imshow(KECK_06_MAP_11, cmap='nipy_spectral')
#plt.annotate('NO DATA', (70, 175), fontsize=35)
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(0.03)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(KECK_06_MAP_11_Q3, cmap='nipy_spectral')
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(0.05)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
cbar.ax.tick_params(labelsize=15)
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(3,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(KECK_06_MAP_11_T, cmap=cm.coolwarm)
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Temperature (K)' + u'\u00B1' + ' 28K', fontsize=20)
#plt.title(r'Thermal Temperatures of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(KECK_06_MAP_11_CD, cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density x10$^{16}$ ($m^{-2}$) ' + u'\u00B1' + ' 0.1444 x 10$^{16}$$m^{-2}$', fontsize=20)
cbar.ax.tick_params(labelsize=15)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(KECK_06_MAP_11_TE, cmap='cividis')
cbar = plt.colorbar()
cbar.set_label(r'Total $H_{3}^{+}$ Emission ($\mu$W$m^{-2}$sr$^{-1}$) +- 2.592 $\mu$W$m^{-2}$sr$^{-1}$', fontsize=17.5)
cbar.ax.tick_params(labelsize=15)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(0, 180) #0, 3601

#%%
