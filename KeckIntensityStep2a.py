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

for n in range(ABsubs): #This for loop uses the A - B - B + A and adds them into a list Keck_DataABBA before creating a total spectra 
    image_dataSUB = ((Keck_Data[s]/60 - Cal_Flats) - (Keck_Data[(s+1)]/60 - Cal_Flats) - (Keck_Data[(s+2)]/60 - Cal_Flats) + (Keck_Data[(s+3)]/60 - Cal_Flats))/4
    Keck_DataABBA.append(image_dataSUB)
    s += 4
    Keck_Data_Total += Keck_DataABBA[n]
    filename = 'KeckDataABBASet' + str(n) + '.txt'
    np.savetxt(filename, Keck_DataABBA[n])

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
#%%
#### Fit a Gaussin plot over the H3+ Q(1,0) line in the first ABBA method ####

# Now match a gaussian profile across all 5 lines to find the intensity, and width of the slit
def fit_func(x, a0, a1, a2, a3, a4, a5): # First write a guassian function credit to pen and pants IDL's Gaussfit in Python
    z = (x - a1) / a2
    y = a0 * np.exp(-z**2 / a2) + a3 + a4 * x + a5 * x**2
    return y

Line = 1
X = np.arange(400)
X2 = np.arange(300)
X3 = np.arange(100)

Keck_Data_NTotalQ1 = np.zeros((image_data1.shape[1]))
Keck_Data_PTotalQ1 = np.zeros((image_data1.shape[1]))
    
if Line == 1:
    b = 50
    c = 125
    for n in range(60):
        Keck_Data_NTotalQ1 += Keck_Data_Total[(b),:]
        Keck_Data_PTotalQ1 += Keck_Data_Total[(c),:]
        b += 1
        c += 1
    Keck_Data_NTotal = Keck_Data_NTotalQ1 / 60
    Keck_Data_PTotal = Keck_Data_PTotalQ1 / 60
    Keck_DataQ1N = Keck_Data_NTotal[0:400]
    Keck_DataQ1P = Keck_Data_PTotal[0:400]
    parameters1, covariance1 = curve_fit(fit_func, X, Keck_DataQ1N, p0=[23.2, 1.5, 142, -5, 0, 0])
    Q1NFitData = fit_func(X, *parameters1)
    Assist00 = np.array([-parameters1[0], parameters1[1], parameters1[2], parameters1[3], parameters1[4], parameters1[5]])
    parameters2, covariance2 = curve_fit(fit_func, X, Keck_DataQ1P, p0=[Assist00])
    Assist01 = np.array([parameters1[0], parameters1[1], parameters1[2], parameters1[3], parameters1[4], parameters1[5]])
    Q1PFitData = fit_func(X, *parameters2)
    plt.figure()
    #plt.title(r'Total $Q(1,0^{-})$ emission line flux Intensity against Wavelength', fontsize=30)
    plt.ylabel('Normalised Detector Counts', fontsize=20)
    #plt.ylabel('Uncalibrated Intensity (CCD Counts)', fontsize=20)
    plt.xlabel(r'Wavelength Axis Row Position (1.7 x 10$^{-3}$$\mu$m per pixel)', fontsize=20)
    #label_x = 0, 100, 200, 300, 400
    #plt.xticks(label_x, ('3.9448', '3.9506', '3.9566', '3.9624', '3.9682'), fontsize=15)
    plt.xlim(100, 180)
    plt.ylim(-1.5, 1.5)
    plt.grid(color='k', linestyle='--', linewidth=0.5)
    Keck_DataQ1N = np.add(Keck_DataQ1N, 5.0)
    Keck_DataQ1P = np.add(Keck_DataQ1P, 5.0)
    Keck_DataQ1N = np.true_divide(Keck_DataQ1N, 28.23770955403646)
    Keck_DataQ1P = np.true_divide(Keck_DataQ1P, 33.35024744669597)
    Q1NFitData = np.add(Q1NFitData, 5.0)
    Q1PFitData = np.add(Q1PFitData, 5.0)
    Q1NFitData = np.true_divide(Q1NFitData, 28.23770955403646)
    Q1PFitData = np.true_divide(Q1PFitData, 33.35024744669597)
    plt.plot(X, Keck_DataQ1N, 'k.', X, Q1NFitData, 'r-', linewidth=3)
    plt.plot(X, Keck_DataQ1P, 'k.', X, Q1PFitData, 'b-', linewidth=3)
    plt.yticks(fontsize=15)
    plt.xticks(fontsize=15)
