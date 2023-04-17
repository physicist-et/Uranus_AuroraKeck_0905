# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:17:50 2021

@author: snowy
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import csv
from matplotlib.patches import Ellipse
from KeckDatah3ppy_Unrough3v5 import New_IntQ1B, New_IntQ3B, New_CD, New_Temp, New_TE, New_IntQ1Err, New_IntQ3Err, New_TempErr, New_CDErr, New_TE_Err
#from KeckIntensityStep2a import Keck_DataABBA
from matplotlib import cm

#%%#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
uranus_seangleK = (5.075900 + 5.065686)/2
uranus_seangleI = (35.784010 + 35.773649)/2
#stretch yy to become a sphere
flattening =0.0229
uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
uranus_seangleI_Rads = (uranus_seangleI*np.pi)/180
losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
eq_po_ratioK=1-losflattening

y_Keck = np.linspace(-11.23168567912943, 11.23168567912943, 23) #Approximate point due to the slight pixel boundaries having a shorter edge due to the planet's curvature

y_Keckadj = y_Keck/eq_po_ratioK

losflattening=flattening*(1-np.sin((uranus_seangleI/180)*np.pi))
eq_po_ratioI=1-losflattening

y1_IRTF = -0.89263
y2_IRTF = 0.89263

y1_IRTFadj = y1_IRTF/eq_po_ratioI
y2_IRTFadj = y2_IRTF/eq_po_ratioI
# #%% First lets confirm the middle from a total of Q1
# with open('MiddlePointData.csv', 'r') as file: #This reads in the file from 
#     MidP = file.read().replace('\n', ' ')
# file.close()

# Middle_Points = np.fromstring(MidP, dtype=float, count=-1, sep= ' ')

# for a in range(13):
#     Example_Keck = Keck_DataABBA[a*2] + Keck_DataABBA[(a*2)+1] + Keck_DataABBA[(a*2)+2] + Keck_DataABBA[(a*2)+3]
#     fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
#     ax.imshow(Example_Keck, cmap='gist_gray')
#     EllsP = Ellipse((141.996, (Middle_Points[8*a]+Middle_Points[8*a+2]+Middle_Points[8*a+4]+Middle_Points[8*a+6])/4), 22.41004051808411, (22.41004051808411/eq_po_ratioK), angle=0, linewidth=1, fill=False)
#     EllsN = Ellipse((141.996, (Middle_Points[8*a+1]+Middle_Points[8*a+3]+Middle_Points[8*a+5]+Middle_Points[8*a+7])/4), 22.41004051808411, (22.41004051808411/eq_po_ratioK), angle=0, linewidth=1, color ='w', fill=False)
#     ax.add_artist(EllsP)
#     ax.add_artist(EllsN)

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
Extra = ((27/60)/17.24)*360
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck+Extra)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK1.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a < 46:
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
    if b < 1 and a > 0:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
    elif a == 0 or a == 22 or a == 23 or a == 45:
        if a > 22:
            d = a - 23
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[d]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[d]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        else:
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(np.round(Contents2_Keck))
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK1.append(Lat_Keck)
        b = 1
    elif b == 1 and a < 45:
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
        Long_Keck = 0.1457799347697654 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 0.1457799347697654 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (0.1457799347697654 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(46):
    if b < 1 and a > 0:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif a == 0 or a == 22 or a == 23 or a == 45:
        if a > 22:
            d = a - 23
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[d]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[d]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        else:
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(np.round(Contents2_Keck))
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a < 45:
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
Extra = ((27/60)/17.24)*360
#First lets sort Latitudes
for a in range(46):
    if b < 1 and a < 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 1.9741013903855542 - math.atan(Contents1_Keck)
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
    elif b == 0 and a == 22:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = 1.9741013903855542 - math.atan(Contents1_Keck)
        Long_Keck =(Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck+Extra)
        b = 1
    elif b == 1 and a >= 23:
        c = a - 23
        r_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[c]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
        Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[c]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
        Long_Keck = (1.9741013903855542 - math.atan(Contents1_Keck))
        Long_Keck = (Long_Keck*180)/np.pi
        LongitudeK.append(Long_Keck)

b = 0
LatitudeK = []

for a in range(46):
    if b < 1 and a > 0:
        r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
        pheta_Keck = math.asin(r_Keck/11.491436449930903)
        Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(Contents2_Keck)
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
    elif a == 0 or a == 22 or a == 23 or a == 45:
        if a > 22:
            d = a - 23
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[d]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[d]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        else:
            r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
            pheta_Keck = math.asin(r_Keck/11.491436449930903)
            Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
        Lat_Keck = math.asin(np.round(Contents2_Keck))
        Lat_Keck = (Lat_Keck*180)/np.pi
        LatitudeK.append(Lat_Keck)
        b = 1
    elif b == 1 and a < 45:
        c = a - 23
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
print(len(LatitudeK)) #Now we need to translate this over to the pixel marking

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
    losflattening=float("{0:.4f}".format(flattening*(1-np.sin(uranus_seangleK_Rads))))
    eq_po_ratioK=1-losflattening
    End_pix = eq_po_ratioK*np.sqrt((11.491436449930903**2)-(0.6824**2))
    y_Keck = np.linspace(-1*End_pix, End_pix, 23)
    y_Keckadj = y_Keck/eq_po_ratioK
    x1_Keck = -0.68240
    x2_Keck = 0.68240
    b = 0
    for a in range(46):
        if b < 1 and a > 0 and a < 22:
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
                # print(LatitudeK[a], LongitudeK[a])
            else:
                Long_Keck = (Longs[m] + 360 - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
                # print(LatitudeK[a], LongitudeK[a])
        elif a == 0 or a == 22 or a == 23 or a == 45:
             if a > 22:
                d = a - 23
                r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[d]**2)
                pheta_Keck = math.asin(r_Keck/11.491436449930903)
                Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[d]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
                Lat_Keck = math.asin(round(Contents2_Keck))
                Lat_Keck = (Lat_Keck*180)/np.pi
                LatitudeK.append(Lat_Keck)
                if a == 23:
                    Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
                else:
                    Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
                Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[d]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
                if Longs[m] > 300:
                   Long_Keck = (Longs[m] - Longs[0])
                   Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                   LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
                   # print(LatitudeK[a], LongitudeK[a])
                else:
                   Long_Keck = (Longs[m] + 360 - Longs[0])
                   Long_Keck = (Long_Keck*np.pi)/180  - math.atan(Contents1_Keck)
                   LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
                   # print(LatitudeK[a], LongitudeK[a])
             else:
                r_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[a]**2)
                pheta_Keck = math.asin(r_Keck/11.491436449930903)
                Contents2_Keck = (np.cos(pheta_Keck)*np.sin(uranus_seangleK_Rads))+((y_Keckadj[a]*np.sin(pheta_Keck)*np.cos(uranus_seangleK_Rads))/r_Keck)
                Lat_Keck = math.asin(round(Contents2_Keck))
                Lat_Keck = (Lat_Keck*180)/np.pi
                LatitudeK.append(Lat_Keck)
                if a == 0:
                    Contents1_Keck = (x1_Keck*np.sin(pheta_Keck))
                else:
                    Contents1_Keck = (x2_Keck*np.sin(pheta_Keck))
                Contents1_Keck = Contents1_Keck/((r_Keck*np.cos(pheta_Keck)*np.cos(uranus_seangleK_Rads))-(y_Keckadj[a]*np.sin(uranus_seangleK_Rads)*np.sin(pheta_Keck)))
                if Longs[m] > 300:
                    Long_Keck = (Longs[m] - Longs[0])
                    Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                    LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
                    # print(LatitudeK[a], LongitudeK[a])
                else:
                    Long_Keck = (Longs[m] + 360 - Longs[0])
                    Long_Keck = (Long_Keck*np.pi)/180  - math.atan(Contents1_Keck)
                    LongitudeK.append(((Long_Keck*180)/np.pi)+Extra)
                    # print(LatitudeK[a], LongitudeK[a])
             if a == 23:
                 b = 1
        elif b == 1 and a < 45:
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
                # print(LatitudeK[a], LongitudeK[a])
            else:
                Long_Keck = (Longs[m] + 360 - Longs[0])
                Long_Keck = (Long_Keck*np.pi)/180 - math.atan(Contents1_Keck)
                LongitudeK.append((Long_Keck*180)/np.pi)
                # print(LatitudeK[a], LongitudeK[a])
                
