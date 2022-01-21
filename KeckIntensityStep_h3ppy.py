# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:17:19 2020

@author: Emma 'Amelia'
"""
import matplotlib.pyplot as plt
import numpy as np
import h3ppy
from matplotlib import cm
import math
from matplotlib.colors import ListedColormap
#from LOSPractice import LOSc_array
from KeckIntensityStep2a import Keck_DataABBA
from KeckDataReductionStep1 import Fc_HD215

#%%
#Now we pull the new Data Points and duplicate what happened in KeckDatah3ppy
with open('MiddlePointData.csv', 'r') as file: #This reads in the file from 
    MidP = file.read().replace('\n', ' ')
file.close()

Middle_Points = np.fromstring(MidP, dtype=float, count=-1, sep= ' ')
Mid_Points = np.rint(Middle_Points)

Start_Points = []
Finish_Points = []

for m in range(int(len(Mid_Points)/2)):
    MidsP1P = Mid_Points[2*m] - 11
    MidsP1N = Mid_Points[2*m] + 11
    MidsP2P = Mid_Points[2*m + 1] - 11
    MidsP2N = Mid_Points[2*m + 1] + 11
    Start_Points.append(MidsP1P)
    Start_Points.append(MidsP2P)
    Finish_Points.append(MidsP1N)
    Finish_Points.append(MidsP2N)
    
#%% First produce data where the Positive and Negative emission have been matched up
# This is completed by carrying out Step 4 but over a larger width for the Gaussian fitting
    
w1 = 0
w2 = 1024
i = 0
ABBAalpha = []

for xx in range(54):
    ABBA = Keck_DataABBA[xx]*Fc_HD215*((4.2545*(10**10))/(0.288*0.1725))
    ABBAN = ABBA[int(Start_Points[i]):int(Finish_Points[i]), w1:w2] 
    ABBAN = ABBAN
    ABBAP = ABBA[int(Start_Points[i+1]):int(Finish_Points[i+1]), w1:w2] 
    ABBAT = ABBAN-ABBAP
    ABBAalpha.append(ABBAT/2)
    i += 2

#%%Assuming everything has gone to plan we can then put in the rest of the results and see what we get out at the end
# Create the h3ppy object feed data into it
    
h3p = h3ppy.h3p()
wave = h3p.wavegen(3.94466192, 4.00463162, 1024)
Q1Ints = []
Q3Ints = []
Q1Max = []
Q3Max = []
Temps = []
T_err = []
Col_Densities = []
Col_err = []
T_emission = []
Tot_EM_Err = []
c = 0

for xx in range(13):
    ABBAi = (ABBAalpha[xx*4] + ABBAalpha[(xx*4)+1] + ABBAalpha[(xx*4)+2] + ABBAalpha[(xx*4)+3])/4
    for i in range(11):
            ABBAt = (ABBAi[(i*2),:] + ABBAi[(i*2)+1,:])/2
            h3p.set(nbackground = 1, wavelength = wave, data = ABBAt, R = 20000, temperature = 576)
            # Guess the density
            h3p.guess_density(verbose=False)
            # By generating a model at this point we can compare our initial guess to the data
            guess = h3p.model()
            # First let's just fit the background
            h3p.set(nbackground = 1)
            ptf = ['background_0']
            fit = h3p.fit(params_to_fit = ptf)
            Vars, errs = h3p.get_results(verbose=False)
            # Only fit a linear fit as the emission background is level and a quadratic for offset  
            # Remember, the variables are stored in the h3p object so it'll remember the results 
            # of the last fit
            h3p.set(noffset = 2)
            ptf = ['offset_0', 'offset_1']
            fit2 = h3p.fit(params_to_fit = ptf, verbose = False)
            Vars, errs = h3p.get_results(verbose=False)
            # Then let's fit the temperature, density and line-width
            ptf = ['temperature', 'density', 'sigma_0']
            fit3 = h3p.fit(params_to_fit = ptf)
            Vars, errs = h3p.get_results(verbose = False)
            # plt.figure()
            # plt.plot(wave[0:300], ABBAt[0:300])
            # plt.plot(wave[0:300], fit3[0:300])
            if Vars == False:
                A2 = Vars['sigma_0']
                # print(A2)
                FWHM = A2*2*np.sqrt(2*math.log(2))
                Q1Ints.append(np.nanmax(fit3)*1000000*FWHM)
                Q1Max.append(np.nanmax(fit3))
                Q3Ints.append(np.nanmax(fit3[400:1024])*1000000*FWHM)
                Q3Max.append(np.nanmax(fit3[400:1024]))
                Temps.append(0)
                T_err.append(0)
                Col_Densities.append(0)
                Col_err.append(0)
            else:
                A2 = Vars['sigma_0']
                # print(A2)
                FWHM = A2*2*np.sqrt(2*math.log(2))
                Q1Ints.append(np.nanmax(fit3)*1000000*FWHM)
                Q1Max.append(np.nanmax(fit3))
                Q3Ints.append(np.nanmax(fit3[400:1024])*1000000*FWHM)
                Q3Max.append(np.nanmax(fit3[400:1024]))
                Temps.append(Vars['temperature'])
                T_err.append(errs['temperature'])
                Col_Densities.append(Vars['density'])
                Col_err.append(errs['density'])

#To make life easier, we then calculate the total emission seperately

for c in range(143):
    if Temps[c] == 0:
        T_emission.append(0)
        Tot_EM_Err.append(0)
    else:
        EMission = h3p.total_emission(temperature = Temps[c], density = Col_Densities[c])
        T_emission.append(EMission)
        T_EM_err = np.sqrt((T_err[c]/Temps[c])**2 + ((np.sqrt(2)*T_err[c])/Temps[c])**2 + ((np.sqrt(3)*T_err[c])/Temps[c])**2 + ((np.sqrt(4)*T_err[c])/Temps[c])**2)
        T_EM_err = (T_emission[c]/Col_Densities[c])*np.sqrt((T_EM_err)**2 + (Col_err[c]/Col_Densities[c])**2)
        Total_EM_err = T_emission[c]*np.sqrt(((T_EM_err*Col_Densities[c])/T_emission[c])**2 + (Col_err[c]/Col_Densities[c])**2)
        Tot_EM_Err.append(Total_EM_err)
        
print(np.nanmean(Q1Ints))
print(np.nanmean(Q3Ints))
print(np.nanmean(Temps))
print(np.nanmean(Col_Densities))

#%% Now to map these correctly across a image
Q1_Ints = np.transpose(np.reshape(Q1Ints, (13, 11)))
Set1_Int = Q1_Ints[:, 0:7]
Set2_Int_OffSlit = Q1_Ints[:, 7:9]
Set2_Int_OffSlit = np.flipud(Set2_Int_OffSlit)
Set2_Int = np.flipud(Q1_Ints[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ1 = np.hstack((Set1_Int, Off_Slit_Time))
New_IntQ1 = np.hstack((New_IntQ1, Set2_Int))
#New_IntQ1[New_IntQ1 == 0] = np.nan

#Now we need to convert the intensities from the line of sight enhancements
LOSc = []
Pixels = 8, 4, 0, 4, 8 # These are the limits of each pixel across Uranus
for iii in range(5):
    r_planet = 21.41/2 # radius of Uranus in pixels
    r_pathway = Pixels[iii]
    losc = np.cos(r_pathway/r_planet)
    LOSc.append(losc)

from Uranus_TimeToLong import Limits, Long_Err 
TIME = ['07:40', '08:08', '08:36', '09:04', '09:32', '10:00', '10:28', '10:56', '11:24', '11:52', '12:20', '12:48', '13:16']
PIXELS = ['2', '1', '0', '-1', '2']

plt.figure()
plt.imshow(New_IntQ1, cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ???', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(1,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
#plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.xlabel(r'Arbitary Uranian Longitude ($^\circ$) +- ??? $^\circ$')
plt.ylabel('Spatial position across Uranus (Pixel No. +- 1)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Q3_Ints = np.transpose(np.reshape(Q3Ints, (13, 11)))
Set1_Int = Q3_Ints[:, 0:7]
Set2_Int_OffSlit = Q3_Ints[:, 7:9]
Set2_Int_OffSlit = np.flipud(Set2_Int_OffSlit)
Set2_Int = np.flipud(Q3_Ints[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ3 = np.hstack((Set1_Int, Off_Slit_Time))
New_IntQ3 = np.hstack((New_IntQ3, Set2_Int))
#New_IntQ3[New_IntQ3 == 0] = np.nan

plt.figure()
plt.imshow(New_IntQ3, cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$)', fontsize=17.5)
plt.title(r'$H_{3}^{+}$ $Q(3,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Temperatures = np.transpose(np.reshape(Temps, (13, 11)))
Set1_Temp = Temperatures[:, 0:7]
Set2_Temp_OffSlit = Temperatures[:, 7:9]
Set2_Temp_OffSlit = np.flipud(Set2_Temp_OffSlit)
Set2_Temp = np.flipud(Temperatures[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_Temp = np.hstack((Set1_Temp, Off_Slit_Time))
New_Temp = np.hstack((New_Temp, Set2_Temp))
#New_Temp[New_Temp == 0] = np.nan

plt.figure()
plt.imshow(New_Temp, cmap=cm.coolwarm)
cbar = plt.colorbar()
cbar.set_label(r'Ro-vibrational Temperature (K) +- 23K', fontsize=17.5)
plt.title(r'$H_{3}^{+}$ Rotational Temperatures across Uranus from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 22.5)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Col_Density = np.transpose(np.reshape(Col_Densities, (13, 11)))
Set1_CD = Col_Density[:, 0:7]
Set2_CD_OffSlit = Col_Density[:, 7:9]
Set2_CD_OffSlit = np.flipud(Set2_CD_OffSlit)
Set2_CD = np.flipud(Col_Density[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_CD = np.hstack((Set1_CD, Off_Slit_Time))
New_CD = np.hstack((New_CD, Set2_CD))
#New_CD[New_CD == 0] = np.nan

plt.figure()
plt.imshow(New_CD, cmap='plasma')
cbar = plt.colorbar()
cbar.set_label(r'Column Density ($m^{-2}$) +- 0.15 x 10$^{16}$$m^{-2}$', fontsize=17.5)
plt.title(r'$H_{3}^{+}$ Column Density across Uranus from 07:28 to 13:21 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 22.5)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

T_emission = np.transpose(np.reshape(T_emission, (13, 11)))
Set1_TE = T_emission[:, 0:7]
Set2_TE_OffSlit = T_emission[:, 7:9]
Set2_TE_OffSlit = np.flipud(Set2_TE_OffSlit)
Set2_TE = np.flipud(T_emission[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_TE = np.hstack((Set1_TE, Off_Slit_Time))
New_TE = np.hstack((New_TE, Set2_TE))
#New_TE[New_TE == 0] = np.nan

plt.figure()
plt.imshow(New_TE*(10**6), cmap='cividis')
cbar = plt.colorbar()
cbar.set_label(r'Total $H_{3}^{+}$ Emission ($\mu$W$m^{-2}$sr$^{-1}$) +- 2.592 $\mu$W$m^{-2}$sr$^{-1}$', fontsize=17.5)
plt.title(r'Total $H_{3}^{+}$ Emission across Uranus from 07:28 to 13:21 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 22.5)
plt.xlabel('UTC Time (HH:MM ' + u'\u00B1' + ' 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

#%% Now to calculate the intensity of Emissions from Q1 and Q3 using curve fit

from lmfit import Model
from types import SimpleNamespace
import math

def gaussian_fit(x, a0, a1, a2, a3, a4, a5):
    z = (x - a1) / a2
    y = a0 * np.exp(-z**2 / a2) + a3 + a4 * x + a5 * x**2
    return y

ABBAi = []
A0_Q1 = []
Err_A0_Q1 = []
A0_Q3 = []
Err_A0_Q3 = []
A2_Q1 = []
Err_A2_Q1 = []
A2_Q3 = []
Err_A2_Q3 = []
FWHMQ1 = []
FWHMQ3 = []
INTSQ1 = []
INTSQ3 = []
XX= np.arange(300)
#from AvParams import AVALSAv
iiii = 0
for xx in range(13):
    ABBAi = (ABBAalpha[xx*4] + ABBAalpha[(xx*4)+1] + ABBAalpha[(xx*4)+2] + ABBAalpha[(xx*4)+3])/4
    for i in range(11):
        ABBAt = (ABBAi[2*i,:]+ABBAi[2*i+1,:])/2
        gmodel = Model(gaussian_fit)
        A01 = np.nanmax(ABBAt[0:300])
        A03 = np.nanmax(ABBAt[650:750])
        resultQ1 = gmodel.fit(ABBAt[0:300], x=XX, a0=A01, a1=142, a2=1.3, a3=0, a4=0, a5=0)
        resultQ3 = gmodel.fit(ABBAt[680:720], x=np.arange(40), a0=A03, a1=17, a2=1.3, a3=0, a4=0, a5=0)
        pQ1 = SimpleNamespace(**resultQ1.best_values)
        eQ1 = np.sqrt(np.diag(resultQ1.covar))
        A0_Q1.append(pQ1.a0)
        A2_Q1.append(pQ1.a2*5.856416015603827e-5)
        Err_A0_Q1.append(eQ1[0])
        Err_A2_Q1.append(eQ1[2]*5.856416015603827e-5)
        FWHM = pQ1.a2*5.856416015603827e-5*2*np.sqrt(2*math.log(2))
        FWHMQ1.append(FWHM)
        INTSQ1.append(pQ1.a0*FWHM)
        pQ3 = SimpleNamespace(**resultQ3.best_values)
        eQ3 = np.sqrt(np.diag(resultQ3.covar))
        A0_Q3.append(pQ3.a0)
        A2_Q3.append(pQ3.a2*5.856416015603827e-5)
        Err_A0_Q3.append(eQ3[0])
        Err_A2_Q3.append(eQ3[2]*5.856416015603827e-5)
        FWHM = pQ3.a2*5.856416015603827e-5*2*np.sqrt(2*math.log(2))
        FWHMQ3.append(FWHM)
        INTSQ3.append(pQ3.a0*FWHM)
        # if i == 11 and xx == 20:
        #     pass
            #plt.plot(np.arange(1024), ABBAt)
            #print(A0_Q1)
                
    print('ABBA Set ' + str(xx) + ' completed!')

Q1_IntErr = []
Q3_IntErr = []

for o in range(143):
    Q1IntErr = INTSQ1[o]*np.sqrt((Err_A0_Q1[o]/A0_Q1[o])**2 + (Err_A2_Q1[o]/A2_Q1[o])**2)
    Q1_IntErr.append(Q1IntErr)
    Q3IntErr = INTSQ3[o]*np.sqrt((Err_A0_Q3[o]/A0_Q3[o])**2 + (Err_A2_Q3[o]/A2_Q3[o])**2)
    Q3_IntErr.append(Q3IntErr)

Q1_IntsB = np.transpose(np.reshape(INTSQ1, (13, 11)))
Set1_IntB = Q1_IntsB[:, 0:7]
Set2_Int_OffSlitB = Q1_IntsB[:, 7:9]
Set2_Int_OffSlitB = np.flipud(Set2_Int_OffSlitB)
Set2_IntB = np.flipud(Q1_IntsB[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ1B = np.hstack((Set1_IntB, Off_Slit_Time))
New_IntQ1B = np.hstack((New_IntQ1B, Set2_IntB))
#New_IntQ1B[New_IntQ1B == 0] = np.nan

# #Now to create the graphs

# TIME = ['07:40', '08:08', '08:36', '09:04', '09:32', '10:00', '10:28', '10:56', '11:24', '11:52', '12:20', '12:48', '13:16']
# PIXELS = ['2', '1', '0', '-1', '2']

plt.figure()
plt.imshow(New_IntQ1B*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q1_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(1,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Q3_IntsB = np.transpose(np.reshape(INTSQ3, (13, 11)))
Set1_IntB = Q3_IntsB[:, 0:7]
Set2_Int_OffSlitB = Q3_IntsB[:, 7:9]
Set2_Int_OffSlitB = np.flipud(Set2_Int_OffSlitB)
Set2_IntB = np.flipud(Q3_IntsB[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ3B = np.hstack((Set1_IntB, Off_Slit_Time))
New_IntQ3B = np.hstack((New_IntQ3B, Set2_IntB))
#New_IntQ3B[New_IntQ3B == 0] = np.nan

plt.figure()
plt.imshow(New_IntQ3B*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q3_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(3,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)