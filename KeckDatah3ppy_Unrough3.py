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

#%%
#Now we pull the new Data Points and duplicate what happened in KeckDatah3ppy
with open('KeckDataPix0.csv', 'r') as file: #This reads in the file from 
    Pix0 = file.read().replace('\n', ' ')
    Pix0 = np.fromstring(Pix0, dtype=float, count=-1, sep= ' ')
    Pix0 = np.reshape(Pix0, (27, 1024))
file.close()

with open('KeckDataPix1.csv', 'r') as file: #This reads in the file from 
    Pix1 = file.read().replace('\n', ' ')
    Pix1 = np.fromstring(Pix1, dtype=float, count=-1, sep= ' ')
    Pix1 = np.reshape(Pix1, (27, 1024))
file.close()

with open('KeckDataPix2.csv', 'r') as file: #This reads in the file from 
    Pix2 = file.read().replace('\n', ' ')
    Pix2 = np.fromstring(Pix2, dtype=float, count=-1, sep= ' ')
    Pix2 = np.reshape(Pix2, (27, 1024))
file.close()

with open('KeckDataPix3.csv', 'r') as file: #This reads in the file from 
    Pix3 = file.read().replace('\n', ' ')
    Pix3 = np.fromstring(Pix3, dtype=float, count=-1, sep= ' ')
    Pix3 = np.reshape(Pix3, (27, 1024))
file.close()

with open('KeckDataPix4.csv', 'r') as file: #This reads in the file from 
    Pix4 = file.read().replace('\n', ' ')
    Pix4 = np.fromstring(Pix4, dtype=float, count=-1, sep= ' ')
    Pix4 = np.reshape(Pix4, (27, 1024))
file.close()

with open('KeckDataPix5.csv', 'r') as file: #This reads in the file from 
    Pix5 = file.read().replace('\n', ' ')
    Pix5 = np.fromstring(Pix5, dtype=float, count=-1, sep= ' ')
    Pix5 = np.reshape(Pix5, (27, 1024))
file.close()

with open('KeckDataPix6.csv', 'r') as file: #This reads in the file from 
    Pix6 = file.read().replace('\n', ' ')
    Pix6 = np.fromstring(Pix6, dtype=float, count=-1, sep= ' ')
    Pix6 = np.reshape(Pix6, (27, 1024))
file.close()

with open('KeckDataPix7.csv', 'r') as file: #This reads in the file from 
    Pix7 = file.read().replace('\n', ' ')
    Pix7 = np.fromstring(Pix7, dtype=float, count=-1, sep= ' ')
    Pix7 = np.reshape(Pix7, (27, 1024))
file.close()

with open('KeckDataPix8.csv', 'r') as file: #This reads in the file from 
    Pix8 = file.read().replace('\n', ' ')
    Pix8 = np.fromstring(Pix8, dtype=float, count=-1, sep= ' ')
    Pix8 = np.reshape(Pix8, (27, 1024))
file.close()

with open('KeckDataPix9.csv', 'r') as file: #This reads in the file from 
    Pix9 = file.read().replace('\n', ' ')
    Pix9 = np.fromstring(Pix9, dtype=float, count=-1, sep= ' ')
    Pix9 = np.reshape(Pix9, (27, 1024))
file.close()

with open('KeckDataPix10.csv', 'r') as file: #This reads in the file from 
    Pix10 = file.read().replace('\n', ' ')
    Pix10 = np.fromstring(Pix10, dtype=float, count=-1, sep= ' ')
    Pix10 = np.reshape(Pix10, (27, 1024))
file.close()

with open('KeckDataPix11.csv', 'r') as file: #This reads in the file from 
    Pix11 = file.read().replace('\n', ' ')
    Pix11 = np.fromstring(Pix11, dtype=float, count=-1, sep= ' ')
    Pix11 = np.reshape(Pix11, (27, 1024))
file.close()