#%% Now to calculate 108 lines (Latitudes are all the same so same 2 lines repeated)
#So work out all 1 degree positions 
from PIL import Image, ImageDraw

# =============================================================================
# polygon = [(54.79195714973601, LatitudeK[0]+90), (0, LatitudeK[23]+90), (20.93325239054063, LatitudeK[1]+90), (33.858704759195376, LatitudeK[24]+90)]
# polygon2 = [(LongitudeK[1]+27.395244685792576, LatitudeK[1]+90), (LongitudeK[24]+27.395244685792576, LatitudeK[24]+90), (LongitudeK[25]+27.395244685792576, LatitudeK[2]+90), (LongitudeK[2]+27.395244685792576, LatitudeK[25]+90)]
# =============================================================================
width = 361
height = 181

img = Image.new('L', (width, height), 0)
for i in range(22):
    if i < 1:
        polygon = [(LongitudeK[i]-np.nanmin(LongitudeK), LatitudeK[i]+90), (LongitudeK[23+i]-np.nanmin(LongitudeK), LatitudeK[23+i]+90), (LongitudeK[24+i]-np.nanmin(LongitudeK), LatitudeK[24+i]+90), (LongitudeK[1+i]-np.nanmin(LongitudeK), LatitudeK[1+i]+90)]
        ImageDraw.Draw(img).polygon(polygon, outline=2, fill=2)  
    else:
        polygon = [(LongitudeK[i]-np.nanmin(LongitudeK), LatitudeK[i]+90), (LongitudeK[23+i]-np.nanmin(LongitudeK), LatitudeK[23+i]+90), (LongitudeK[24+i]-np.nanmin(LongitudeK), LatitudeK[24+i]+90), (LongitudeK[1+i]-np.nanmin(LongitudeK), LatitudeK[1+i]+90)]
        ImageDraw.Draw(img).polygon(polygon, outline=2, fill=2)
        
#ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
#ImageDraw.Draw(img).polygon(polygon2, outline=1, fill=1)
Slit0 = np.flipud(np.array(img))

plt.figure()
plt.imshow(Slit0) #Need to add the pixels to each other to get the right representation probably by saving each drawing? Or doing two polygons and saving them at a time?

SlitF = []
Pix = []

#Instead lets set up the 181, 360 strips seperately
for i in range(22):
    Fill_point = (math.floor(LatitudeK[i]) - math.floor(LatitudeK[i+1]))*-1
    Pix = np.ones((int(Fill_point),361))*(New_IntQ1B[i,0]+New_IntQ1B[i+1,0])
    if i == 0:
        Pix = np.ones((int(Fill_point+1),361))*(New_IntQ1B[i,0]+New_IntQ1B[i+1,0])
        SlitF = Pix
    else:
        SlitF = np.vstack((SlitF, Pix))
        
plt.figure()
plt.imshow(SlitF)

#So the final picture is 
plt.figure()
plt.imshow(Slit0*SlitF, cmap='nipy_spectral')
#%%
img2 = Image.new('L', (width, height), 0)
for i in range(22):
    ii = i + 46
    if i < 1:
        polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
        ImageDraw.Draw(img2).polygon(polygon, outline=2, fill=2)
    elif i < 21:
        polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
        ImageDraw.Draw(img2).polygon(polygon, outline=2, fill=2)        
    else:
        polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
        ImageDraw.Draw(img2).polygon(polygon, outline=2, fill=2)
        
#ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
#ImageDraw.Draw(img).polygon(polygon2, outline=1, fill=1)
Slit0 = np.flipud(np.array(img2))

plt.figure()
plt.imshow(Slit0)

SlitF = []

for i in range(22):
    ii = i + 46
    if i < 1:
        Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
        Pix_1 = np.ones((int(Fill_point+1),361))
        SlitF = Pix_1*(New_IntQ1B[i,1]+New_IntQ1B[i+1,1])  
    else:
        Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
        Pix = np.ones((int(Fill_point),361))*(New_IntQ1B[i-1,1]+New_IntQ1B[i,1])
        SlitF = np.vstack((SlitF, Pix))

plt.figure()
plt.imshow(SlitF)

plt.figure()
plt.imshow(Slit0*SlitF, cmap='nipy_spectral')

#%% Now we make a loop for just Q1 and Q1 Err maps
Slit_Shape = []
Slit_Values = []
Slit_Errors = []
Slit_Values3 = []
Slit_Errors3 = []
Slit_Temps = []
Slit_TempErrors = []
Slit_CDs = []
Slit_CDErrors = []
Slit_TE = [] #New_TempErr, New_CDErr
Slit_TE_Errors = []

