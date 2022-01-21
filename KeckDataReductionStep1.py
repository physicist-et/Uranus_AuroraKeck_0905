# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:16:02 2020

@author: Emma 'Amelia'
"""
# Here we will extract out the star files, the flat files and dark files to be used in the first stage of data reduction

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits #import the relevant directories to read a fits file from your directory and plot it
from types import SimpleNamespace
from skimage import exposure
from matplotlib import cm
from gaussstar import gaussstar

from lmfit import Model

Star1_Data = []
Star2_Data = []
Flats_Darks_Data = []
Lamps_Data = []

for n in range(299): #We use this list to create a list which holds all the data from Order19
    num = n + 1
    if num < 6:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_000' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Flats_Darks_Data.append(image_datai)
    elif num < 8 and num > 5:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_000' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Lamps_Data.append(image_datai)
    elif num >= 72 and num < 76:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_00' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Star1_Data.append(image_datai)
    elif num >= 192 and num < 196:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_0' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Star2_Data.append(image_datai)

Gauss_Star_Factor = gaussstar()
s = 0
Darks = (Flats_Darks_Data[(s+2)] + Flats_Darks_Data[(s+3)])/2

True_Darks = Darks

Calibrate1 = (Flats_Darks_Data[s] - True_Darks)
Calibrate2 = (Flats_Darks_Data[s+1] - True_Darks)
Calibrate3 = (Flats_Darks_Data[s+4] - True_Darks)

Lamps = (Lamps_Data[s+1] - Lamps_Data[s])

Cal_Lamps = Lamps/(10*0.250)

Cal_Flats = (Calibrate1 + Calibrate2 + Calibrate3)/(3*2*10)

Cal_Darks = True_Darks/(2*10)

#Sort the view of the imshow
p_lower, p_higher = np.percentile(Cal_Darks, (0.01, 99.9))
array_to_view = exposure.rescale_intensity(Cal_Darks, in_range=(p_lower, p_higher))

fig = plt.figure(figsize=(12,8))
plt.imshow(array_to_view, cmap='gist_gray')
plt.xlabel(r'Wavelength Pixel Position (5.7851 x 10$^{-5}$ $\mu$m per pixel)', fontsize=20)
plt.ylabel('Spatial Pixel Position across the Slit (Pixel No.)', fontsize=20)
plt.title('Dark Frame', fontsize=25)
m = cm.ScalarMappable(cmap='gist_gray')
m.set_array(array_to_view)
cbar = fig.colorbar(m, ticks=[-1, -0.5, 0, 0.5, 1])
cbar.ax.set_yticklabels(['0', '0.25', '0.5', '0.75', '1.0'], fontsize=12.5)
cbar.set_label('Normalisted Detector counts', fontsize=20)

p_lower, p_higher = np.percentile(Cal_Flats, (5, 95))
array_to_view = exposure.rescale_intensity(Cal_Flats, in_range=(p_lower, p_higher))

fig = plt.figure(figsize=(12,8))
plt.imshow(array_to_view, cmap='gist_gray')
plt.xlabel(r'Wavelength Pixel Position (5.7851 x 10$^{-5}$ $\mu$m per pixel)', fontsize=20)
plt.ylabel('Spatial Pixel Position across the Slit (Pixel No.)', fontsize=20)
plt.title('Flat Frame', fontsize=25)
m = cm.ScalarMappable(cmap='gist_gray')
m.set_array(array_to_view)
cbar = fig.colorbar(m, ticks=[0, 0.25, 0.5, 0.75, 1])
cbar.ax.set_yticklabels(['0', '0.25', '0.5', '0.75', '1.0'], fontsize=12.5)
cbar.set_label('Normalised Detector counts', fontsize=20)

Star1_DataA1 = (Star1_Data[0]/(60*Gauss_Star_Factor)) - Cal_Flats
Star1_DataB1 = (Star1_Data[1]/(60*Gauss_Star_Factor)) - Cal_Flats
Star1_DataB2 = (Star1_Data[2]/(60*Gauss_Star_Factor)) - Cal_Flats
Star1_DataA2 = (Star1_Data[3]/(60*Gauss_Star_Factor)) - Cal_Flats

Star2_DataA1 = (Star2_Data[0]/(60*Gauss_Star_Factor)) - Cal_Flats
Star2_DataB1 = (Star2_Data[1]/(60*Gauss_Star_Factor)) - Cal_Flats
Star2_DataB2 = (Star2_Data[2]/(60*Gauss_Star_Factor)) - Cal_Flats
Star2_DataA2 = (Star2_Data[3]/(60*Gauss_Star_Factor)) - Cal_Flats

Star1 = (Star1_DataA1 - Star1_DataB1 - Star1_DataB2 + Star1_DataA2)/4
Star2 = (Star2_DataA1 - Star2_DataB1 - Star2_DataB2 + Star2_DataA2)/4

#plt.figure()
#plt.imshow(True_Star1, cmap='gist_gray')
#plt.axhline(84, color='r', ls='--')
#plt.axhline(160, color='b', ls='--')

plt.figure()
plt.imshow(Star2, cmap='gist_gray')
plt.title('Order 19 spectra of HD 215 143 observed on 5th September 2006', fontsize=25)
plt.xlabel(r'Wavelength $\lambda$ (+- 0.0016 $\mu$m)', fontsize=20)
label_x = 0, 200, 400, 600, 800, 1000
plt.xticks(label_x, ('3.9448', '3.9564', '3.9680', '3.9795', '3.9911', '4.0003'), fontsize=10)
plt.ylabel('Spatial Pixel No. across the slit (Pixel No.)', fontsize=20)
plt.axvline(696.652257000841, color='r', ls='--')
plt.axvline(142.22591552273104, color='r', ls='--')
plt.axhline(82, color='r', ls='--')
plt.axhline(158, color='b', ls='--')

#plt.figure()
#plt.imshow(Cal_Lamps, cmap='gist_gray')
#plt.xlabel('Wavelength Pixel Position', fontsize=20)
#plt.ylabel('Spatial Pixel Position across the Slit', fontsize=20)
#plt.title('Scaled Lamp Arcs across Order 19', fontsize=25)
#cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
#cbar.set_label('Uncalibrated Intensity (CCD Counts per second)', fontsize=20)

#Now we will determine the correct fit for the line by fitting a gaussian over the star fits files and finding the peak position 
# Now match a gaussian profile across all 5 lines to find the intensity, and width of the slit
def gaussian_fit(x, a0, a1, a2, a3, a4, a5): # First write a guassian function credit to pen and pants IDL's Gaussfit in Python
    z = (x - a1) / a2
    y = a0 * np.exp(-z**2 / a2) + a3 + a4 * x + a5 * x**2
    return y

Star1P = Star1[50:120,:]
Star1N = Star2[125:195,:]

Star2P = Star1[50:120,:]
Star2N = Star2[125:195,:]
X = np.arange(70)

Star1PPeak = []
Star1NPeak = []
A0Star1P = []
A2Star1P = []
A0Star1N = []
A2Star1N = []

for i in range(1024):
    StarP = Star1P[:,i]
    StarN = Star1N[:,i]
    gmodel = Model(gaussian_fit)
    result1P = gmodel.fit(StarP, x=X, a0=45.992871104978725, a1=34.3, a2=1.9, a3=-0.6, a4=0, a5=0)
    result1N = gmodel.fit(StarN, x=X, a0=-62.95745470927416, a1=36.1, a2=2.0, a3=-0.7, a4=0, a5=0)
    p = SimpleNamespace(**result1P.best_values)
    n = SimpleNamespace(**result1N.best_values)
    Star1PPeak.append(p.a1+50)
    Star1NPeak.append(n.a1+125)
    A0Star1P.append(p.a0)
    A2Star1P.append(p.a2)
    A0Star1N.append(n.a0)
    A2Star1N.append(n.a2)

Peak1P = np.array(Star1PPeak)
Peak1N = np.array(Star1NPeak)
ABBASep = Peak1N - Peak1P
XI = np.arange(1024)

plt.figure()
plt.title(r'Peak pixel position for both A frame and B frame emissions of HD 218 639')
plt.xlabel(r'Wavelength $\lambda$ (+- 0.0016 $\mu$m)')
label_x = 0, 200, 400, 600, 800, 1000
plt.xticks(label_x, ('3.9448', '3.9564', '3.9680', '3.9795', '3.9911', '4.0003'), fontsize=10)
plt.ylabel(r'Spatial Pixel No. across the slit (Pixel No.)')
plt.plot(XI, Peak1P, color='r')
plt.plot(XI, Peak1N, color='b')
plt.plot(XI, ABBASep, color='g')
plt.ylim(0,228)
plt.xlim(0,1024)

#Now find the difference between the AR and DEC
PyThag1 = np.sqrt((347.45797-347.45506)**2 + (-14.51132+14.50954)**2)
Sep_Ratio = PyThag1*3600
print('Arc seconds seperation for Star 1 is ' + str(np.mean(Sep_Ratio)) + ' +- ' + str(np.std(Sep_Ratio)) + ' Arc seconds')

Spat_Ratio = (PyThag1*3600)/ABBASep
print('The spatial scale for Star 1 is ' + str(np.mean((Spat_Ratio))) + ' +- ' + str(np.std((Spat_Ratio))) + ' Arc second per pixel')

#Now we will do the exact same for Star 2 HD 215 143 as we did for Star 1 HD 218 639
Star2PPeak = []
Star2NPeak = []
A0Star2P = []
A2Star2P = []
A0Star2N = []
A2Star2N = []

for i in range(1024):
    StarP = Star2P[:,i]
    StarN = Star2N[:,i]
    gmodel = Model(gaussian_fit)
    result2P = gmodel.fit(StarP, x=X, a0=54.09817216036432, a1=31.9, a2=2.6, a3=0, a4=0, a5=0)
    result2N = gmodel.fit(StarN, x=X, a0=-54.09817216036432, a1=33.7, a2=2.65, a3=0, a4=0, a5=0)
    p = SimpleNamespace(**result2P.best_values)
    n = SimpleNamespace(**result2N.best_values)
    Star2PPeak.append(p.a1+50)
    Star2NPeak.append(n.a1+125)
    A0Star2P.append(p.a0)
    A2Star2P.append(p.a2)
    A0Star2N.append(n.a0)
    A2Star2N.append(n.a2)

Peak2P = np.array(Star2PPeak)
Peak2N = np.array(Star2NPeak)
ABBA2Sep = Peak2N - Peak2P
XI = np.arange(1024)

plt.figure()
plt.title(r'Peak pixel position for both A frame and B frame emissions of HD 215 143', fontsize=20)
plt.xlabel(r'Wavelength $\lambda$ (+- 0.0016 $\mu$m)', fontsize=15)
label_x = 0, 200, 400, 600, 800, 1000
plt.xticks(label_x, ('3.9448', '3.9564', '3.9680', '3.9795', '3.9911', '4.0003'), fontsize=10)
plt.ylabel(r'Spatial Pixel No. across the slit (Pixel No.)', fontsize=15)
plt.plot(XI, Peak2P, color='r')
plt.plot(XI, Peak2N, color='b')
plt.plot(XI, ABBA2Sep, color='g')
plt.ylim(0,228)
plt.xlim(0,1024)

#Now find the difference between the AR and DEC
Pythag2 = np.sqrt((-6.963025+6.962605)**2 + (340.81135-340.807805)**2)
Sep_Ratio2 = Pythag2*3600
print('Arc seconds seperation for Star 2 is ' + str(np.mean(Sep_Ratio2)) + ' +- ' + str(np.std(Sep_Ratio2)) + ' Arc seconds')

Spat_Ratio2 = (Pythag2*3600)/ABBA2Sep
print('The spatial scale for Star 2 is ' + str(np.mean(Spat_Ratio2)) + ' +- ' + str(np.std(Spat_Ratio2)) + ' Arc second per pixel')

#Now that the Spatial Ratio's are known between Star's we will now work out their Observed Flux to compare it against the expected.
A0Star1P = np.array(A0Star1P)
A2Star1P = np.array(A2Star1P)
A0Star1N = np.array(A0Star1N)
A2Star1N = np.array(A2Star1N)

A0Star2P = np.array(A0Star2P)
A2Star2P = np.array(A2Star2P)
A0Star2N = np.array(A0Star2N)
A2Star2N = np.array(A2Star2N)

FWHM_Star1P = A2Star1P*2*np.sqrt(2*np.log(2))
FWHM_Star1N = A2Star1N*2*np.sqrt(2*np.log(2))

FWHM_Star2P = A2Star2P*2*np.sqrt(2*np.log(2))
FWHM_Star2N = A2Star2N*2*np.sqrt(2*np.log(2))

Flux_Star1 = (((A0Star1P*FWHM_Star1P)+(-1*A0Star1N*FWHM_Star1N))/2)
Flux_Star2 = (((A0Star2P*FWHM_Star2P)+(-1*A0Star2N*FWHM_Star2N))/2)

#Now we need to find the spectral scaling across each order to find the flux calibration

#From here we need to find the expected Intensity of each Star to find the ratio used for our Data files, as found in Rosie's Thesis
#This is between 3.94 and 4.00 micrometers so the atmospheric window is most likely in the L' filter
F_HD218 = 4.07*(10**-10)
F_HD215 = 4.07*(10**-10)
F_HR1578 = 4.07*(10**-10)
F_Star = 7.3*(10**-11)
M_lambda_HR1578 = 6.417 # at 2.2 micrometers
M_lambda_HD218 = 6.369
M_lambda_HD215 = 6.480
M_lambda_star = 3.4

F_A0_HD218 = F_HD218*(10**(-0.4*M_lambda_HD218))
F_A0_HD215 = F_HD215*(10**(-0.4*M_lambda_HD215))
F_A0_HR1578 = F_HR1578*(10**(-0.4*M_lambda_HR1578))
F_A0_star = F_Star*(10**(-0.4*M_lambda_star))

hc = (6.63*10**-34)*(2.99*10**8)
kb = 1.38*10**-23
T_HD218 = 10000
T_HD215 = 11000
T_HR1578 = 10000
T_star = 10000
Lambda_AW = 2.2 # In micrometers
Lambda_AW1 = 3.45
Lambda = (np.arange(1024)*0.00005817)+3.9448

Fbb_HD218 = F_A0_HD218*((Lambda_AW/Lambda)**5)*(np.exp((hc/kb)/(Lambda_AW*T_HD218))/(np.exp((hc/kb)/(Lambda*T_HD218))))
Fbb_HD215 = F_A0_HD215*((Lambda_AW/Lambda)**5)*(np.exp((hc/kb)/(Lambda_AW*T_HD215))/(np.exp((hc/kb)/(Lambda*T_HD215))))
Fbb_HR1578 = F_A0_HR1578*((Lambda_AW/Lambda)**5)*(np.exp((hc/kb)/(Lambda_AW*T_HR1578))/(np.exp((hc/kb)/(Lambda*T_HR1578))))
Fbb_star = F_A0_star*((Lambda_AW1/Lambda)**5)*(np.exp((hc/kb)/(Lambda_AW1*T_star))/(np.exp((hc/kb)/(Lambda*T_star))))

Flux_Star1 = (Flux_Star1)/Lambda
Flux_Star2 = (Flux_Star2)/Lambda

#Now we can compare the lines against the expected values for the flux of these stars
fig, ax = plt.subplots()
#ax.plot(Lambda, Flux_Star1, color='r', label='HD 218 639 observed')
ax.plot(Lambda, Flux_Star2, color='k', label='HD 215 143 observed')
ax.set_xlabel(r'Wavelength  $\lambda$ ($\mu$m)', fontsize=15)
ax.set_ylabel(r'Uncalibrated Intensity (CCD countss$^{-1}$$\mu$m$^{-1}$)', fontsize=15)
ax.set_title(r'Observed and Expected Flux of HD 215 143 across Order 19', fontsize=20)
ax.set_ylim(0, 60)
ax.set_xlim(Lambda[0], Lambda[1023])
ax.grid()
ax2=ax.twinx()
#ax2.plot(Lambda, Fbb_HD218, color='k', label='HD 218 639 expected')
ax2.plot(Lambda, Fbb_HD215, color='b', label='HD 215 143 expected')
ax2.plot(Lambda, Fbb_HR1578, color='g', label='HR 1578 expected')
ax2.plot(Lambda, Fbb_star, color='r', label='Henrik example')
#ax2.set_ylabel(r'Blackbody Flux (Wm$^{-2}$$\mu$m$^{-1}$)', fontsize=15)
#ax2.set_ylim(0, 40*(10**-13))
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

#Finally we will work out the Intensity to CCD counts ratio for order 19 which can be used on the data from order 19
Fc_HD218 = Fbb_HD218/Flux_Star1
Fc_HD215 = Fbb_HD215/Flux_Star2

#plt.figure()
#plt.plot(Lambda, Fc_HD218, color='r', label='HD 218 639 calibration spectrum')
#plt.plot(Lambda, Fc_HD215, color='k', label='HD 215 143 calibration spectrum')
#plt.xlabel(r'Wavelength $\lambda$ ($\mu$m)', fontsize=15)
#plt.ylabel(r'Flux (Wm$^{-2}$$\mu$m$^{-1}$Counts$^{-1}$)', fontsize=15)
#plt.title(r'Flux Calibration Spectre HD 215 143 aross Order 19', fontsize=20)
#plt.legend(loc='upper right')
#plt.xlim(Lambda[0], Lambda[1023])
#plt.grid()
#plt.ylim(0.18*(10**-15), 0.3*(10**-15))