with open('KeckDataPix12.csv', 'r') as file: #This reads in the file from 
    Pix12 = file.read().replace('\n', ' ')
    Pix12 = np.fromstring(Pix12, dtype=float, count=-1, sep= ' ')
    Pix12 = np.reshape(Pix12, (27, 1024))
file.close()

with open('KeckDataPix13.csv', 'r') as file: #This reads in the file from 
    Pix13 = file.read().replace('\n', ' ')
    Pix13 = np.fromstring(Pix13, dtype=float, count=-1, sep= ' ')
    Pix13 = np.reshape(Pix13, (27, 1024))
file.close()

with open('KeckDataPix14.csv', 'r') as file: #This reads in the file from 
    Pix14 = file.read().replace('\n', ' ')
    Pix14 = np.fromstring(Pix14, dtype=float, count=-1, sep= ' ')
    Pix14 = np.reshape(Pix14, (27, 1024))
file.close()

with open('KeckDataPix15.csv', 'r') as file: #This reads in the file from 
    Pix15 = file.read().replace('\n', ' ')
    Pix15 = np.fromstring(Pix15, dtype=float, count=-1, sep= ' ')
    Pix15 = np.reshape(Pix15, (27, 1024))
file.close()

with open('KeckDataPix16.csv', 'r') as file: #This reads in the file from 
    Pix16 = file.read().replace('\n', ' ')
    Pix16 = np.fromstring(Pix16, dtype=float, count=-1, sep= ' ')
    Pix16 = np.reshape(Pix16, (27, 1024))
file.close()

with open('KeckDataPix17.csv', 'r') as file: #This reads in the file from 
    Pix17 = file.read().replace('\n', ' ')
    Pix17 = np.fromstring(Pix17, dtype=float, count=-1, sep= ' ')
    Pix17 = np.reshape(Pix17, (27, 1024))
file.close()

with open('KeckDataPix18.csv', 'r') as file: #This reads in the file from 
    Pix18 = file.read().replace('\n', ' ')
    Pix18 = np.fromstring(Pix18, dtype=float, count=-1, sep= ' ')
    Pix18 = np.reshape(Pix18, (27, 1024))
file.close()

with open('KeckDataPix19.csv', 'r') as file: #This reads in the file from 
    Pix19 = file.read().replace('\n', ' ')
    Pix19 = np.fromstring(Pix19, dtype=float, count=-1, sep= ' ')
    Pix19 = np.reshape(Pix19, (27, 1024))
file.close()

with open('KeckDataPix20.csv', 'r') as file: #This reads in the file from 
    Pix20 = file.read().replace('\n', ' ')
    Pix20 = np.fromstring(Pix20, dtype=float, count=-1, sep= ' ')
    Pix20 = np.reshape(Pix20, (27, 1024))
file.close()

with open('KeckDataPix21.csv', 'r') as file: #This reads in the file from 
    Pix21 = file.read().replace('\n', ' ')
    Pix21 = np.fromstring(Pix21, dtype=float, count=-1, sep= ' ')
    Pix21 = np.reshape(Pix21, (27, 1024))
file.close()

New_Pix0 = (Pix0 + Pix1)/2
New_Pix1 = (Pix2 + Pix3)/2
New_Pix2 = (Pix4 + Pix5)/2
New_Pix3 = (Pix6 + Pix7)/2
New_Pix4 = (Pix8 + Pix9)/2
New_Pix5 = (Pix10 + Pix11)/2
New_Pix6 = (Pix12 + Pix13)/2
New_Pix7 = (Pix14 + Pix15)/2
New_Pix8 = (Pix16 + Pix17)/2
New_Pix9 = (Pix18 + Pix19)/2
New_Pix10 = (Pix20 + Pix21)/2

# New_Pix0 = (Pix0 + Pix1)
# New_Pix1 = (Pix2 + Pix3)
# New_Pix2 = (Pix4 + Pix5)
# New_Pix3 = (Pix6 + Pix7)
# New_Pix4 = (Pix8 + Pix9)
# New_Pix5 = (Pix10 + Pix11)
# New_Pix6 = (Pix12 + Pix13)
# New_Pix7 = (Pix14 + Pix15)
# New_Pix8 = (Pix16 + Pix17)
# New_Pix9 = (Pix18 + Pix19)
# New_Pix10 = (Pix20 + Pix21)