for x in range(13):
    if x == 7 or x == 8:
        pass
    if x < 7 or x > 8:
        img = Image.new('L', (width, height), 0)
        img2 = Image.new('L', (width, height), 0)
        img3 = Image.new('L', (width, height), 0)    
        for i in range(22): #Here we then draw out the slit shape
            ii = i + 46*x
            if i < 1:
                polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
                ImageDraw.Draw(img2).polygon(polygon, outline=1, fill=1)
            elif i < 21:
                polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
                ImageDraw.Draw(img2).polygon(polygon, outline=1, fill=1)        
            else:
                polygon = [(LongitudeK[ii]-np.nanmin(LongitudeK), LatitudeK[ii]+90), (LongitudeK[23+ii]-np.nanmin(LongitudeK), LatitudeK[23+ii]+90), (LongitudeK[24+ii]-np.nanmin(LongitudeK), LatitudeK[24+ii]+90), (LongitudeK[1+ii]-np.nanmin(LongitudeK), LatitudeK[1+ii]+90)]
                ImageDraw.Draw(img2).polygon(polygon, outline=1, fill=1)
        Slit_Shape.append(np.flipud(img2))
        for i in range(22):
            ii = i + 46*x
            if i < 1:
                Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
                Pix_1 = np.ones((int(Fill_point+1),361))
                SlitF = np.ones((int(Fill_point+1),361))*((New_IntQ1B[i+1,x]+New_IntQ1B[i,x])/2)
                SlitFE = np.ones((int(Fill_point+1),361))*np.sqrt(New_IntQ1Err[i+1,x]**2 + New_IntQ1Err[i,x]**2)
                SlitF3 = np.ones((int(Fill_point+1),361))*((New_IntQ3B[i+1,x]+New_IntQ3B[i,x])/2)
                SlitFE3 = np.ones((int(Fill_point+1),361))*np.sqrt(New_IntQ3Err[i+1,x]**2 + New_IntQ3Err[i,x]**2)
                SlitT = np.ones((int(Fill_point+1),361))*((New_Temp[i+1,x]+New_Temp[i,x])/2)
                SlitTE = np.ones((int(Fill_point+1),361))*np.sqrt(New_TempErr[i+1,x]**2 + New_TempErr[i,x]**2)
                SlitCD = np.ones((int(Fill_point+1),361))*((New_CD[i+1,x]+New_CD[i,x])/2)
                SlitCDE = np.ones((int(Fill_point+1),361))*np.sqrt(New_CDErr[i+1,x]**2 + New_CDErr[i,x]**2)
                SlitTEm = np.ones((int(Fill_point+1),361))*((New_TE[i+1,x]+New_TE[i,x])/2)
                SlitTErr = np.ones((int(Fill_point+1), 361))*np.sqrt(New_TE_Err[i+1,x]**2 + New_TE_Err[i,x]**2)
            elif i < 19 or i == 20:
                Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
                Pix = np.ones((int(Fill_point),361))*((New_IntQ1B[i+1,x]+New_IntQ1B[i,x])/2)
                PixT = np.ones((int(Fill_point),361))*((New_Temp[i+1,x]+New_Temp[i,x])/2)
                PixF3 = np.ones((int(Fill_point),361))*((New_IntQ3B[i+1,x]+New_IntQ3B[i,x])/2)
                PixFE3 = np.ones((int(Fill_point),361))*np.sqrt(New_IntQ3Err[i+1,x]**2 + New_IntQ3Err[i,x]**2)
                PixCD = np.ones((int(Fill_point),361))*((New_CD[i+1,x]+New_CD[i,x])/2)
                PixTEm = np.ones((int(Fill_point), 361))*((New_TE[i+1,x]+New_TE[i,x])/2)
                Error = np.sqrt(New_IntQ1Err[i+1,x]**2 + New_IntQ1Err[i,x]**2)
                ErrorT = np.sqrt(New_TempErr[i+1,x]**2 + New_TempErr[i,x]**2)
                ErrorCD = np.sqrt(New_CDErr[i+1,x]**2 + New_CDErr[i,x]**2)
                ErrorTE = np.sqrt(New_TE_Err[i+1,x]**2 + New_TE_Err[i,x]**2)
                PixE = np.ones((int(Fill_point), 361))*Error
                PixTE = np.ones((int(Fill_point), 361))*ErrorT
                PixCDE = np.ones((int(Fill_point), 361))*ErrorCD
                PixTErr = np.ones((int(Fill_point), 361))*ErrorTE
                SlitF = np.vstack((SlitF, Pix))
                SlitF3 = np.vstack((SlitF3, PixF3))
                SlitT = np.vstack((SlitT, PixT))
                SlitCD = np.vstack((SlitCD, PixCD))
                SlitTEm = np.vstack((SlitTEm, PixTEm))
                SlitFE = np.vstack((SlitFE, PixE))
                SlitFE3 = np.vstack((SlitFE3, PixFE3))
                SlitTE = np.vstack((SlitTE, PixTE))
                SlitCDE = np.vstack((SlitCDE, PixCDE))
                SlitTErr = np.vstack((SlitTErr, PixTErr))
                # print(np.nanmean(SlitTE))
            elif i == 21:
                Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
                Pix = np.ones((int(Fill_point+1),361))*((New_IntQ1B[i+1,x]+New_IntQ1B[i,x])/2)
                PixF3 = np.ones((int(Fill_point+1),361))*((New_IntQ3B[i+1,x]+New_IntQ3B[i,x])/2)
                PixFE3 = np.ones((int(Fill_point+1),361))*np.sqrt(New_IntQ3Err[i+1,x]**2 + New_IntQ3Err[i,x]**2)
                PixT = np.ones((int(Fill_point+1),361))*((New_Temp[i+1,x]+New_Temp[i,x])/2)
                PixCD = np.ones((int(Fill_point+1),361))*((New_CD[i+1,x]+New_CD[i,x])/2)
                PixTEm = np.ones((int(Fill_point+1), 361))*((New_TE[i+1,x]+New_TE[i,x])/2)
                Error = np.sqrt(New_IntQ1Err[i+1,x]**2 + New_IntQ1Err[i,x]**2)
                ErrorT = np.sqrt(New_TempErr[i+1,x]**2 + New_TempErr[i,x]**2)
                ErrorCD = np.sqrt(New_CDErr[i+1,x]**2 + New_CDErr[i,x]**2)
                ErrorTE = np.sqrt(New_TE_Err[i+1,x]**2 + New_TE_Err[i,x]**2)
                PixE = np.ones((int(Fill_point+1), 361))*Error
                PixTE = np.ones((int(Fill_point+1), 361))*ErrorT
                PixCDE = np.ones((int(Fill_point+1), 361))*ErrorCD
                PixTErr = np.ones((int(Fill_point+1), 361))*ErrorTE
                SlitF = np.vstack((SlitF, Pix))
                SlitF3 = np.vstack((SlitF3, PixF3))
                SlitT = np.vstack((SlitT, PixT))
                SlitCD = np.vstack((SlitCD, PixCD))
                SlitTEm = np.vstack((SlitTEm, PixTEm))
                SlitFE = np.vstack((SlitFE, PixE))
                SlitFE3 = np.vstack((SlitFE3, PixFE3))
                SlitTE = np.vstack((SlitTE, PixTE))
                SlitCDE = np.vstack((SlitCDE, PixCDE))
                SlitTErr = np.vstack((SlitTErr, PixTErr))
                # print(np.nanmean(SlitTE))
            else:
                Fill_point = (math.floor(LatitudeK[ii]) - math.floor(LatitudeK[ii+1]))*-1
                Pix = np.ones((int(Fill_point-1),361))*((New_IntQ1B[i+1,x]+New_IntQ1B[i,x])/2)
                PixF3 = np.ones((int(Fill_point-1),361))*((New_IntQ3B[i+1,x]+New_IntQ3B[i,x])/2)
                PixFE3 = np.ones((int(Fill_point-1),361))*np.sqrt(New_IntQ3Err[i+1,x]**2 + New_IntQ3Err[i,x]**2)
                PixT = np.ones((int(Fill_point-1),361))*((New_Temp[i+1,x]+New_Temp[i,x])/2)
                PixCD = np.ones((int(Fill_point-1), 361))*((New_CD[i+1,x]+New_CD[i,x])/2)
                PixTEm = np.ones((int(Fill_point-1), 361))*((New_TE[i+1,x]+New_TE[i,x])/2)
                PixE = np.ones((int(Fill_point-1), 361))*np.sqrt(New_IntQ1Err[i+1,x]**2 + New_IntQ1Err[i,x]**2)
                PixTE = np.ones((int(Fill_point-1), 361))*np.sqrt(New_TempErr[i+1,x]**2 + New_TempErr[i,x]**2)
                PixCDE = np.ones((int(Fill_point-1), 361))*np.sqrt(New_CDErr[i+1,x]**2 + New_CDErr[i,x]**2)
                PixTErr = np.ones((int(Fill_point-1), 361))*np.sqrt(New_TE_Err[i+1,x]**2 + New_TE_Err[i,x]**2)
                SlitF = np.vstack((SlitF, Pix))
                SlitF3 = np.vstack((SlitF3, PixF3))
                SlitT = np.vstack((SlitT, PixT))
                SlitCD = np.vstack((SlitCD, PixCD))
                SlitTEm = np.vstack((SlitTEm, PixTEm))
                SlitFE = np.vstack((SlitFE, PixE))
                SlitFE3 = np.vstack((SlitFE3, PixFE3))
                SlitTE = np.vstack((SlitTE, PixTE))
                SlitCDE = np.vstack((SlitCDE, PixCDE))
                SlitTErr = np.vstack((SlitTErr, PixTErr))
                # print(np.nanmean(SlitTE))
        ResultSlit = (SlitF*np.flipud(img2))
        Result3Slit = (SlitF3*np.flipud(img2))
        TempSlit = (SlitT*np.flipud(img2))
        CDSlit = (SlitCD*np.flipud(img2))
        ErrorSlit = (SlitFE*np.flipud(img2))
        Error3Slit = (SlitFE3*np.flipud(img2))
        TempErrorSlit = (SlitTE*np.flipud(img2))
        CDErrorSlit = (SlitCDE*np.flipud(img2))
        TESlit = (SlitTEm*np.flipud(img2))
        TErrSlit = (SlitTErr*np.flipud(img2))
        ResultSlit = np.nan_to_num(ResultSlit)
        ResultSlit3 = np.nan_to_num(Result3Slit)
        TempSlit = np.nan_to_num(TempSlit)
        CDSlit = np.nan_to_num(CDSlit)
        TESlit = np.nan_to_num(TESlit)
        ErrorSlit = np.nan_to_num(ErrorSlit)
        Error3Slit = np.nan_to_num(Error3Slit)
        TempErrorSlit = np.nan_to_num(TempErrorSlit)
        CDErrorSlit = np.nan_to_num(CDErrorSlit)
        TEErrorSlit = np.nan_to_num(TErrSlit)
        Slit_Values.append(ResultSlit)
        Slit_Values3.append(Result3Slit)
        Slit_Errors.append(ErrorSlit)
        Slit_Errors3.append(Error3Slit)
        Slit_Temps.append(TempSlit)
        Slit_TempErrors.append(TempErrorSlit)
        Slit_CDs.append(CDSlit)
        Slit_CDErrors.append(CDErrorSlit)
        Slit_TE.append(TESlit)
        Slit_TE_Errors.append(TEErrorSlit)

