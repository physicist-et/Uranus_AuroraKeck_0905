# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:09:27 2020

@author: Emma 'Amelia'
"""
#Now lets make only the first ABBA set produce Temperatures and Ion Denisty
import matplotlib.pyplot as plt
import numpy as np
import h3ppy
from KeckIntensityStep2a import Keck_DataABBA
from KeckDataReductionStep1 import Fc_HD215

with open('MiddlePointData.csv', 'r') as file: #This reads in the file from 
    MidP = file.read().replace('\n', ' ')
file.close()

Middle_Points = np.fromstring(MidP, dtype=float, count=-1, sep= ' ')
Middle_Points = np.rint(Middle_Points)

Start_Points = []
Finish_Points = []

for m in range(54):
    MidsP1P = int(75 - 11)
    MidsP1N = int(152 + 11)
    MidsP2P = int(75 - 11)
    MidsP2N = int(152 + 11)
    Start_Points.append(MidsP1P)
    Start_Points.append(MidsP2P)
    Finish_Points.append(MidsP1N)
    Finish_Points.append(MidsP2N)

#Check this step with the new mid points selected

#%% Once the above has been completed just this cell should be complied for time effectiveness if possible
Data_Set_0 = Keck_DataABBA[0]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_1 = Keck_DataABBA[1]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_2 = Keck_DataABBA[2]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_3 = Keck_DataABBA[3]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_4 = Keck_DataABBA[4]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_5 = Keck_DataABBA[5]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_6 = Keck_DataABBA[6]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_7 = Keck_DataABBA[7]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_8 = Keck_DataABBA[8]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_9 = Keck_DataABBA[9]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_10 = Keck_DataABBA[10]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_11 = Keck_DataABBA[11]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_12 = Keck_DataABBA[12]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_13 = Keck_DataABBA[13]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_14 = Keck_DataABBA[14]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_15 = Keck_DataABBA[15]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_16 = Keck_DataABBA[16]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_17 = Keck_DataABBA[17]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_18 = Keck_DataABBA[18]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_19 = Keck_DataABBA[19]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_20 = Keck_DataABBA[20]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_21 = Keck_DataABBA[21]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_22 = Keck_DataABBA[22]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_23 = Keck_DataABBA[23]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_24 = Keck_DataABBA[24]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_25 = Keck_DataABBA[25]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_26 = Keck_DataABBA[26]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_27 = Keck_DataABBA[27]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_28 = Keck_DataABBA[28]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_29 = Keck_DataABBA[29]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_30 = Keck_DataABBA[30]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_31 = Keck_DataABBA[31]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_32 = Keck_DataABBA[32]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_33 = Keck_DataABBA[33]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_34 = Keck_DataABBA[34]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_35 = Keck_DataABBA[35]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_36 = Keck_DataABBA[36]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_37 = Keck_DataABBA[37]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_38 = Keck_DataABBA[38]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_39 = Keck_DataABBA[39]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_40 = Keck_DataABBA[40]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_41 = Keck_DataABBA[41]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_42 = Keck_DataABBA[42]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_43 = Keck_DataABBA[43]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_44 = Keck_DataABBA[44]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_45 = Keck_DataABBA[45]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_46 = Keck_DataABBA[46]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_47 = Keck_DataABBA[47]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_48 = Keck_DataABBA[48]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_49 = Keck_DataABBA[49]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_50 = Keck_DataABBA[50]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_51 = Keck_DataABBA[51]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_52 = Keck_DataABBA[52]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))
Data_Set_53 = Keck_DataABBA[53]*Fc_HD215*((4.2545*(10**10)/(0.288*0.1725)))

#%% Call in all the data from previusly and then add in the pixels togethe to produce a final Dataset bins
First_Pix_Set0 = []
First_Pix_Set1 = []
First_Pix_Set2 = []
First_Pix_Set3 = []
First_Pix_Set4 = []
First_Pix_Set5 = []
First_Pix_Set6 = []
First_Pix_Set7 = []
First_Pix_Set8 = []
First_Pix_Set9 = []
First_Pix_Set10 = []
First_Pix_Set11 = []
First_Pix_Set12 = []
First_Pix_Set13 = []
First_Pix_Set14 = []
First_Pix_Set15 = []
First_Pix_Set16 = []
First_Pix_Set17 = []
First_Pix_Set18 = []
First_Pix_Set19 = []
First_Pix_Set20 = []
First_Pix_Set21 = []
First_Pix_Set22 = []
First_Pix_Set23 = []
First_Pix_Set24 = []
First_Pix_Set25 = []
First_Pix_Set26 = []

for i in range(1024):
    n = 0
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S0 = (Data_Set_0[P, i] - Data_Set_0[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S1 = (Data_Set_1[P, i] - Data_Set_1[N, i])/2
    First_Pix_Set0.append((Data_S0 + Data_S1)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    Data_S2 = (Data_Set_2[P, i] - Data_Set_2[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S3 = (Data_Set_3[P, i] - Data_Set_3[N, i])/2
    First_Pix_Set1.append((Data_S2 + Data_S3)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S4 = (Data_Set_4[P, i] - Data_Set_4[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S5 = (Data_Set_5[P, i] - Data_Set_5[N, i])/2
    First_Pix_Set2.append((Data_S4 + Data_S5)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S6 = (Data_Set_6[P, i] - Data_Set_6[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S7 = (Data_Set_7[P, i] - Data_Set_7[N, i])/2
    First_Pix_Set3.append((Data_S6 + Data_S7)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S8 = (Data_Set_8[P, i] - Data_Set_8[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S9 = (Data_Set_9[P, i] - Data_Set_9[N, i])/2
    First_Pix_Set4.append((Data_S8 + Data_S9)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S10 = (Data_Set_10[P, i] - Data_Set_10[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S11 = (Data_Set_11[P, i] - Data_Set_11[N, i])/2
    First_Pix_Set5.append((Data_S10 + Data_S11)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S12 = (Data_Set_12[P, i] - Data_Set_12[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S13 = (Data_Set_13[P, i] - Data_Set_13[N, i])/2
    First_Pix_Set6.append((Data_S12 + Data_S13)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S14 = (Data_Set_14[P, i] - Data_Set_14[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S15 = (Data_Set_15[P, i] - Data_Set_15[N, i])/2
    First_Pix_Set7.append((Data_S14 + Data_S15)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S16 = (Data_Set_16[P, i] - Data_Set_16[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S17 = (Data_Set_17[P, i] - Data_Set_17[N, i])/2
    First_Pix_Set8.append((Data_S16 + Data_S17)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S18 = (Data_Set_18[P, i] - Data_Set_18[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S19 = (Data_Set_19[P, i] - Data_Set_19[N, i])/2
    First_Pix_Set9.append((Data_S18 + Data_S19)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S20 = (Data_Set_20[P, i] - Data_Set_20[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S21 = (Data_Set_21[P, i] - Data_Set_21[N, i])/2
    First_Pix_Set10.append((Data_S20 + Data_S21)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S22 = (Data_Set_22[P, i] - Data_Set_22[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S23 = (Data_Set_23[P, i] - Data_Set_23[N, i])/2
    First_Pix_Set11.append((Data_S22 + Data_S23)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S24 = (Data_Set_24[P, i] - Data_Set_24[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S25 = (Data_Set_25[P, i] - Data_Set_25[N, i])/2
    First_Pix_Set12.append((Data_S24 + Data_S25)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S26 = (Data_Set_26[P, i] - Data_Set_26[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S27 = (Data_Set_27[P, i] - Data_Set_27[N, i])/2
    First_Pix_Set13.append((Data_S26 + Data_S27)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S28 = (Data_Set_28[P, i] - Data_Set_28[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S29 = (Data_Set_29[P, i] - Data_Set_29[N, i])/2
    First_Pix_Set14.append((Data_S28 + Data_S29)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S30 = (Data_Set_30[P, i] - Data_Set_30[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S31 = (Data_Set_31[P, i] - Data_Set_31[N, i])/2
    First_Pix_Set15.append((Data_S30 + Data_S31)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S32 = (Data_Set_32[P, i] - Data_Set_32[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S33 = (Data_Set_33[P, i] - Data_Set_33[N, i])/2
    First_Pix_Set16.append((Data_S32 + Data_S33)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S34 = (Data_Set_34[P, i] - Data_Set_34[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S35 = (Data_Set_35[P, i] - Data_Set_35[N, i])/2
    First_Pix_Set17.append((Data_S34 + Data_S35)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S36 = (Data_Set_36[P, i] - Data_Set_36[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S37 = (Data_Set_37[P, i] - Data_Set_37[N, i])/2
    First_Pix_Set18.append((Data_S36 + Data_S37)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S38 = (Data_Set_38[P, i] - Data_Set_38[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S39 = (Data_Set_39[P, i] - Data_Set_39[N, i])/2
    First_Pix_Set19.append((Data_S38 + Data_S39)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S40 = (Data_Set_40[P, i] - Data_Set_40[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S41 = (Data_Set_41[P, i] - Data_Set_41[N, i])/2
    First_Pix_Set20.append((Data_S40 + Data_S41)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S42 = (Data_Set_42[P, i] - Data_Set_42[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S43 = (Data_Set_43[P, i] - Data_Set_43[N, i])/2
    First_Pix_Set21.append((Data_S42 + Data_S43)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S44 = (Data_Set_44[P, i] - Data_Set_44[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S45 = (Data_Set_45[P, i] - Data_Set_45[N, i])/2
    First_Pix_Set22.append((Data_S44 + Data_S45)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S46 = (Data_Set_46[P, i] - Data_Set_46[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S47 = (Data_Set_47[P, i] - Data_Set_47[N, i])/2
    First_Pix_Set23.append((Data_S46 + Data_S47)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S48 = (Data_Set_48[P, i] - Data_Set_48[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S49 = (Data_Set_49[P, i] - Data_Set_49[N, i])/2
    First_Pix_Set24.append((Data_S48 + Data_S49)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S50 = (Data_Set_50[P, i] - Data_Set_50[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S51 = (Data_Set_51[P, i] - Data_Set_51[N, i])/2
    First_Pix_Set25.append((Data_S50 + Data_S51)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S52 = (Data_Set_52[P, i] - Data_Set_52[N, i])/2
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])
    n += 2
    Data_S53 = (Data_Set_53[P, i] - Data_Set_53[N, i])/2
    First_Pix_Set26.append((Data_S52 + Data_S53)/2)
    P = int(Start_Points[n])
    N = int(Start_Points[n+1])

#%% Need to save the data here so we'll start doubling up data in time
n = 0

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_0[P:PF,:] - Data_Set_0[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_1[P:PF,:] - Data_Set_1[N:NF,:])/2
n += 2
Time0 = np.add(DataI, DataII)
Time0 = Time0/2
np.savetxt("KeckDataSet0.csv", Time0, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_2[P:PF,:] - Data_Set_2[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_3[P:PF,:] - Data_Set_3[N:NF,:])/2
n += 2
Time1 = np.add(DataI, DataII)
Time1 = Time1/2
np.savetxt("KeckDataSet1.csv", Time1, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_4[P:PF,:] - Data_Set_4[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_5[P:PF,:] - Data_Set_5[N:NF,:])/2
n += 2
Time2 = np.add(DataI, DataII)
Time2 = Time2/2
np.savetxt("KeckDataSet2.csv", Time2, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_6[P:PF,:] - Data_Set_6[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_7[P:PF,:] - Data_Set_7[N:NF,:])/2
n += 2
Time3 = np.add(DataI, DataII)
Time3 = Time3/2
np.savetxt("KeckDataSet3.csv", Time3, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_8[P:PF,:] - Data_Set_8[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_9[P:PF,:] - Data_Set_9[N:NF,:])/2
n += 2
Time4 = np.add(DataI, DataII)
Time4 = Time4/2
np.savetxt("KeckDataSet4.csv", Time4, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_10[P:PF,:] - Data_Set_10[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_11[P:PF,:] - Data_Set_11[N:NF,:])/2
n += 2
Time5 = np.add(DataI, DataII)
Time5 = Time5/2
np.savetxt("KeckDataSet5.csv", Time5, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_12[P:PF,:] - Data_Set_12[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_13[P:PF,:] - Data_Set_13[N:NF,:])/2
n += 2
Time6 = np.add(DataI, DataII)
Time6 = Time6/2
np.savetxt("KeckDataSet6.csv", Time6, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_14[P:PF,:] - Data_Set_14[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_15[P:PF,:] - Data_Set_15[N:NF,:])/2
n += 2
Time7 = np.add(DataI, DataII)
Time7 = Time7/2
np.savetxt("KeckDataSet7.csv", Time7, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_16[P:PF,:] - Data_Set_16[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_17[P:PF,:] - Data_Set_17[N:NF,:])/2
n += 2
Time8 = np.add(DataI, DataII)
Time8 = Time8/2
np.savetxt("KeckDataSet8.csv", Time8, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_18[P:PF,:] - Data_Set_18[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_19[P:PF,:] - Data_Set_19[N:NF,:])/2
n += 2
Time9 = np.add(DataI, DataII)
Time9 = Time9/2
np.savetxt("KeckDataSet9.csv", Time9, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_20[P:PF,:] - Data_Set_20[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_21[P:PF,:] - Data_Set_21[N:NF,:])/2
n += 2
Time10 = np.add(DataI, DataII)
Time10 = Time10/2
np.savetxt("KeckDataSet10.csv", Time10, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_22[P:PF,:] - Data_Set_22[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_23[P:PF,:] - Data_Set_23[N:NF,:])/2
n += 2
Time11 = np.add(DataI, DataII)
Time11 = Time11/2
np.savetxt("KeckDataSet11.csv", Time11, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_24[P:PF,:] - Data_Set_24[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_25[P:PF,:] - Data_Set_25[N:NF,:])/2
n += 2
Time12 = np.add(DataI, DataII)
Time12 = Time12/2
np.savetxt("KeckDataSet12.csv", Time12, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_26[P:PF,:] - Data_Set_26[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_27[P:PF,:] - Data_Set_27[N:NF,:])/2
n += 2
Time13 = np.add(DataI, DataII)
Time13 = Time13/2
np.savetxt("KeckDataSet13.csv", Time13, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_28[P:PF,:] - Data_Set_28[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_29[P:PF,:] - Data_Set_29[N:NF,:])/2
n += 2
Time14 = np.add(DataI, DataII)
Time14 = Time14/2
np.savetxt("KeckDataSet14.csv", Time14, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_30[P:PF,:] - Data_Set_30[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_31[P:PF,:] - Data_Set_31[N:NF,:])/2
n += 2
Time15 = np.add(DataI, DataII)
Time15 = Time15/2
np.savetxt("KeckDataSet15.csv", Time15, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_32[P:PF,:] - Data_Set_32[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_33[P:PF,:] - Data_Set_33[N:NF,:])/2
n += 2
Time16 = np.add(DataI, DataII)
Time16 = Time16/2
np.savetxt("KeckDataSet16.csv", Time16, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_34[P:PF,:] - Data_Set_34[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_35[P:PF,:] - Data_Set_35[N:NF,:])/2
n += 2
Time17 = np.add(DataI, DataII)
Time17 = Time17/2
np.savetxt("KeckDataSet17.csv", Time17, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_36[P:PF,:] - Data_Set_36[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_37[P:PF,:] - Data_Set_37[N:NF,:])/2
n += 2
Time18 = np.add(DataI, DataII)
Time18 = Time18/2
np.savetxt("KeckDataSet18.csv", Time18, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_38[P:PF,:] - Data_Set_38[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_39[P:PF,:] - Data_Set_39[N:NF,:])/2
n += 2
Time19 = np.add(DataI, DataII)
Time19 = Time19/2
np.savetxt("KeckDataSet19.csv", Time19, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_40[P:PF,:] - Data_Set_40[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_41[P:PF,:] - Data_Set_41[N:NF,:])/2
n += 2
Time20 = np.add(DataI, DataII)
Time20 = Time20/2
np.savetxt("KeckDataSet20.csv", Time20, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_42[P:PF,:] - Data_Set_42[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_43[P:PF,:] - Data_Set_43[N:NF,:])/2
n += 2
Time21 = np.add(DataI, DataII)
Time21 = Time21/2
np.savetxt("KeckDataSet21.csv", Time21, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_44[P:PF,:] - Data_Set_44[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_45[P:PF,:] - Data_Set_45[N:NF,:])/2
n += 2
Time22 = np.add(DataI, DataII)
Time22 = Time22/2
np.savetxt("KeckDataSe22.csv", Time22, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_46[P:PF,:] - Data_Set_46[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_47[P:PF,:] - Data_Set_47[N:NF,:])/2
n += 2
Time23 = np.add(DataI, DataII)
Time23 = Time23/2
np.savetxt("KeckDataSet23.csv", Time23, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_48[P:PF,:] - Data_Set_48[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_49[P:PF,:] - Data_Set_49[N:NF,:])/2
n += 2
Time24 = np.add(DataI, DataII)
Time24 = Time24/2
np.savetxt("KeckDataSet24.csv", Time24, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_50[P:PF,:] - Data_Set_50[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_51[P:PF,:] - Data_Set_51[N:NF,:])/2
n += 2
Time25 = np.add(DataI, DataII)
Time25 = Time25/2
np.savetxt("KeckDataSet25.csv", Time25, delimiter=",")

P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataI = (Data_Set_52[P:PF,:] - Data_Set_52[N:NF,:])/2
n += 2
P = int(Start_Points[n])
PF = int(Finish_Points[n])
N = int(Start_Points[n+1])
NF = int(Finish_Points[n+1])
DataII = (Data_Set_53[P:PF,:] - Data_Set_53[N:NF,:])/2
n += 2
Time26 = np.add(DataI, DataII)
Time26 = Time26/2
np.savetxt("KeckDataSet26.csv", Time26, delimiter=",")

#%% Now we need to call the Time variables and seperate them by Pixels and put these into Pixel files

for a in range(22):
    Tot = np.concatenate((Time0[a,:], Time1[a,:], Time2[a,:], Time3[a,:], Time4[a,:], Time5[a,:], Time6[a,:], Time7[a,:], Time8[a,:], Time9[a,:], Time10[a,:], Time11[a,:], Time12[a,:], Time13[a,:], Time14[a,:], Time15[a,:], Time16[a,:], Time17[a,:], Time18[a,:], Time19[a,:], Time20[a,:], Time21[a,:], Time22[a,:], Time23[a,:], Time24[a,:], Time25[a,:], Time26[a,:]))
    Pix0 = np.reshape(Tot, (27, 1024))
    np.savetxt('KeckDataPix' + str(a) + '.csv', Tot, delimiter=',')
