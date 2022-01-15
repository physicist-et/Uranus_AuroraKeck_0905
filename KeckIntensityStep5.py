# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:35:14 2020

@author: emt18
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from Uranus_TimeToLongv2 import Limits
from KeckIntensityStep2a import Keck_DataABBA
from KeckDataReductionStep1 import Fc_HD215
from lmfit import Model
from types import SimpleNamespace
from matplotlib import cm
from LOSPractice import LOSc_array

# Put the Negative and Positive Emissions together and then Gaussian fit over the emission to find the Intensity
# Write out the Gaussian progfile for Python this will need some inital values to assist in the fitting
def gaussian_fit(x, a0, a1, a2, a3, a4, a5):
    z = (x - a1) / a2
    y = a0 * np.exp(-z**2 / a2) + a3 + a4 * x + a5 * x**2
    return y

LOS_adjust = []

for i in range(22):
    LOS_adj = (LOSc_array[i]+LOSc_array[i+1])/2
    LOS_adjust.append(LOS_adj)
    
#%% Now we define the space of Keck Data for the map

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
    ABBAN = ABBAN*-1
    ABBAP = ABBA[int(Start_Points[i+1]):int(Finish_Points[i+1]), w1:w2] 
    ABBAT = ABBAN+ABBAP
    ABBAalpha.append(ABBAT/2)
    i += 2

plt.figure()
plt.imshow(ABBAalpha[0])
#Here we should have an array of 28 arrays of 54 (Y height) by 400 (X height) which we can then Gaussian fit in the next segment
#%% Now taking these we will run Gaussian's over all 54 rows to find A0 values which in turn will be saved

XX = np.arange(300)
X = np.arange(100)
AVALS = []
COVALS = []
SDs = []

ABBAi = []
TLDR = []
i = 0

#for xx in range(54):
#    ABBAi = ABBAalpha[xx]
#    for i in range(22):
#        ABBAt = -1*ABBAi[i,140:145]
#        ABBATLDR = np.sum(ABBAt)
#        TLDR.append(ABBATLDR)

#Ints = np.reshape(TLDR, (28,54))
#IntS = np.transpose(Ints)

#plt.figure()
#plt.imshow(-1*IntS, cmap='binary')
#plt.xlabel('ABBA set No. (Sets)')

#plt.xticks(np.arange(-0.5,28, step=1))
#plt.ylabel('Spatial position across Uranus (Pixel No.)')
#plt.hlines(9.5, xmin=-0.5, xmax=27.5, color='c', linewidth=4)
#plt.hlines(43.5, xmin=-0.5, xmax=27.5, color='c', linewidth=4)
#cbar = plt.colorbar() #Prints out an image in greyscale of the fits file
#cbar.set_label('Uncalibrated Intensity (CCD Counts)')

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
#from AvParams import AVALSAv
iiii = 0
for xx in range(54):
    ABBAi = ABBAalpha[xx]
    for i in range(22):
        ABBAt = -1*ABBAi[i,:]
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
        if i == 11 and xx == 20:
            pass
            #plt.plot(np.arange(1024), ABBAt)
            #print(A0_Q1)
                
    print('ABBA Set ' + str(xx) + ' completed!')

Q1_IntErr = []
Q3_IntErr = []

for o in range(1188):
    Q1IntErr = INTSQ1[o]*np.sqrt((Err_A0_Q1[o]/A0_Q1[o])**2 + (Err_A2_Q1[o]/A2_Q1[o])**2)
    Q1_IntErr.append(Q1IntErr)
    Q3IntErr = INTSQ3[o]*np.sqrt((Err_A0_Q3[o]/A0_Q3[o])**2 + (Err_A2_Q3[o]/A2_Q3[o])**2)
    Q3_IntErr.append(Q3IntErr)
    
T_Int_Err = np.sqrt((np.nanmean(Q1_IntErr)**2) + (np.nanmean(Q3_IntErr)**2))
print('Total Q1 + Q3 Err is =' + str(T_Int_Err*10**6))   

#%% Next we sit up the intensities from the Gaussian plots to produce 1 by 54 stripes of the intensity over the 28 intervals of time
INTSQ1 = np.transpose(np.reshape(INTSQ1, (54, 22)))
INTSQ3 = np.transpose(np.reshape(INTSQ3, (54, 22)))