#    print('The pixel position of the Q1 Negative Gaussian Peak is' + ' ' + str(parameters1[1]))
#    print('The pixel width of the Q1 Negative Gaussian fit is' + ' ' + str(parameters1[2]))
#    print('The pixel position of the Q1 Positive Gaussian Peak is' + ' ' + str(parameters2[1]))
#    print('The pixel width of the Q1 Positive Gaussian fit is' + ' ' + str(parameters2[2]))
    Line = 2

if Line == 2:
    Keck_DataQ2N = Keck_Data_NTotal[300:600]
    Keck_DataQ2P = Keck_Data_PTotal[300:600]
    parameters3, covariance3 = curve_fit(fit_func, X2, Keck_DataQ2N, p0=[4.1, 1.47, 151, -5, -0.001, 0])
    Q2NFitData = fit_func(X2, *parameters3)
    Assist0 = np.array([-20, 1.5, 151, -6, 0.001, 0]) #Here the curvefit program struggles to fit the curve so, if we inverse the curve found from the negative and use this as a start for the positive the program is able to fit it
    parameters4, covariance4 = curve_fit(fit_func, X2, Keck_DataQ2P, p0=Assist0)
    Q2PFitData = fit_func(X2, *parameters4)
    plt.figure()
    plt.title(r'$Q(2,0^{-})$ emission line Intensity against Wavelength', fontsize=30)
    plt.ylabel('Uncalibrated Intensity (CCD Counts)', fontsize=20)
    plt.xlabel(r'Wavelength ($\mu$m)', fontsize=20)
    #label_x = 0, 100, 200, 300
    #plt.xticks(label_x, ('3.9625', '3.9685', '3.9745', '3.9805'), fontsize=15)
    #plt.ylim(-1500, 3000)
#    Keck_DataQ2N = np.add(Keck_DataQ2N, 85.47336196899414)
    plt.plot(X2, Keck_DataQ2N, 'ko', X2, Q2NFitData, 'm-', linewidth=3)
    plt.plot(X2, Keck_DataQ2P, 'bo', X2, Q2PFitData, 'r-', linewidth=3)
#    print(' ')
#    print('The pixel position of the Q2 Negative Gaussian Peak is' + ' ' + str(parameters3[1]+300))
#    print('The pixel width of the Q2 Negative Gaussian fit is' + ' ' + str(parameters3[2]))
#    print('The pixel position of the Q2 Positive Gaussian Peak is' + ' ' + str(parameters4[1]+300))
#    print('The pixel width of the Q2 Positive Gaussian fit is' + ' ' + str(parameters4[2]))
    Line = 3

if Line == 3:
    Keck_DataQ3N = Keck_Data_NTotal[650:750]
    Keck_DataQ3P = Keck_Data_PTotal[650:750]
    Assist2 = np.array([parameters2[0], parameters1[1], parameters2[2], parameters2[3], parameters2[4], parameters2[5]])
    parameters6, covariance6 = curve_fit(fit_func, X3, Keck_DataQ3P, p0=[-46.5, 1.5, 47, -5, 0, 0])
    Q3PFitData = fit_func(X3, *parameters6)
    Assist1 = np.array([-parameters6[0], parameters6[1], parameters6[2], parameters6[3], parameters6[4], parameters6[5]])
    parameters5, covariance5 = curve_fit(fit_func, X3, Keck_DataQ3N, p0=[Assist1])
    Q3NFitData = fit_func(X3, *parameters5)
    plt.figure()
    plt.title(r'$H_{3}^{+}$ Singular Horizontal Cut across the Spectrograph with Intensity against Wavelength', fontsize=30)
    plt.ylabel('Uncalibrated Intensity (CCD Counts)', fontsize=20)
    plt.xlabel(r'Wavelength ($\mu$m)', fontsize=20)
   #label_x = 0, 50, 150, 300, 350
    #plt.xticks(label_x, ('3.9775', '3.9805', '3.9865', '3.9925', '3.9955'), fontsize=15)
    #plt.ylim(-1500, 3000)
    plt.plot(X3, Keck_DataQ3N, 'ko', X3, Q3NFitData, 'm-', linewidth=3)
    plt.plot(X3, Keck_DataQ3P, 'bo', X3, Q3PFitData, 'r-', linewidth=3)
    plt.grid(color='k', linestyle='--', linewidth=0.5)
