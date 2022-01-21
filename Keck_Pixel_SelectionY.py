# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:59:46 2020

@author: Emma 'Amelia'
"""
#First we're going to sort the data as is suggested in the obs log for the day, i.e. sort the data into 3 sections ensuring to get rid of faulty data
import numpy as np
import more_itertools as mit
import matplotlib.pyplot as plt
from astropy.io import fits #import the relevant directories to read a fits file from your directory and plot it
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

#plt.figure()
#plt.imshow(Keck_Data_Total, cmap='gist_gray')
#plt.xlabel(r'Wavelength ($\mu$m) +- 0.0017 $\mu$m', fontsize=15)
#label_x = 0, 200, 400, 600, 800, 1000
#plt.xticks(label_x, ('3.9447', '3.9564', '3.9680', '3.9763', '3.9912', '4.0028'), fontsize=15)
#plt.ylabel('Spatial position across Slit (Pixel No.)', fontsize=15)
#plt.axvline(142, color='blue', ls='--')
#plt.axhline(40, color='r', ls='--')
#plt.title(r'Infrared Uranus observations with NIRSPEC on $5^{th}$ September 2006, 07:25 to 15:24 UTC, between 3.9447$\mu$m and 4.0028$\mu$m ', fontsize=18)
#cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
#cbar.set_label('Uncalibrated Intensity (CCD Counts)', fontsize=18)

#%% Now we have our data sets which means we can start deciding where to take the middle point for our slit to set up for h3ppy
#First pull up our first ABBA set and select noise 

#plt.figure()
#plt.imshow(Keck_DataABBA[0], cmap='gist_gray')
#plt.xlabel(r'Wavelength ($\mu$m) +- 0.0017 $\mu$m', fontsize=15)
#label_x = 0, 200, 400, 600, 800, 1000
#plt.xticks(label_x, ('3.9447', '3.9564', '3.9680', '3.9763', '3.9912', '4.0028'), fontsize=15)
#plt.ylabel('Spatial position across Slit (Pixel No.)', fontsize=15)
#plt.axvline(142, color='blue', ls='--')
#plt.axhline(40, color='r', ls='--')
#plt.title(r'Infrared Uranus observations with NIRSPEC on $5^{th}$ September 2006, 07:25 to 15:24 UTC, between 3.9447$\mu$m and 4.0028$\mu$m ', fontsize=18)
#cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
#cbar.set_label('Uncalibrated Intensity (CCD Counts)', fontsize=18)

#N = Keck_DataABBA[3]
#Noise = N[70:150, 500:600]
#Noise_Mean = np.mean(Noise)
#Noise_Std = np.std(Noise)
#Noise_Max = Noise_Mean + 1*Noise_Std
#Noise_Min = Noise_Mean - 1*Noise_Std

#Now we want to go through around 142 so 120 to 160 in y and check for pixels above the Noise Int and write these down
Slit_NumbersP = []
Slit_NumbersN = []
Mid_PointsP = []
Mid_PointsN = []

#DATA = Keck_DataABBA[3]
#DATA_Line = DATA[:, 141]
#for ii in range(150):
#    DATA_Pixel = DATA_Line[ii+50]
#    if DATA_Pixel > Noise_Max:
#        Pixel_NumbersP.append(ii+50)
#    elif DATA_Pixel < Noise_Min:
#        Pixel_NumbersN.append(ii+50)
#    else:
#        pass
#GroupsP = [list(group) for group in mit.consecutive_groups(Pixel_NumbersP)]
#Slit_NosP = max(GroupsP, key=len)
#Start_PointP = min(Slit_NosP)
#Finish_PointP = max(Slit_NosP)
#Slit_NumbersP.append(Start_PointP)
#Slit_NumbersP.append(Finish_PointP)
#GroupsN = [list(group) for group in mit.consecutive_groups(Pixel_NumbersN)]
#Slit_NosN = max(GroupsN, key=len)
#Start_PointN = min(Slit_NosN)
#Finish_PointN = max(Slit_NosN)
#Slit_NumbersN.append(Start_PointN)
#Slit_NumbersN.append(Finish_PointN)

for n in range(54):
    DATA = Keck_DataABBA[n]
    Noise = DATA[75:150, 500:600]
    Noise_Mean = np.mean(Noise)
    Noise_Std = np.std(Noise)
    Noise_Max = Noise_Mean + 2*Noise_Std
    Noise_Min = Noise_Mean - 2*Noise_Std
    for i in range(3):
        Pixel_NumbersP = []
        Pixel_NumbersN = []
        Start = 141
        Line_No = Start + i
        DATA_Line = DATA[:, Line_No]
        for ii in range(150):
            DATA_Pixel = DATA_Line[ii+50]
            if DATA_Pixel > Noise_Max:
                Pixel_NumbersP.append(ii+50)
            elif DATA_Pixel < Noise_Min:
                Pixel_NumbersN.append(ii+50)
            else:
                pass
        GroupsP = [list(group) for group in mit.consecutive_groups(Pixel_NumbersP)]
        Slit_NosP = max(GroupsP, key=len)
        Start_PointP = min(Slit_NosP)
        Finish_PointP = max(Slit_NosP)
        Slit_NumbersP.append(Start_PointP)
        Slit_NumbersP.append(Finish_PointP)
        MidsP = int((Finish_PointP - Start_PointP)/2) + Start_PointP
        Mid_PointsP.append(MidsP)
        GroupsN = [list(group) for group in mit.consecutive_groups(Pixel_NumbersN)]
        Slit_NosN = max(GroupsN, key=len)
        Start_PointN = min(Slit_NosN)
        Finish_PointN = max(Slit_NosN)
        Slit_NumbersN.append(Start_PointN)
        Slit_NumbersN.append(Finish_PointN)
        MidsN = int((Finish_PointN - Start_PointN)/2) + Start_PointN
        Mid_PointsN.append(MidsN)
        
#Now the Middle point of every point across the slit is known for the observation, the data from Uranus can be taken out and used in the further investigations and hence the error in these can be found too
i = 0
Mid_PointP = []
Mid_PointN = []
Std_Mid_PointP = []
Std_Mid_PointN = []

for n in range(int(len(Mid_PointsP)/3)):
    i = n*3
    Mid_PointP.append(int(np.mean(Mid_PointsP[i:i+3])))
    Std_Mid_PointP.append(np.std(Mid_PointsP[i:i+3]))
    Mid_PointN.append(int(np.mean(Mid_PointsN[i:i+3])))
    Std_Mid_PointN.append(np.std(Mid_PointsN[i:i+3]))

#Now we need to find out what the mean standard deviation is
Mean_Std_Pix = int(np.mean(Std_Mid_PointP + Std_Mid_PointN))

#Need to Zip one array after the other (Mid_PointP and Mid_PointN)
Mid_Points = []

for n in range(int(len(Mid_PointP))):
    Mid_Points.append(Mid_PointP[n])
    Mid_Points.append(Mid_PointN[n])
    
np.savetxt("MiddlePointData11.csv", Mid_Points, delimiter=",")