Set1_INTSQ1 = INTSQ1[:, 0:27]
Set2_INTSQ1_OffSlitB = np.flipud(INTSQ1[:, 27:36])
Set2_INTSQ1 = np.flipud(INTSQ1[:, 36:55])

Off_Slit_Time = np.zeros((22,9))
New_INTSQ1 = np.hstack((Set1_INTSQ1, Off_Slit_Time))
New_INTSQ1 = np.hstack((New_INTSQ1, Set2_INTSQ1))
#New_INTSQ1[New_INTSQ1 == 0] = np.nan

Set1_INTSQ3 = INTSQ3[:, 0:27] #28
Set2_INTSQ3_OffSlitB = np.flipud(INTSQ3[:, 27:36]) #8
Set2_INTSQ3 = np.flipud(INTSQ3[:, 36:55]) #17

Off_Slit_Time = np.zeros((22,9))
New_INTSQ3 = np.hstack((Set1_INTSQ3, Off_Slit_Time))
New_INTSQ3 = np.hstack((New_INTSQ3, Set2_INTSQ3))
#New_INTSQ3[New_INTSQ3 == 0] = np.nan

#Need to flip the Set 2 Int values to get the final image
plt.figure()
plt.imshow(New_INTSQ1*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q1_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(1,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
#plt.xticks(np.arange(13), TIME)

plt.figure()
plt.imshow(New_INTSQ3*(10**6), cmap=cm.nipy_spectral)
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}Wm^{-2}sr^{-1}$) +- ' + str("{:.2f}".format(round(np.nanmean(Q3_IntErr)*(10**6), 2))) + ' ${\mu}Wm^{-2}sr^{-1}$', fontsize=17.5) 
plt.title(r'$H_{3}^{+}$ $Q(3,0^{-})$ Intensity of Uranus observations from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 20)
plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
plt.ylabel('Latitude across Uranus (ULS) (Degree +- ???)', fontsize=17.5, labelpad=9)
    
#%% Now we will take the intensities found and produce 28 seperate graphs which should show the intensity over the surface of Uranus's ionosphere

r_planet = 11.491436449930903
LatPointsT = int(np.arcsin(11/r_planet)*(180/np.pi)*(10*2) -1)
Pix_Lat11N = int(82.58874251245483*10)
Pix_Lat10N = int(67.73782306590236*10)
Pix_Lat9N = int(58.162143303725436*10)
Pix_Lat8N = int(50.368295310014865*10)
Pix_Lat7N = int(43.52739307923493*10)
Pix_Lat6N = int(37.283511974413145*10)
Pix_Lat5N = int(31.443001218995096*10)
Pix_Lat4N = int(25.884673499120684*10)
Pix_Lat3N = int(20.524728424162266*10)
Pix_Lat2N = int(15.300307115229453*10)
Pix_Lat1N = int(10.16066558783987*10)
Pix_Lat0 = int(5.061820951538881*10)
Pix_Lat1S = int(-0.03716781215110235*10)
Pix_Lat2S = int(-5.177255955909495*10)
Pix_Lat3S = int(-10.40247273797995*10)
Pix_Lat4S = int(-15.7636535139867*10)
Pix_Lat5S = int(-21.323822912428657*10)
Pix_Lat6S = int(-27.16708756854347*10)
Pix_Lat7S = int(-33.415244212433485*10)
Pix_Lat8S = int(-40.26332537997243*10)
Pix_Lat9S = int(-48.07115799215469*10)
Pix_Lat10S = int(-57.68450927583689*10)
Pix_Lat11S = int(-72.93827724669491*10)
LatPointsT = (Pix_Lat11N - Pix_Lat11S + 1)

Filler = np.zeros(1555)

#%% Now to construct the latitude and longitudinal maps
e = 0
for ii in range(1237):
    if ii == 0:
        d = 0
        for iii in range(LatPointsT):
            vi = Pix_Lat11N - iii     
            if vi == Pix_Lat11N:
                Tests = New_INTSQ1[21,d]
                Tests3 = New_INTSQ3[21,d]
            elif vi < Pix_Lat11N and vi > Pix_Lat10N:
                Tests = np.append(Tests, New_INTSQ1[21,d])
                Tests3 = np.append(Tests3,New_INTSQ3[21,d])                
            elif vi <= Pix_Lat10N and vi > Pix_Lat9N:
                Tests = np.append(Tests, New_INTSQ1[20,d])
                Tests3 = np.append(Tests3,New_INTSQ3[20,d])
            elif vi <= Pix_Lat9N and vi > Pix_Lat8N:
                Tests = np.append(Tests, New_INTSQ1[19,d])
                Tests3 = np.append(Tests3, New_INTSQ3[19,d])
            elif vi <= Pix_Lat8N and vi > Pix_Lat7N:
                Tests = np.append(Tests, New_INTSQ1[18,d])
                Tests3 = np.append(Tests3, New_INTSQ3[18,d])
            elif vi <= Pix_Lat7N and vi > Pix_Lat6N:
                Tests = np.append(Tests, New_INTSQ1[17,d])
                Tests3 = np.append(Tests3, New_INTSQ3[17,d])
            elif vi <= Pix_Lat6N and vi > Pix_Lat5N:
                Tests = np.append(Tests, New_INTSQ1[16,d])
                Tests3 = np.append(Tests3,New_INTSQ3[16,d])
            elif vi <= Pix_Lat5N and vi > Pix_Lat4N:
                Tests = np.append(Tests, New_INTSQ1[15,d])
                Tests3 = np.append(Tests3, New_INTSQ3[15,d])
            elif vi <= Pix_Lat4N and vi > Pix_Lat3N:
                Tests = np.append(Tests, New_INTSQ1[14,d])
                Tests3 = np.append(Tests3, New_INTSQ3[14,d])
            elif vi <= Pix_Lat3N and vi > Pix_Lat2N:
                Tests = np.append(Tests, New_INTSQ1[13,d])
                Tests3 = np.append(Tests3, New_INTSQ3[13,d])
            elif vi <= Pix_Lat2N and vi > Pix_Lat1N:
                Tests = np.append(Tests, New_INTSQ1[12,d])
                Tests3 = np.append(Tests3,New_INTSQ3[12,d])
            elif vi <= Pix_Lat1N and vi > Pix_Lat0:
                Tests = np.append(Tests, New_INTSQ1[11,d])
                Tests3 = np.append(Tests3, New_INTSQ3[11,d])
            elif vi <= Pix_Lat0 and vi > Pix_Lat1S:
                Tests = np.append(Tests, New_INTSQ1[10,d])
                Tests3 = np.append(Tests3, New_INTSQ3[10,d])
            elif vi <= Pix_Lat1S and vi > Pix_Lat2S:
                Tests = np.append(Tests, New_INTSQ1[9,d])
                Tests3 = np.append(Tests3, New_INTSQ3[9,d])
            elif vi <= Pix_Lat2S and vi > Pix_Lat3S:
                Tests = np.append(Tests, New_INTSQ1[8,d])
                Tests3 = np.append(Tests3, New_INTSQ3[8,d])
            elif vi <= Pix_Lat3S and vi > Pix_Lat4S:
                Tests = np.append(Tests, New_INTSQ1[7,d])
                Tests3 = np.append(Tests3, New_INTSQ3[7,d])
            elif vi <= Pix_Lat4S and vi > Pix_Lat5S:
                Tests = np.append(Tests, New_INTSQ1[6,d])
                Tests3 = np.append(Tests3, New_INTSQ3[6,d])
            elif vi <= Pix_Lat5S and vi > Pix_Lat6S:
                Tests = np.append(Tests, New_INTSQ1[5,d])
                Tests3 = np.append(Tests3, New_INTSQ3[5,d])
            elif vi <= Pix_Lat6S and vi > Pix_Lat7S:
                Tests = np.append(Tests, New_INTSQ1[4,d])
                Tests3 = np.append(Tests3, New_INTSQ3[4,d])
            elif vi <= Pix_Lat7S and vi > Pix_Lat8S:
                Tests = np.append(Tests, New_INTSQ1[3,d])
                Tests3 = np.append(Tests3, New_INTSQ3[3,d])
            elif vi <= Pix_Lat8S and vi > Pix_Lat9S:
                Tests = np.append(Tests, New_INTSQ1[2,d])
                Tests3 = np.append(Tests3, New_INTSQ3[2,d])
            elif vi <= Pix_Lat9S and vi > Pix_Lat10S:
                Tests = np.append(Tests, New_INTSQ1[1,d])
                Tests3 = np.append(Tests3, New_INTSQ3[1,d])
            elif vi <= Pix_Lat10S and vi >= Pix_Lat11S:
                Tests = np.append(Tests, New_INTSQ1[0,d])
                Tests3 = np.append(Tests3, New_INTSQ3[0,d])
        Test_1 = np.array(Tests)
        Test_3 = np.array(Tests3)
    elif ii > Limits[e] and ii <= Limits[e+2]:
        for iii in range(LatPointsT):
            vi = Pix_Lat11N - iii     
            if vi == Pix_Lat11N:
                Tests = New_INTSQ1[21,d]
                Tests3 = New_INTSQ3[21,d]
            elif vi < Pix_Lat11N and vi > Pix_Lat10N:
                Tests = np.append(Tests, New_INTSQ1[21,d])
                Tests3 = np.append(Tests3,New_INTSQ3[21,d])                
            elif vi <= Pix_Lat10N and vi > Pix_Lat9N:
                Tests = np.append(Tests, New_INTSQ1[20,d])
                Tests3 = np.append(Tests3,New_INTSQ3[20,d])
            elif vi <= Pix_Lat9N and vi > Pix_Lat8N:
                Tests = np.append(Tests, New_INTSQ1[19,d])
                Tests3 = np.append(Tests3, New_INTSQ3[19,d])
            elif vi <= Pix_Lat8N and vi > Pix_Lat7N:
                Tests = np.append(Tests, New_INTSQ1[18,d])
                Tests3 = np.append(Tests3, New_INTSQ3[18,d])
            elif vi <= Pix_Lat7N and vi > Pix_Lat6N:
                Tests = np.append(Tests, New_INTSQ1[17,d])
                Tests3 = np.append(Tests3, New_INTSQ3[17,d])
            elif vi <= Pix_Lat6N and vi > Pix_Lat5N:
                Tests = np.append(Tests, New_INTSQ1[16,d])
                Tests3 = np.append(Tests3,New_INTSQ3[16,d])
            elif vi <= Pix_Lat5N and vi > Pix_Lat4N:
                Tests = np.append(Tests, New_INTSQ1[15,d])
                Tests3 = np.append(Tests3, New_INTSQ3[15,d])
            elif vi <= Pix_Lat4N and vi > Pix_Lat3N:
                Tests = np.append(Tests, New_INTSQ1[14,d])
                Tests3 = np.append(Tests3, New_INTSQ3[14,d])
            elif vi <= Pix_Lat3N and vi > Pix_Lat2N:
                Tests = np.append(Tests, New_INTSQ1[13,d])
                Tests3 = np.append(Tests3, New_INTSQ3[13,d])
            elif vi <= Pix_Lat2N and vi > Pix_Lat1N:
                Tests = np.append(Tests, New_INTSQ1[12,d])
                Tests3 = np.append(Tests3,New_INTSQ3[12,d])
            elif vi <= Pix_Lat1N and vi > Pix_Lat0:
                Tests = np.append(Tests, New_INTSQ1[11,d])
                Tests3 = np.append(Tests3, New_INTSQ3[11,d])
            elif vi <= Pix_Lat0 and vi > Pix_Lat1S:
                Tests = np.append(Tests, New_INTSQ1[10,d])
                Tests3 = np.append(Tests3, New_INTSQ3[10,d])
            elif vi <= Pix_Lat1S and vi > Pix_Lat2S:
                Tests = np.append(Tests, New_INTSQ1[9,d])
                Tests3 = np.append(Tests3, New_INTSQ3[9,d])
            elif vi <= Pix_Lat2S and vi > Pix_Lat3S:
                Tests = np.append(Tests, New_INTSQ1[8,d])
                Tests3 = np.append(Tests3, New_INTSQ3[8,d])
            elif vi <= Pix_Lat3S and vi > Pix_Lat4S:
                Tests = np.append(Tests, New_INTSQ1[7,d])
                Tests3 = np.append(Tests3, New_INTSQ3[7,d])
            elif vi <= Pix_Lat4S and vi > Pix_Lat5S:
                Tests = np.append(Tests, New_INTSQ1[6,d])
                Tests3 = np.append(Tests3, New_INTSQ3[6,d])
            elif vi <= Pix_Lat5S and vi > Pix_Lat6S:
                Tests = np.append(Tests, New_INTSQ1[5,d])
                Tests3 = np.append(Tests3, New_INTSQ3[5,d])
            elif vi <= Pix_Lat6S and vi > Pix_Lat7S:
                Tests = np.append(Tests, New_INTSQ1[4,d])
                Tests3 = np.append(Tests3, New_INTSQ3[4,d])
            elif vi <= Pix_Lat7S and vi > Pix_Lat8S:
                Tests = np.append(Tests, New_INTSQ1[3,d])
                Tests3 = np.append(Tests3, New_INTSQ3[3,d])
            elif vi <= Pix_Lat8S and vi > Pix_Lat9S:
                Tests = np.append(Tests, New_INTSQ1[2,d])
                Tests3 = np.append(Tests3, New_INTSQ3[2,d])
            elif vi <= Pix_Lat9S and vi > Pix_Lat10S:
                Tests = np.append(Tests, New_INTSQ1[1,d])
                Tests3 = np.append(Tests3, New_INTSQ3[1,d])
            elif vi <= Pix_Lat10S and vi >= Pix_Lat11S:
                Tests = np.append(Tests, New_INTSQ1[0,d])
                Tests3 = np.append(Tests3, New_INTSQ3[0,d])
        Test_1 = np.hstack((Test_1, Tests))
        Test_3 = np.hstack((Test_3, Tests3))
        if ii == Limits[e+2]:
           e += 2
           d += 1
    else:
        Test_1 = np.hstack((Test_1, Filler))
        Test_3 = np.hstack((Test_3, Filler))
#Can't get Limits and the final 54 sets to match up?
#%% And now to map the map

Mapping_Q1 = np.reshape(Test_1, (1237, 1555))
Mapping_Q1 = Mapping_Q1.transpose()
Mapping_Q1 = np.flipud(Mapping_Q1)
Mapping_Q1[Mapping_Q1 == 0] = np.nan

#To make a standard map we'll add in blank space to create a 180 degree by 180 degree map
Blank = np.zeros((75, 1237))
Blank2 = np.zeros((1801, 563))
Blank3 = np.zeros((171, 1237))
#Blank3 = np.zeros((1800, 1800))
Mapping_Q1 = np.vstack((Blank, Mapping_Q1))
Mapping_Q1 = np.vstack((Mapping_Q1, Blank3))
Mapping_Q1 = np.hstack((Mapping_Q1, Blank2))
#Mapping_Q1 = np.hstack((Mapping_Q1, Blank3))
Mapping_Q1[Mapping_Q1 == 0] = np.nan

plt.figure()
plt.imshow(Mapping_Q1*(10**6), cmap='nipy_spectral')
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(round(np.nanmean(Q1_IntErr)*(10**6), 2))) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=17.5) 
plt.title(r'Intensity of $H_{3}^{+}$ $Q(1,0^{-})$', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
plt.ylabel('Latitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
#plt.xticks(np.arange(0, 1801, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=11)
plt.yticks(np.arange(0, 1801, 300), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=11)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800), 0, 1800, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.hlines((0, 300, 600, 900, 1200, 1500, 1800), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.ylim(1800, 0) #1801, -1
plt.xlim(0, 3601) #0, 3601

Mapping_Q3 = np.reshape(Test_3, (1237, 1555))
Mapping_Q3 = Mapping_Q3.transpose()
Mapping_Q3 = np.flipud(Mapping_Q3)
Mapping_Q3[Mapping_Q3 == 0] = np.nan

#To make a standard map we'll add in blank space to create a 180 degree by 180 degree map
Blank = np.zeros((75, 1237))
Blank2 = np.zeros((1801, 563))
Blank3 = np.zeros((171, 1237))
#Blank3 = np.zeros((1800, 1800))
Mapping_Q3 = np.vstack((Blank, Mapping_Q3))
Mapping_Q3 = np.vstack((Mapping_Q3, Blank3))
Mapping_Q3 = np.hstack((Mapping_Q3, Blank2))
#Mapping_Q1 = np.hstack((Mapping_Q1, Blank3))
Mapping_Q3[Mapping_Q3 == 0] = np.nan

plt.figure()
plt.imshow(Mapping_Q3*(10**6), cmap='nipy_spectral')
cbar = plt.colorbar()
cbar.set_label(r'Intensity (${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$) ' + u'\u00B1' + ' ' + str("{:.2f}".format(round(np.nanmean(Q3_IntErr)*(10**6), 2))) + ' ${\mu}W$ ' + '$m^{-2}$ ' + '$sr^{-1}$', fontsize=17.5) 
plt.title(r'Intensity of $H_{3}^{+}$ $Q(3,0^{-})$', pad = 45, fontsize = 20)
plt.xlabel('Arbitrary Longitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
plt.ylabel('Latitude across Uranus ($^\circ$)', fontsize=17.5, labelpad=11)
#plt.xticks(np.arange(0, 3601, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$', '200$^\circ$', '220$^\circ$', '240$^\circ$', '260$^\circ$', '280$^\circ$', '300$^\circ$', '320$^\circ$', '340$^\circ$', '360$^\circ$'])
plt.xticks(np.arange(0, 1801, 200), ['0$^\circ$', '20$^\circ$', '40$^\circ$', '60$^\circ$', '80$^\circ$', '100$^\circ$', '120$^\circ$', '140$^\circ$', '160$^\circ$', '180$^\circ$'], fontsize=11)
plt.yticks(np.arange(0, 1801, 300), ['90$^\circ$N', '60$^\circ$N', '30$^\circ$N', '0$^\circ$', '30$^\circ$S', '60$^\circ$S', '90$^\circ$S'], fontsize=11)
#plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.vlines((0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800), 0, 1800, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.hlines((0, 300, 600, 900, 1200, 1500, 1800), 0, 3600, colors = 'k', linestyles = 'dotted', alpha = 0.4)
plt.ylim(1800, 0) #1801, -1
plt.xlim(0, 1801) #0, 3601

# =============================================================================
# #%% Now we need to make temperature and column density with h3ppy
# import h3ppy
# # This function sub-divides data centered on a list of wavelengths
# def subdivide(wave, spec, middles, width = 20) : 
#     ret = []
#     for m in middles : 
#         centre = np.abs(wave - m).argmin()
#         for i in range(centre - width, centre + width) : 
#             ret.append(spec[i])
#     return np.array(ret)
# 
# h3p = h3ppy.h3p()
# wave = h3p.wavegen(3.94466192, 4.00463162, 1024)
# spec = ABBAalpha[2]
# spec = -1*spec[9,:]
# centers = [3.953, 3.971, 3.9854]
# cpos = np.arange(3) * 41 + 20
# Temps = []
# T_err = []
# Col_Densities = []
# Col_err = []
# 
# # Create sub-arrays, focusing on where the H3+ lines are
# subspec = subdivide(wave, spec, centers)
# subwave = subdivide(wave, wave, centers)
# 
# # Set the wavelength and the data
# h3p.set(wavelength = subwave, data = subspec, R = 20000, density = 5e15, temperature = 630)
# 
# # Create a x scale for plotting 
# xx      = range(len(subspec))
# 
# # Guess the density and proceed with a five parameter fit
# # =============================================================================
# # h3p.guess_density()
# # =============================================================================
# fit = h3p.fit()
# vars, errs = h3p.get_results()
# 
# # Plot the fit
# fig, ax = plt.subplots()
# ax.plot(xx, subspec * 1e3, '.', label = 'Observation')
# ax.plot(xx, fit * 1e3, label = 'h3ppy H$_3^+$ fit')
# ax.set(xlabel = h3p.xlabel(), ylabel = h3p.ylabel(prefix = 'm'), xticks = cpos)
# ax.set_xticklabels(centers)
# ax.legend(frameon = False)
# # =============================================================================
# =============================================================================
# # Create sub-arrays, focusing on where the H3+ lines are
# subspec = subdivide(wave, spec, centers)
# subwave = subdivide(wave, wave, centers)
# 
# subspecv2 = np.concatenate((np.zeros(15), subspec[15:25]))
# subspecv2 = np.concatenate((subspecv2, np.zeros(30)))
# subspecv2 = np.concatenate((subspecv2, subspec[55:65]))
# subspecv2 = np.concatenate((subspecv2, np.zeros(30)))
# subspecv2 = np.concatenate((subspecv2, subspec[95:105]))
# subspecv2 = np.concatenate((subspecv2, np.zeros(15)))
# 
# # Set the wavelength and the data
# h3p.set(wavelength = subwave, data = subspecv2, R = 20000, density = 5*(10**16))
# 
# # Create a x scale for plotting 
# xx      = range(len(subspecv2))
# 
# # Guess the density and proceed with a five parameter fit
# fit = h3p.fit()
# vars, errs = h3p.get_results()
# 
# # Plot the fit
# fig, ax = plt.subplots()
# ax.plot(xx, subspecv2 * 1e3, '.', label = 'Observation')
# ax.plot(xx, fit * 1e3, label = 'h3ppy H$_3^+$ fit')
# ax.set(xlabel = h3p.xlabel(), ylabel = h3p.ylabel(prefix = 'm'), xticks = cpos)
# ax.set_xticklabels(centers)
# ax.legend(frameon = False)
# =============================================================================

# =============================================================================
# for xxx in range(54):
#     ABBAi = ABBAalpha[xxx]
#     for i in range(22):
#         spec = -1*ABBAi[i,:]
#         # Create sub-arrays, focusing on where the H3+ lines are
#         subspec = subdivide(wave, spec, centers)
#         subwave = subdivide(wave, wave, centers)
# 
#         # Set the wavelength and the data
#         h3p.set(wavelength = subwave, data = subspec, R = 20000, density = 1e16, temperature = 575)
# 
#         # Create a x scale for plotting 
#         xx = range(len(subspec))
# 
#         # Guess the density and proceed with a five parameter fit
#         fit = h3p.fit(verbose = False)
#         vars, errs = h3p.get_results()
#         if vars == False:
#             Temps.append(0)
#             T_err.append(0)
#             Col_Densities.append(0)
#             Col_err.append(0)            
#         else:
#             Temps.append(vars['temperature'])
#             T_err.append(errs['temperature'])
#             Col_Densities.append(vars['density'])
#             Col_err.append(errs['density'])
# =============================================================================


#%% Map these values similar to above

# =============================================================================
# TEMPS = np.transpose(np.reshape(Temps, (54, 22)))
# COLS = np.transpose(np.reshape(Col_Densities, (54, 22)))
# 
# Set1_TEMPS = TEMPS[:, 0:27]
# Set2_TEMPS_OffSlitB = np.flipud(TEMPS[:, 27:36])
# Set2_TEMPS = np.flipud(TEMPS[:, 36:55])
# 
# Off_Slit_Time = np.zeros((22,9))
# New_TEMPS = np.hstack((Set1_TEMPS, Off_Slit_Time))
# New_TEMPS = np.hstack((New_TEMPS, Set2_TEMPS))
# #New_INTSQ1[New_INTSQ1 == 0] = np.nan
# 
# Set1_COLS = COLS[:, 0:28] #28
# Set2_COLS_OffSlitB = np.flipud(COLS[:, 28:36]) #8
# Set2_COLS = np.flipud(COLS[:, 36:55]) #17
# 
# Off_Slit_Time = np.zeros((22,9))
# New_COLS = np.hstack((Set1_COLS, Off_Slit_Time))
# New_COLS = np.hstack((New_COLS, Set2_COLS))
# 
# #Need to flip the Set 2 Int values to get the final image
# plt.figure()
# plt.imshow(New_TEMPS, cmap=cm.coolwarm)
# cbar = plt.colorbar()
# cbar.set_label(r'Temperature (K) +- ' + str(int(np.nanmean(T_err))) + 'K', fontsize=17.5)
# plt.title(r'$H_{3}^{+}$ Rotational Temperatures across Uranus from 07:40 to 13:16 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 22.5)
# plt.xlabel('UTC Time (HH:MM +- 00:02)', fontsize=17.5, labelpad=10)
# plt.ylabel('Spatial position across Uranus (Pixel No. +- 2)', fontsize=17.5, labelpad=9)
# #plt.xticks(np.arange(13), TIME)
# #plt.yticks(np.arange(5), PIXELS)
# 
# plt.figure()
# plt.imshow(New_COLS, cmap='plasma')
# cbar = plt.colorbar()
# cbar.set_label(r'Column Density ($m^{-2}$) +- ' + str(int(np.nanmean(Col_err))) + '$m^{-2}$', fontsize=17.5)
# plt.title(r'$H_{3}^{+}$ Column Density across Uranus from 07:28 to 13:21 UTC on $5^{th}$ September 2006', pad = 105, fontsize = 22.5)
# plt.xlabel('UTC Time (HH:MM +- 00:14)', fontsize=17.5, labelpad=10)
# plt.ylabel('Spatial position across Uranus (Pixel No. +- 2.5)', fontsize=17.5, labelpad=9)
# 
# =============================================================================