Fin_Val = np.zeros((181, 361))
Fin_3_Val = np.zeros((181, 361))
Fin_3_Err = np.zeros((181, 361))
Fin_Slit_Shape = np.zeros((181, 361))
Fin_Err = np.zeros((181, 361))
Fin_Temp = np.zeros((181, 361))
Fin_Temp_Err = np.zeros((181, 361))
Fin_CD = np.zeros((181, 361))
Fin_CD_Err = np.zeros((181, 361))
Fin_TE = np.zeros((181, 361))
Fin_TE_Err = np.zeros((181, 361))
Slit_Shape_Ex = Slit_Shape[0] + Slit_Shape[1]

for x in range(11):
    Fin_Val += Slit_Values[x]
    Fin_3_Val += Slit_Values3[x]
    Fin_Temp += Slit_Temps[x]
    Fin_CD += Slit_CDs[x]
    Fin_TE += Slit_TE[x]
    Fin_Err += Slit_Errors[x]
    Fin_3_Err += Slit_Errors3[x]
    Fin_Temp_Err += Slit_TempErrors[x]
    Fin_CD_Err += Slit_CDErrors[x]
    Fin_Slit_Shape += Slit_Shape[x]
    Fin_TE_Err += Slit_TE_Errors[x]
    if x == 10:
        IntQ1_Map = Fin_Val/Fin_Slit_Shape
        IntQ3_Map = Fin_3_Val/Fin_Slit_Shape
        Temperature_Map = Fin_Temp/Fin_Slit_Shape
        CDs_Map = Fin_CD/Fin_Slit_Shape
        TEs_Map = Fin_TE/Fin_Slit_Shape
        Error_Map = Fin_Err/Fin_Slit_Shape
        Error_3Map = Fin_3_Err/Fin_Slit_Shape
        Temp_Error_Map = Fin_Temp_Err/Fin_Slit_Shape
        CD_Error_Map = Fin_CD_Err/Fin_Slit_Shape
        TE_Error_Map = Fin_TE_Err/Fin_Slit_Shape
        
plt.figure()
plt.imshow(Slit_Shape[0])
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
# #plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
# plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
# plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
# #plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
# plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
# plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
# plt.ylim(180, 0) #1801, -1
# plt.xlim(-0.5, 179.5) #0, 3601


#%% Now we need to make two arrays (One that lets us know how many pixels intersect and the other to just keep adding the values together) #Need to do the final steps here!!!!!
#First lets focus on the number

# #Now to add all FIN_SLITS together and divide it by Slits Mask
KECK_06_MAP_11 = IntQ1_Map
KECK_06_MAP_11[KECK_06_MAP_11 == 0] = np.nan

KECK_06_MAP_11_Q1E = Error_Map
KECK_06_MAP_11_Q1E[KECK_06_MAP_11_Q1E == 0] = np.nan


#%%
plt.figure()
plt.imshow(KECK_06_MAP_11*10**6, cmap='nipy_spectral')
# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(Error_Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

#Now we want to find the mean for the intensities and put a filter than anything 
Example_Mean = np.nanmean(IntQ1_Map)
Example_Error = np.nanmean(Error_Map**2)

