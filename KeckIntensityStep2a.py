# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:43:47 2020

@author: Emma 'Amelia'
"""
# Recreate the Total file we found in Step 2 and then recreating the same ABBA pattern with 28 sets

#### Load a fits file in Python and print the headers ####

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits #import the relevant directories to read a fits file from your directory and plot it
from scipy.optimize import curve_fit
from KeckDataReductionStep1 import Cal_Flats
image_file1 = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_0111.fits' #imports a single fits file from the cwd + the file path in the commas
fits.open(image_file1)

image_data1 = fits.getdata(image_file1, ext=0) #Focuses specifically on the array data contained within the fits file

Keck_Data = [] #First create lists in which the arrays of Keck data will go into
Keck_DataABBA = []
Keck_Data_Total = np.zeros((image_data1.shape[0], image_data1.shape[1]))
s = 0 #This will be used to create the ABBA pattern

for n in range(224): #We use this list to create a list which holds all the data from Order19
    num = n + 76
    if num < 100:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_00' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Keck_Data.append(image_datai)
    elif num < 192 and num >= 100:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_0' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Keck_Data.append(image_datai)
    elif num >= 192 and num < 196:
        print('Star files')
    elif num >= 196 and num < 296:
        image_filei = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/05Sep06 Observations/uranus/order19/05sep06_0' + str(num) + '.fits'
        fits.open(image_filei)
        image_datai = fits.getdata(image_filei, ext=0)
        Keck_Data.append(image_datai)
    else:
        print('Galaxy files')
    
ABsubs = len(Keck_Data)//4 #We create this variable to create the ABBA pattern

# for n in range(ABsubs): #This for loop uses the A - B - B + A and adds them into a list Keck_DataABBA before creating a total spectra 
#     image_dataSUB = ((Keck_Data[s]/60 - Cal_Flats) - (Keck_Data[(s+1)]/60 - Cal_Flats) - (Keck_Data[(s+2)]/60 - Cal_Flats) + (Keck_Data[(s+3)]/60 - Cal_Flats))/4
#     Keck_DataABBA.append(image_dataSUB)
#     s += 4
#     Keck_Data_Total += Keck_DataABBA[n]
#     filename = 'KeckDataABBASet' + str(n) + '.txt'
#     np.savetxt(filename, Keck_DataABBA[n])

# Save the data files for all Keck_DataABBA Files

#### Plot a intensity graph of order 19, of the first ABBA method and of all the ABBA results ####

#plt.figure()
#plt.imshow(Keck_DataABBA[0], cmap='gist_gray')
#plt.title(r'First ABBA observation set of Uranus with NIRSPEC on $5^{th}$ September 2006', fontsize=23)
#plt.xlabel(r'Wavelength ($\mu$m)', fontsize=20)
#label_x = 0, 200, 400, 600, 800, 1000
#plt.xticks(label_x, ('3.9445', '3.9565', '3.9685', '3.9804', '3.9924', '4.0044'), fontsize=15)
#plt.ylabel('Spatial position across Slit (Pixel No.)', fontsize=16)
#cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
#cbar.set_label('Uncalibrated Intensity (CCD Counts)', fontsize=20)
#%%
plt.figure()
Keck_Tests = Keck_Data_Total[0:228, 0:230]
Keck_Tests1 = np.add(Keck_Tests, 85.47336196899414)
Keck_Tests2 = np.true_divide(Keck_Tests1, 141.00852584838867)
plt.axhline(79, color='r', ls='--')
plt.axhline(155, color='b', ls='--')
#plt.imshow(Keck_Data_Total, cmap='gist_gray')
plt.imshow(Keck_Tests2, cmap='gist_gray')
plt.xlabel('Wavelength Axis Column Position (0.1" per pixel)', fontsize=20)
plt.xticks(fontsize=15)
#plt.xlabel(r'Wavelength ($\mu$m) +- 0.0017 $\mu$m', fontsize=15)
#label_x = 0, 200, 400, 600, 800, 1000
#plt.xticks(label_x, ('3.9447', '3.9564', '3.9680', '3.9763', '3.9912', '4.0028'), fontsize=15)
plt.ylabel('Spatial Axis Row Position (0.17" per pixel)', fontsize=20)
plt.yticks(fontsize=15)
#plt.axvline(142, color='blue', ls='--')
#plt.axhline(40, color='r', ls='--')
#plt.title(r'Infrared Uranus observations with NIRSPEC on $5^{th}$ September 2006, 07:25 to 15:24 UTC, between 3.9447$\mu$m and 4.0028$\mu$m ', fontsize=18)
cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
cbar.ax.tick_params(labelsize=15)
cbar.set_label('Normalised Detector Counts', fontsize=20)