#    print(' ')
#    print('The pixel position of the Q3 Negative Gaussian Peak is' + ' ' + str(parameters5[1]+650))
#    print('The pixel width of the Q3 Negative Gaussian fit is' + ' ' + str(parameters5[2]))
#    print('The pixel position of the Q3 Positive Gaussian Peak is' + ' ' + str(parameters6[1]+650))
#    print('The pixel width of the Q3 Positive Gaussian fit is' + ' ' + str(parameters6[2]))
    Line = 4

if Line == 4:
    Keck_DataQ4N = Keck_Data_NTotal[570:870]
    Keck_DataQ4P = Keck_Data_PTotal[570:870]
    Assist3 = np.array([parameters3[0], parameters3[1], parameters3[2], parameters3[3], parameters3[4], parameters3[5]])
    parameters7, covariance7 = curve_fit(fit_func, X2, Keck_DataQ4N, p0=Assist3)
    Q4NFitData = fit_func(X2, *parameters7)
    Assist4 = np.array([parameters4[0], parameters7[1], parameters4[2], parameters4[3], parameters4[4], parameters4[5]])
    parameters8, covariance8 = curve_fit(fit_func, X2, Keck_DataQ4P, p0=Assist4)
    Q4PFitData = fit_func(X2, *parameters8)
    plt.figure()
    plt.title('4th emission peaks of both negative and positive intensity')
    plt.ylabel('Uncalibrated Intensity (CCD Counts)', fontsize=20)
    plt.xlabel(r'Wavelength ($\mu$m)', fontsize=20)
    #label_x = 30, 130, 230, 280
    #plt.xticks(label_x, ('3.9805', '3.9865', '3.9925', '3.9955'), fontsize=15)
    plt.plot(X2, Keck_DataQ4N, 'ko', X2, Q4NFitData, 'm-', linewidth=3)
    plt.plot(X2, Keck_DataQ4P, 'bo', X2, Q4PFitData, 'r-', linewidth=3)
    #plt.ylim(-1500, 3000)
#    print(' ')
#    print('The pixel position of the Q4 Negative Gaussian Peak is' + ' ' + str(parameters7[1]+570))
#    print('The pixel width of the Q4 Negative Gaussian fit is' + ' ' + str(parameters7[2]))
#    print('The pixel position of the Q4 Positive Gaussian Peak is' + ' ' + str(parameters8[1]+570))
#    print('The pixel width of the Q4 Positive Gaussian fit is' + ' ' + str(parameters8[2]))
    Line = 5
    
if Line == 5:
    Keck_DataQ5N = Keck_Data_NTotal[700:1000]
    Keck_DataQ5P = Keck_Data_PTotal[700:1000]
    Assist5 = np.array([parameters3[0], parameters3[1], parameters3[2], parameters3[3], parameters3[4], parameters3[5]])
    parameters9, covariance9 = curve_fit(fit_func, X2, Keck_DataQ5N, p0=Assist5)
    Q5NFitData = fit_func(X2, *parameters9)
    Assist6 = np.array([-parameters9[0], parameters9[1], parameters9[2], parameters9[3], parameters9[4], parameters9[5]])
    parameters10, covariance10 = curve_fit(fit_func, X2, Keck_DataQ5P, p0=Assist6)
    Q5PFitData = fit_func(X2, *parameters10)
    plt.figure()
    plt.ylabel('Uncalibrated Intensity (CCD Counts)', fontsize=20)
    plt.xlabel(r'Wavelength ($\mu$m)', fontsize=20)
    #label_x = 0, 100, 200, 300
    #plt.xticks(label_x, ('3.9865', '3.9925', '3.9985', '4.0045'), fontsize=15)
    #plt.ylim(-1500, 3000)
    plt.plot(X2, Keck_DataQ5N, 'ko', X2, Q5NFitData, 'm-', linewidth=3)
    plt.plot(X2, Keck_DataQ5P, 'bo', X2, Q5PFitData, 'r-', linewidth=3)
    plt.title('5th emission peaks of both negative and positive intensity')
#    print(' ')
#    print('The pixel position of the Q5 Negative Gaussian Peak is' + ' ' + str(parameters9[1]+700))
#    print('The pixel width of the Q5 Negative Gaussian fit is' + ' ' + str(parameters9[2]))
#    print('The pixel position of the Q5 Positive Gaussian Peak is' + ' ' + str(parameters10[1]+700))
#    print('The pixel width of the Q5 Positive Gaussian fit is' + ' ' + str(parameters10[2]))