Filter_Max = Example_Mean - np.sqrt(Example_Error)

np.save('Keck_Q1_Ints_Map.npy', KECK_06_MAP_11*10**6)
#So the new image would look like so
# KECK_06_MAP_11A = IntQ1_Map
# KECK_06_MAP_11A[IntQ1_Map <= Filter_Max] = np.nan

# plt.figure()
# plt.imshow(IntQ1_Map*10**6)
# # plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
# cbar = plt.colorbar()
# cbar.ax.tick_params(labelsize=15)
# cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(Error_Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
# #plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
# plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
# plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
# #plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
# #plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
# plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
# plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
# #plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
# plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
# plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
# plt.ylim(180, 0) #1801, -1
# plt.xlim(-0.5, 179.5) #0, 3601

# Error_Help_Map = Error_Map
# Filter = (IntQ1_Map > Filter_Max)
# Error_Help_Map = Error_Help_Map*(Filter*1)
# Error_Help_Map[Error_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(Error_Map*10**6, cmap='nipy_spectral')
# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Error of the Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601


#%% Now lets put the HST emissions in the same mapping

# First lets build up the signal here with each emission

HST_EM1 = [4]
HST_EM1 = np.concatenate((np.ones(23), HST_EM1))
HST_EM1 = np.concatenate((HST_EM1, np.ones(23)))
HST_EM1 = np.concatenate((np.zeros(70), HST_EM1))
HST_EM1 = np.concatenate((HST_EM1, np.zeros(64)))
HST_ES = np.ones(24)
HST_ES = np.concatenate((HST_ES, np.ones(23)))
HST_ES = np.concatenate((np.zeros(70), HST_ES))
HST_ES = np.concatenate((HST_ES, np.zeros(64)))
HST_ES = np.tile(HST_ES, (35, 1))
HST_EM1 = np.vstack((HST_ES, HST_EM1))
HST_EM1 = np.vstack((HST_EM1, HST_ES))
HST_EM1 = np.vstack((np.zeros((20, 181)), HST_EM1))
HST_EM1 = np.vstack((HST_EM1, np.zeros((90, 181))))

# plt.figure()
# plt.imshow(HST_EM1, cmap='gist_yarg')

HST_EM2 = [11]
HST_EM2 = np.concatenate((np.ones(5), HST_EM2))
HST_EM2 = np.concatenate((HST_EM2, np.ones(5)))
HST_EM2 = np.concatenate((np.zeros(44), HST_EM2))
HST_EM2 = np.concatenate((HST_EM2, np.zeros(126)))
HST_ES = np.ones(6)
HST_ES = np.concatenate((HST_ES, np.ones(5)))
HST_ES = np.concatenate((np.zeros(44), HST_ES))
HST_ES = np.concatenate((HST_ES, np.zeros(126)))
HST_ES = np.tile(HST_ES, (3, 1))
HST_EM2 = np.vstack((HST_ES, HST_EM2))
HST_EM2 = np.vstack((HST_EM2, HST_ES))
HST_EM2 = np.vstack((np.zeros((76, 181)), HST_EM2))
HST_EM2 = np.vstack((HST_EM2, np.zeros((98, 181))))

# plt.figure()
# plt.imshow(HST_EM2, cmap='gist_yarg')

HST_EM3 = [10]
HST_EM3 = np.concatenate((np.ones(3), HST_EM3))
HST_EM3 = np.concatenate((HST_EM3, np.ones(3)))
HST_EM3 = np.concatenate((np.zeros(52), HST_EM3))
HST_EM3 = np.concatenate((HST_EM3, np.zeros(122)))
HST_ES = np.ones(4)
HST_ES = np.concatenate((HST_ES, np.ones(3)))
HST_ES = np.concatenate((np.zeros(52), HST_ES))
HST_ES = np.concatenate((HST_ES, np.zeros(122)))
HST_ES = np.tile(HST_ES, (3, 1))
HST_EM3 = np.vstack((HST_ES, HST_EM3))
HST_EM3 = np.vstack((HST_EM3, HST_ES))
HST_EM3 = np.vstack((np.zeros((74, 181)), HST_EM3))
HST_EM3 = np.vstack((HST_EM3, np.zeros((100, 181))))

# plt.figure()
# plt.imshow(HST_EM3, cmap='gist_yarg')

Tot_EM = (HST_EM1 + HST_EM2 + HST_EM3)

plt.figure()
plt.imshow(Tot_EM, cmap='gist_yarg')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Error of the Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

#%% Lets include one for Q3 as well

KECK_06_MAP_113 = IntQ3_Map
KECK_06_MAP_113[KECK_06_MAP_113 == 0] = np.nan

KECK_06_MAP_11_Q3E = Error_3Map
KECK_06_MAP_11_Q3E[KECK_06_MAP_11_Q3E == 0] = np.nan

plt.figure()
plt.imshow(KECK_06_MAP_113*10**6, cmap='nipy_spectral')
# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(Error_3Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(Error_3Map*10**6, cmap='nipy_spectral')
# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Error of the Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601


#%% Now we draw out the Temperature and Error Maps

plt.figure()
plt.imshow(Temperature_Map, cmap=cm.coolwarm)
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Temperature (K)' + u'\u00B1' + ' ' + str(round(np.nanmean(Temp_Error_Map))) + 'K', fontsize=20)
#plt.title(r'Thermal Temperatures of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(Temp_Error_Map, cmap=cm.coolwarm)
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=25)
cbar.set_label(r'Temperature Error (K)', fontsize=20)
#plt.title(r'Thermal Temperatures of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(CDs_Map/(10**16), cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density x10$^{16}$ ($m^{-2}$) ' + u'\u00B1' + str("{:.2f}".format(np.nanmean(CD_Error_Map)/10**16)) + ' x 10$^{16}$$m^{-2}$', fontsize=20)
cbar.ax.tick_params(labelsize=25)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

print(np.nanmean(CDs_Map/(10**16)))
print(np.nanstd(CDs_Map/10**16))