#Produce a final Pix array
New_Pixels = np.array([New_Pix0, New_Pix1, New_Pix2, New_Pix3, New_Pix4, New_Pix5, New_Pix6, New_Pix7, New_Pix8, New_Pix9, New_Pix10])

#%%Assuming everything has gone to plan we can then put in the rest of the results and see what we get out at the end
# Create the h3ppy object feed data into it
    
h3p = h3ppy.h3p()
wave = h3p.wavegen(3.94466192, 4.00463162, 1024)
Q1Ints = []
Q3Ints = []
Temps = []
T_err = []
Col_Densities = []
Col_err = []
T_emission = []
Tot_EM_Err = []
c = 0

for p in range(11):
    data = New_Pixels[p]
    for m in range(13):
            datai = data[2*m, :]
            dataii = data[2*m+1,:]
            #dataii = data[2*m+1,:]
            # Set the wavelength and the data
            h3p.set(nbackground = 1, wavelength = wave, data = (datai+dataii)/2, R = 20000, temperature = 576)
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
            if Vars == False:
                A2 = Vars['sigma_0']
                FWHM = A2*2*np.sqrt(2*math.log(2))
                Q1Ints.append(np.nanmax(fit3)*1000000*FWHM)
                Q3Ints.append(np.nanmax(fit3[400:1024])*1000000*FWHM)
                Temps.append(0)
                T_err.append(0)
                Col_Densities.append(0)
                Col_err.append(0)
            else:
                A2 = Vars['sigma_0']
                FWHM = A2*2*np.sqrt(2*math.log(2))
                Q1Ints.append(np.nanmax(fit3)*1000000*FWHM)
                Q3Ints.append(np.nanmax(fit3[400:1024])*1000000*FWHM)
                Temps.append(Vars['temperature'])
                T_err.append(errs['temperature'])
                Col_Densities.append(Vars['density'])
                Col_err.append(errs['density'])
                #c += 1
                #print(c)

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
    
#%% Now to map these correctly across a image
Q1Ints = np.array(Q1Ints)
Q1_Ints = np.reshape(Q1Ints, (11, 13))
Set1_Int = Q1_Ints[:, 0:7]
Set2_Int_OffSlit = Q1_Ints[:, 7:9]
Set2_Int_OffSlit = np.flipud(Set2_Int_OffSlit)
Set2_Int = np.flipud(Q1_Ints[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ1 = np.hstack((Set1_Int, Off_Slit_Time))
New_IntQ1 = np.hstack((New_IntQ1, Set2_Int))
New_IntQ1[New_IntQ1 == 0] = np.nan

#Now we need to convert the intensities from the line of sight enhancements
LOSc = []
Pixels = 8, 4, 0, 4, 8 # These are the limits of each pixel across Uranus
for iii in range(5):
    r_planet = 21.41/2 # radius of Uranus in pixels
    r_pathway = Pixels[iii]
    losc = np.cos(r_pathway/r_planet)
    LOSc.append(losc)

#New_IntQ1B = []
#for iiii in range(13):
#    o = 0
#    Int = New_IntQ1[:,iiii]
#    if o == 0:
#        Int0 = Int[0]*LOSc[0]
#        o += 1
#    New_IntQ1B.append(Int0)
#    if o == 1:
#        Int1 = Int[1]*LOSc[1]
#        o += 1
#    New_IntQ1B.append(Int1)
#    if o == 2:
#        Int2 = Int[2]*LOSc[2]
#        o += 1
#    New_IntQ1B.append(Int2)
#    if o == 3:
#        Int3 = Int[3]*LOSc[3]
#        o += 1
#    New_IntQ1B.append(Int3)
#    if o == 4:
#        Int4 = Int[4]*LOSc[4]
#    New_IntQ1B.append(Int4)
#
#New_IntQ1B = np.reshape(New_IntQ1B, (13, 10))
#New_IntQ1B = np.transpose(New_IntQ1B)

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

Q3Ints = np.array(Q3Ints)
Q3_Ints = np.reshape(Q3Ints, (11, 13))
Set1_Int = Q3_Ints[:, 0:7]
Set2_Int_OffSlit = Q3_Ints[:, 7:9]
Set2_Int_OffSlit = np.flipud(Set2_Int_OffSlit)
Set2_Int = np.flipud(Q3_Ints[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ3 = np.hstack((Set1_Int, Off_Slit_Time))
New_IntQ3 = np.hstack((New_IntQ3, Set2_Int))
New_IntQ3[New_IntQ3 == 0] = np.nan

#New_IntQ3B = []
#for iiii in range(13):
#    o = 0
#    Int = New_IntQ3[:,iiii]
#    if o == 0:
#        Int0 = Int[0]*LOSc[0]
#        o += 1
#    New_IntQ3B.append(Int0)
#    if o == 1:
#        Int1 = Int[1]*LOSc[1]
#        o += 1
#    New_IntQ3B.append(Int1)
#    if o == 2:
#        Int2 = Int[2]*LOSc[2]
#        o += 1
#    New_IntQ3B.append(Int2)
#    if o == 3:
#        Int3 = Int[3]*LOSc[3]
#        o += 1
#    New_IntQ3B.append(Int3)
#    if o == 4:
#        Int4 = Int[4]*LOSc[4]
#    New_IntQ3B.append(Int4)
#    
#New_IntQ3B = np.reshape(New_IntQ3B, (13, 10))
#New_IntQ3B = np.transpose(New_IntQ3B)

plt.figure()
plt.imshow(New_IntQ3, cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$)', fontsize=17.5)
plt.title(r'$H_{3}^{+}$ $Q(3,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Temps = np.array(Temps)
Temperatures = np.reshape(Temps, (11, 13))
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

Col_Densities = np.array(Col_Densities)
Col_Density = np.reshape(Col_Densities, (11, 13))
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

T_emission = np.array(T_emission)
T_emission = np.reshape(T_emission, (11, 13))
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

def gauss_fit(x, a0, a1, a2, a3, a4, a5): # First write a guassian function credit to pen and pants IDL's Gaussfit in Python
    z = (x - a1) / a2
    y = a0 * np.exp(-z**2 / a2) + a3 + a4 * x + a5 * x**2
    return y

XX = np.arange(400)
X = np.arange(100)
#specically around 0-400 and 650-750 curve fit
for p in range(11):
    data = New_Pixels[p]
    for m in range(13):
        datai = data[2*m, :]
        dataii = data[(2*m+1), :]
        DATA = (datai + dataii)/2
        gmodel = Model(gauss_fit)
        resultQ1 = gmodel.fit(DATA[0:400], x=XX, a0=0.003, a1=142, a2=1.5, a3=0, a4=0, a5=0)
        resultQ3 = gmodel.fit(DATA[650:750], x=X, a0=0.002, a1=47, a2=1.5, a3=0, a4=0, a5=0)
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

#Now to calculate the Intenisty and Errs for graphs
#Intensity values for Q1 and Q3
Q1IntsB = np.array(INTSQ1)
Q1_IntsB = np.reshape(Q1IntsB, (11, 13))
Set1_IntB = Q1_IntsB[:, 0:7]
Set2_Int_OffSlitB = Q1_IntsB[:, 7:9]
Set2_Int_OffSlitB = np.flipud(Set2_Int_OffSlitB)
Set2_IntB = np.flipud(Q1_IntsB[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ1B = np.hstack((Set1_IntB, Off_Slit_Time))
New_IntQ1B = np.hstack((New_IntQ1B, Set2_IntB))
#New_IntQ1B[New_IntQ1B == 0] = np.nan

#New_IntQ1C = []
#for iiii in range(13):
#    o = 0
#    Int = New_IntQ1B[:,iiii]
#    if o == 0:
#        Int0 = Int[0]*LOSc[0]
#        o += 1
#    New_IntQ1C.append(Int0)
#    if o == 1:
#        Int1 = Int[1]*LOSc[1]
#        o += 1
#    New_IntQ1C.append(Int1)
#    if o == 2:
#        Int2 = Int[2]*LOSc[2]
#        o += 1
#    New_IntQ1C.append(Int2)
#    if o == 3:
#        Int3 = Int[3]*LOSc[3]
#        o += 1
#    New_IntQ1C.append(Int3)
#    if o == 4:
#        Int4 = Int[4]*LOSc[4]
#    New_IntQ1C.append(Int4)
#    
#New_IntQ1C = np.reshape(New_IntQ1C, (13, 5))
#New_IntQ1C = np.transpose(New_IntQ1C)

#Now to calculate the errors
Q1_IntErr = []
Q3_IntErr = []

for o in range(143):
    Q1IntErr = INTSQ1[o]*np.sqrt((Err_A0_Q1[o]/A0_Q1[o])**2 + (Err_A2_Q1[o]/A2_Q1[o])**2)
    Q1_IntErr.append(Q1IntErr)
    Q3IntErr = INTSQ3[o]*np.sqrt((Err_A0_Q3[o]/A0_Q3[o])**2 + (Err_A2_Q3[o]/A2_Q3[o])**2)
    Q3_IntErr.append(Q3IntErr)

#Now to create the graphs

TIME = ['07:40', '08:08', '08:36', '09:04', '09:32', '10:00', '10:28', '10:56', '11:24', '11:52', '12:20', '12:48', '13:16']
PIXELS = ['2', '1', '0', '-1', '2']

plt.figure()
plt.imshow(New_IntQ1B*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q1_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(1,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)

Q3IntsB = np.array(INTSQ3)
Q3_IntsB = np.reshape(Q3IntsB, (11, 13))
Set1_IntB = Q3_IntsB[:, 0:7]
Set2_Int_OffSlitB = Q3_IntsB[:, 7:9]
Set2_Int_OffSlitB = np.flipud(Set2_Int_OffSlitB)
Set2_IntB = np.flipud(Q3_IntsB[:, 9:14])

Off_Slit_Time = np.zeros((11,2))
New_IntQ3B = np.hstack((Set1_IntB, Off_Slit_Time))
New_IntQ3B = np.hstack((New_IntQ3B, Set2_IntB))
#New_IntQ3B[New_IntQ3B == 0] = np.nan

#New_IntQ3C = []
#for iiii in range(13):
#    o = 0
#    Int = New_IntQ3B[:,iiii]
#    if o == 0:
#        Int0 = Int[0]*LOSc[0]
#        o += 1
#    New_IntQ3C.append(Int0)
#    if o == 1:
#        Int1 = Int[1]*LOSc[1]
#        o += 1
#    New_IntQ3C.append(Int1)
#    if o == 2:
#        Int2 = Int[2]*LOSc[2]
#        o += 1
#    New_IntQ3C.append(Int2)
#    if o == 3:
#        Int3 = Int[3]*LOSc[3]
#        o += 1
#    New_IntQ3C.append(Int3)
#    if o == 4:
#        Int4 = Int[4]*LOSc[4]
#    New_IntQ3C.append(Int4)
#    
#New_IntQ3C = np.reshape(New_IntQ3C, (13, 5))
#New_IntQ3C = np.transpose(New_IntQ3C)

TIME = ['07:40', '08:08', '08:36', '09:04', '09:32', '10:00', '10:28', '10:56', '11:24', '11:52', '12:20', '12:48', '13:16']
PIXELS = ['46.66', '21.32', '0', '-21.32', '-46.66']

plt.figure()
plt.imshow(New_IntQ3B*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q3_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(3,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
plt.xticks(np.arange(13), TIME)
#plt.yticks(np.arange(5), PIXELS)