plt.figure()
plt.imshow(CD_Error_Map/(10**16), cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density Error x10$^{16}$ ($m^{-2}$) ', fontsize=20)
cbar.ax.tick_params(labelsize=25)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

plt.figure()
plt.imshow(TEs_Map*(10**6), cmap='rainbow')
cbar = plt.colorbar()
cbar.set_label(r'Total Emission (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(TE_Error_Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20)
cbar.ax.tick_params(labelsize=25)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
#plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
#plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 

plt.figure()
plt.imshow(TE_Error_Map*(10**6), cmap='rainbow')
cbar = plt.colorbar()
cbar.set_label(r'Errors of Total Emission from Emission lines (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20)
cbar.ax.tick_params(labelsize=25)
#plt.title(r'Column Density of $H_{3}^{+}$ from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 22.5)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 30), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=25)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=25)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 

#%% Here are all the cropped versions

# KECK_06_MAP_11A = IntQ1_Map
# KECK_06_MAP_11A[IntQ1_Map <= Filter_Max] = np.nan

KECK_06_MAP_11A = np.nan_to_num(IntQ1_Map - Error_Map)
Filter = np.nanmean(IntQ1_Map) + np.nanstd(IntQ1_Map)
Filter2 = np.nanmean(IntQ1_Map)
FilteredInts = (KECK_06_MAP_11A > Filter2)*1*KECK_06_MAP_11A 
FilteredInts = (FilteredInts < Filter)*1*FilteredInts
FilteredInts[FilteredInts == 0] = np.nan

plt.figure()
plt.imshow(FilteredInts*10**6, cmap = 'nipy_spectral')

# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(Error_Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
#plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$ Emission Lines from Uranus on the $5^{th}$ September 2006', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=25, labelpad=15)
plt.ylabel('Latitude across Uranus (ULS) ($^\circ$)', fontsize=25, labelpad=15)
#plt.xticks(np.arange(0, 181, 20), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=15)
#plt.xticks(np.arange(0, 361, 20), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(-0.5, 180, 30), ['0$^\circ$', '30$^\circ$', '60$^\circ$', '90$^\circ$', '120$^\circ$', '150$^\circ$', '180$^\circ$'], fontsize=15)
plt.yticks(np.arange(0, 181, 30), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=15)
# #plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
# plt.vlines((-0.5, 29.5, 59.5, 89.5, 119.5, 149.5, 179.5), -0.5, 179.5, colors = 'k', linestyles = 'dotted', alpha = 0.75)
# plt.hlines((0, 30, 60, 90, 120, 150, 180), 0, 180, colors = 'k', linestyles = 'dotted', alpha = 0.75)
plt.ylim(180, 0) #1801, -1
plt.xlim(-0.5, 179.5) #0, 3601

np.save('FilteredQ1Aurora.npy', FilteredInts)

#%%
Error_Help_Map = Error_Map
#Filter = (IntQ1_Map < Filter_Max)
Error_Help_Map = Error_Help_Map*(((KECK_06_MAP_11A > Filter)*1)-1)*-1
Error_Help_Map[Error_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(Error_Help_Map*10**6, cmap='nipy_spectral')
# plt.imshow(KECK_06_MAP_11*10**6, cmap='gist_heat')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Error of the Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20) 
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

N = np.count_nonzero(np.nan_to_num(FilteredInts))
Sigma_vals = []
for x in range(361):
    Img = np.nan_to_num(Error_Help_Map[:,x])
    for y in  range(181):
         Sigma_vals.append(Img[y]**2)

Sigma_Av = np.sqrt(np.sum(Sigma_vals))/np.sqrt(N)
print(Sigma_Av*10**6)

#%%

Temp_Help_Map = Temperature_Map #- Temp_Error_Map
FilterTMax = np.nanmean(Temperature_Map) + np.nanmean(Temp_Error_Map)
FilterTMin = np.nanmean(Temperature_Map) - np.nanmean(Temp_Error_Map)
FilterTMax = (Temperature_Map > FilterTMax)
FilterTMin = (Temperature_Map < FilterTMin)
FilterT = (((FilterTMax*1)+(FilterTMin*1))-1)*-1
Filter = np.nanmean(IntQ1_Map) #+ np.nanstd(IntQ1_Map)
Filter2 = np.nanmean(IntQ1_Map) + np.nanstd(IntQ1_Map)
# Filter2 = np.nanmean(IntQ1_Map)
#Temp_Help_Map = ((IntQ1_Map > Filter)*1)*Temperature_Map
# Temp_Help_Map = (((KECK_06_MAP_11A > Filter2)*1))*(Temperature_Map) # - Temp_Error_Map)
Temp_Help_Map = (((KECK_06_MAP_11A < Filter2)*1))*(Temp_Help_Map) 
Temp_Help_Map = (((KECK_06_MAP_11A > Filter)*1))*(Temp_Help_Map)
#Temp_Help_Map = Temp_Help_Map*(FilterT)
Temp_Help_Map[Temp_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(Temp_Help_Map, cmap=cm.coolwarm)
#plt.imshow(Temp_Help_Map, cmap='gist_gray')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Temperature (K)' + u'\u00B1' + ' ' + str(round(np.nanmean(Temp_Error_Map))) + 'K', fontsize=20)
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

#%%

Temp_Help_Map = Temp_Error_Map
Temp_Help_Map = Temp_Help_Map*(FilterT)
Temp_Help_Map[Temp_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(Temp_Help_Map, cmap=cm.coolwarm)
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Temperature Error (K)', fontsize=20)
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

#%%
CD_Help_Map = CDs_Map - CD_Error_Map
FilterCDMax = np.nanmean(CDs_Map) - np.sqrt(np.nanmean(CD_Error_Map**2))
FilterCDMax = (CDs_Map > FilterCDMax)
Filter = (FilterCDMax)*1
Filter = np.nanmean(IntQ1_Map) + np.nanstd(IntQ1_Map)
Filter2 = np.nanmean(IntQ1_Map) 
CD_Help_Map = (KECK_06_MAP_11A > Filter2)*1*(CDs_Map - CD_Error_Map)
CD_Help_Map = (KECK_06_MAP_11A < Filter)*1*(CD_Help_Map)
#CD_Help_Map = (((IntQ1_Map > Filter)*1)-1)*-1*(CDs_Map)
CD_Help_Map[CD_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(CD_Help_Map/(10**16), cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density x10$^{16}$ ($m^{-2}$) ' + u'\u00B1' + str("{:.2f}".format(np.nanmean(CD_Error_Map)/10**16)) + ' x 10$^{16}$$m^{-2}$', fontsize=20)
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

#%%
CD_Help_Map = CD_Error_Map
CD_Help_Map = CD_Help_Map*(Filter*1)
CD_Help_Map[CD_Help_Map == 0] = np.nan

plt.figure()
plt.imshow(CD_Help_Map/(10**16), cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density Error x10$^{16}$ ($m^{-2}$) ', fontsize=20)
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

CD_test = (CDs_Map - CD_Error_Map) > np.nanmean(CDs_Map) + np.sqrt(np.nanmean(CD_Error_Map**2))
CD_test = (CD_test*1)*CDs_Map

plt.figure()
plt.imshow(CD_test/(10**16), cmap='RdPu')
cbar = plt.colorbar()
cbar.set_label(r'Column Density Left 10$^{16}$ ($m^{-2}$) ', fontsize=20)
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

#%%
TEm_Help_Map = TEs_Map - TE_Error_Map
#FilterTEMax = np.nanmean(TEs_Map) + np.nanstd(TEs(TE_Error_Map)
Filter = np.nanmean(IntQ1_Map) + np.nanstd(IntQ1_Map)
Filter2 = np.nanmean(IntQ1_Map)
FilteredTEMax = (KECK_06_MAP_11A > Filter2)*TEm_Help_Map
FilteredTEMax = (KECK_06_MAP_11A < Filter)*FilteredTEMax
#FilterTEMax = (TEs_Map > FilterTEMax)
TEm_Help_Map = FilteredTEMax
TEm_Help_Map[TEm_Help_Map == 0] = np.nan

plt.figure()
#plt.imshow((TEs_Map - TE_Error_Map)*(10**6))
plt.imshow(TEm_Help_Map*(10**6), cmap='gist_heat')
cbar = plt.colorbar()
cbar.set_label(r'Total Emission from Emission lines x10$^{6}$ (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ', fontsize=20)
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
plt.xlim(-0.5, 179.5) #0, 

#%%
from skimage import io
import skimage.color
import skimage.filters
# If we make a 180 by 360 transparent with stripes array?
CD_Help_Map = CDs_Map
FilterCDMax = np.nanmean(CDs_Map) + np.nanmean(CD_Error_Map)
FilterCDMax = (CDs_Map < FilterCDMax)
Filter = (FilterCDMax)*1
CD_Help_Map = CD_Help_Map*(Filter-1)
#Filter_Fill = (Filter-1)*-1

import matplotlib as mpl 

mpl.rcParams['hatch.linewidth'] = 3.0

fig, ax = plt.subplots(frameon=False)
fig.subplots_adjust(0, 0, 1, 1)
Background = ax.add_patch(plt.Polygon([(0,0), (0, 361), (181, 361), (181, 0), (0,0)], fill=False, hatch='/'))
ax.axis('off')
#plt.savefig("Hatch.png", dpi = 1000)

# Hatching = skimage.io.imread('Hatch.png')[:,:,:3]
# gray_image = skimage.color.rgb2gray(Hatching)
plt.figure()
plt.imshow(Filter, cmap='gist_gray')
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(np.nanmean(Error_Map)*10**6)) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=20) 
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

#%% Max, Min and Average + Errors of Q1 calculations Area 1 = 60:100, 10:65 | Area 2 = 0:145, 100:165

print('Area 1 Int Mean = ' + str("{:.3f}".format(np.nanmean(KECK_06_MAP_11A[60:170,10:65])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[60:170,10:65])*10**6)))
print('Area 1 Int Max = ' + str("{:.3f}".format(np.nanmax(KECK_06_MAP_11A[60:170,10:65])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[60:170,10:65])*10**6)))
print('Area 1 Int Min = ' + str("{:.3f}".format(np.nanmin(KECK_06_MAP_11A[60:170,10:65])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[60:170,10:65])*10**6)))

print('Area 2 Int Mean = ' + str("{:.3f}".format(np.nanmean(KECK_06_MAP_11A[0:145,100:165])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[0:145,100:165])*10**6)))
print('Area 2 Int Max = ' + str("{:.3f}".format(np.nanmax(KECK_06_MAP_11A[0:145,100:165])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[0:145,100:165])*10**6)))
print('Area 2 Int Min = ' + str("{:.3f}".format(np.nanmin(KECK_06_MAP_11A[0:145,100:165])*10**6)) + ' with an error of ' + str("{:.3f}".format(np.nanstd(KECK_06_MAP_11A[0:145,100:165])*10**6)))

# Keck_Test = np.nan_to_num(KECK_06_MAP_11A)
# Test = Error_Help_Map[60:170,10:65]
# Test2 = Test = Error_Help_Map[0:145,100:165]
# ErrorMax1 = np.unravel_index(np.argmax(Keck_Test[60:170,10:65]), Test.shape)
# ErrorMax2 = np.unravel_index(np.argmax(Keck_Test[0:145,100:165]), Test2.shape)
# ErrorMin1 = np.unravel_index(np.argmin(Keck_Test[60:170,10:65]), Test.shape)
# ErrorMin2 = np.unravel_index(np.argmin(Keck_Test[0:145,100:165]), Test2.shape)

# print('Area 1 Int Max = ' + str("{:.3f}".format(np.nanmax(KECK_06_MAP_11A[60:170,10:65])*10**6)) + ' with an error of ' + str("{:.3f}".format(Test[ErrorMax1])))
# print('Area 1 Int Min = ' + str("{:.3f}".format(np.nanmin(KECK_06_MAP_11A[60:170,10:65])*10**6)) + ' with an error of ' + str("{:.3f}".format(Test[ErrorMin1])))
# print('Area 2 Int Max = ' + str("{:.3f}".format(np.nanmax(KECK_06_MAP_11A[0:145,100:165])*10**6)) + ' with an error of ' + str("{:.3f}".format(Test2[ErrorMax2])))
# print('Area 2 Int Min = ' + str("{:.3f}".format(np.nanmin(KECK_06_MAP_11A[0:145,100:165])*10**6)) + ' with an error of ' + str("{:.3f}".format(Test2[ErrorMin2])))


#%%Now we use the filter from Keck_06_MAP_11A
CD_Filter = Temperature_Map
Temp_Int_Filter = IntQ1_Map > 0
Temperature_Filter = Temperature_Map*Temp_Int_Filter
Temperature_Filter[Temperature_Filter == 0] = np.nan

plt.figure()
plt.imshow(Temperature_Filter, cmap='coolwarm')
print('Area 1 Temp Mean = ' + str("{:.3f}".format(np.nanmean(Temperature_Filter[60:170,10:65]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[60:170,10:65]))))
print('Area 1 Temp Max = ' + str("{:.3f}".format(np.nanmax(Temperature_Filter[60:170,10:65]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[60:170,10:65]))))
print('Area 1 Temp Min = ' + str("{:.3f}".format(np.nanmin(Temperature_Filter[60:170,10:65]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[60:170,10:65]))))

print('Area 2 Temp Mean = ' + str("{:.3f}".format(np.nanmean(Temperature_Filter[0:145,100:165]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[0:145,100:165]))))
print('Area 2 Temp Max = ' + str("{:.3f}".format(np.nanmax(Temperature_Filter[0:145,100:165]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[0:145,100:165]))))
print('Area 2 Temp Min = ' + str("{:.3f}".format(np.nanmin(Temperature_Filter[0:145,100:165]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(Temperature_Filter[0:145,100:165]))))

#%% 
CD_Filter = CDs_Map
CD_Int_Filter = IntQ1_Map > 0
CD_Filter = CD_Filter*CD_Int_Filter
CD_Filter[CD_Filter == 0] = np.nan

plt.figure()
plt.imshow(CD_Filter, cmap='RdPu')
print('Area 1 CD Mean = ' + str("{:.3f}".format(np.nanmean(CD_Filter[60:170,10:65]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[60:170,10:65]/10**15))))
print('Area 1 CD Max = ' + str("{:.3f}".format(np.nanmax(CD_Filter[60:170,10:65]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[60:170,10:65]/10**15))))
print('Area 1 CD Min = ' + str("{:.3f}".format(np.nanmin(CD_Filter[60:170,10:65]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[60:170,10:65]/10**15))))

print('Area 2 CD Mean = ' + str("{:.3f}".format(np.nanmean(CD_Filter[0:145,100:165]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[0:145,100:165]/10**15))))
print('Area 2 CD Max = ' + str("{:.3f}".format(np.nanmax(CD_Filter[0:145,100:165]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[0:145,100:165]/10**15))))
print('Area 2 CD Min = ' + str("{:.3f}".format(np.nanmin(CD_Filter[0:145,100:165]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(CD_Filter[0:145,100:165]/10**15))))

#%%
TE_Filter = TEs_Map
TE_Int_Filter = IntQ1_Map > 0
TE_Filter = TE_Filter*TE_Int_Filter
TE_Filter[TE_Filter == 0] = np.nan

plt.figure()
plt.imshow(TE_Filter, cmap='RdPu')
print('Area 1 TE Mean = ' + str("{:.3f}".format(np.nanmean(TE_Filter[60:170,10:65]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[60:170,10:65]*10**6))))
print('Area 1 TE Max = ' + str("{:.3f}".format(np.nanmax(TE_Filter[60:170,10:65]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[60:170,10:65]*10**6))))
print('Area 1 TE Min = ' + str("{:.3f}".format(np.nanmin(TE_Filter[60:170,10:65]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[60:170,10:65]*10**6))))

print('Area 2 TE Mean = ' + str("{:.3f}".format(np.nanmean(TE_Filter[0:145,100:165]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[0:145,100:165]*10**6))))
print('Area 2 TE Max = ' + str("{:.3f}".format(np.nanmax(TE_Filter[0:145,100:165]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[0:145,100:165]*10**6))))
print('Area 2 TE Min = ' + str("{:.3f}".format(np.nanmin(TE_Filter[0:145,100:165]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(TE_Filter[0:145,100:165]*10**6))))

#%% All filters applied (except TE cause errors too large)
FilterInt = (IntQ1_Map > 0)*1
FilterT = (((FilterTMax*1)+(FilterTMin*1))-1)*-1
FilterCD = (FilterCDMax)*1

UltimateFilter = FilterInt*FilterT*FilterCD

# plt.figure()
# plt.imshow(UltimateFilter, cmap='gist_gray')

FilteredAurora = UltimateFilter*IntQ1_Map
FilteredAurora[FilteredAurora == 0] = np.nan

#IntsQ1
print('Arc Int Mean = ' + str("{:.3f}".format(np.nanmean(FilteredAurora[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora[0:115,100:155]*10**6))))
print('Arc Int Max = ' + str("{:.3f}".format(np.nanmax(FilteredAurora[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora[0:115,100:155]*10**6))))
print('Arc Int Min = ' + str("{:.3f}".format(np.nanmin(FilteredAurora[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora[0:115,100:155]*10**6))))


FilteredAurora = (UltimateFilter-1)*-1*(Fin_Val/Fin_Slit_Shape)
FilteredAurora[FilteredAurora == 0] =  np.nan

# plt.figure()
# plt.imshow(FilteredAurora, cmap='gist_gray')

# plt.figure()
# plt.imshow(FilteredAurora)

#Whole Area
print('Outside Arc Int Mean = ' + str("{:.3f}".format(np.nanmean(FilteredAurora*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora*10**6))))
print('Outside Arc Int Max = ' + str("{:.3f}".format(np.nanmax(FilteredAurora*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora*10**6))))
print('Outside Arc Int Min = ' + str("{:.3f}".format(np.nanmin(FilteredAurora*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredAurora*10**6))))

#Temps
FilteredTemps = UltimateFilter*Temperature_Map
FilteredTemps[FilteredTemps == 0] = np.nan


print('Arc Temp Mean = ' + str("{:.3f}".format(np.nanmean(FilteredTemps[0:115,100:155]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps[0:115,100:155]))))
print('Arc Temp Max = ' + str("{:.3f}".format(np.nanmax(FilteredTemps[0:115,100:155]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps[0:115,100:155]))))
print('Arc Temp Min = ' + str("{:.3f}".format(np.nanmin(FilteredTemps[0:115,100:155]))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps[0:115,100:155]))))

FilteredTemps = (UltimateFilter-1)*-1*Temperature_Map
FilteredTemps[FilteredTemps == 0] = np.nan

#Whole Area
print('Outside Arc Temp Mean = ' + str("{:.3f}".format(np.nanmean(FilteredTemps))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps))))
print('Outside Arc Temp Max = ' + str("{:.3f}".format(np.nanmax(FilteredTemps))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps))))
print('Outside Arc Temp Min = ' + str("{:.3f}".format(np.nanmin(FilteredTemps))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTemps))))

#CDs

FilteredCDs = UltimateFilter*CDs_Map
FilteredCDs[FilteredCDs == 0] = np.nan

print('Arc CD Mean = ' + str("{:.3f}".format(np.nanmean(FilteredCDs[0:115,100:155]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs[0:115,100:155]/10**15))))
print('Arc CD Max = ' + str("{:.3f}".format(np.nanmax(FilteredCDs[0:115,100:155]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs[0:115,100:155]/10**15))))
print('Arc CD Min = ' + str("{:.3f}".format(np.nanmin(FilteredCDs[0:115,100:155]/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs[0:115,100:155]/10**15))))

FilteredCDs = (UltimateFilter-1)*-1*CDs_Map
FilteredCDs[FilteredCDs == 0] = np.nan

#Whole Area
print('Outside Arc CD Mean = ' + str("{:.3f}".format(np.nanmean(FilteredCDs/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs/10**15))))
print('Outside Arc CD Max = ' + str("{:.3f}".format(np.nanmax(FilteredCDs/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs/10**15))))
print('Outside Arc CD Min = ' + str("{:.3f}".format(np.nanmin(FilteredCDs/10**15))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredCDs/10**15))))

FilteredTE = UltimateFilter*TEs_Map
FilteredTE[FilteredTE == 0] = np.nan

plt.figure()
plt.imshow(FilteredTE, cmap='gist_heat')

print('Arc TE Mean = ' + str("{:.3f}".format(np.nanmean(FilteredTE[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE[0:115,100:155]*10**6))))
print('Arc TE Max = ' + str("{:.3f}".format(np.nanmax(FilteredTE[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE[0:115,100:155]*10**6))))
print('Arc TE Min = ' + str("{:.3f}".format(np.nanmin(FilteredTE[0:115,100:155]*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE[0:115,100:155]*10**6))))

FilteredTE = (UltimateFilter-1)*-1*TEs_Map
FilteredTE[FilteredTE == 0] = np.nan

print('Outside Arc TE Mean = ' + str("{:.3f}".format(np.nanmean(FilteredTE*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE*10**6))))
print('Outside Arc TE Max = ' + str("{:.3f}".format(np.nanmax(FilteredTE*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE*10**6))))
print('Outside Arc TE Min = ' + str("{:.3f}".format(np.nanmin(FilteredTE*10**6))) + ' with an error of ' + str("{:.3f}".format(np.nanstd(FilteredTE*10**6))))

