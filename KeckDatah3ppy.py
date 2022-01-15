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
from matplotlib import cm
import math

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
#Need to flip from 17 to 27 and remember to remove 14 to 17 sets

with open('KeckDataPix0_rough.csv', 'r') as file: #This reads in the file from 
    Pix0 = file.read().replace('\n', ' ')
    Pix0 = np.fromstring(Pix0, dtype=float, count=-1, sep= ' ')
    Pix0 = np.reshape(Pix0, (27, 1024))
file.close()

with open('KeckDataPix1_rough.csv', 'r') as file: #This reads in the file from 
    Pix1 = file.read().replace('\n', ' ')
    Pix1 = np.fromstring(Pix1, dtype=float, count=-1, sep= ' ')
    Pix1 = np.reshape(Pix1, (27, 1024))
file.close()

with open('KeckDataPix2_rough.csv', 'r') as file: #This reads in the file from 
    Pix2 = file.read().replace('\n', ' ')
    Pix2 = np.fromstring(Pix2, dtype=float, count=-1, sep= ' ')
    Pix2 = np.reshape(Pix2, (27, 1024))
file.close()

with open('KeckDataPix3_rough.csv', 'r') as file: #This reads in the file from 
    Pix3 = file.read().replace('\n', ' ')
    Pix3 = np.fromstring(Pix3, dtype=float, count=-1, sep= ' ')
    Pix3 = np.reshape(Pix3, (27, 1024))
file.close()

with open('KeckDataPix4_rough.csv', 'r') as file: #This reads in the file from 
    Pix4 = file.read().replace('\n', ' ')
    Pix4 = np.fromstring(Pix4, dtype=float, count=-1, sep= ' ')
    Pix4 = np.reshape(Pix4, (27, 1024))
file.close()

with open('KeckDataPix5_rough.csv', 'r') as file: #This reads in the file from 
    Pix5 = file.read().replace('\n', ' ')
    Pix5 = np.fromstring(Pix5, dtype=float, count=-1, sep= ' ')
    Pix5 = np.reshape(Pix5, (27, 1024))
file.close()

with open('KeckDataPix6_rough.csv', 'r') as file: #This reads in the file from 
    Pix6 = file.read().replace('\n', ' ')
    Pix6 = np.fromstring(Pix6, dtype=float, count=-1, sep= ' ')
    Pix6 = np.reshape(Pix6, (27, 1024))
file.close()

with open('KeckDataPix7_rough.csv', 'r') as file: #This reads in the file from 
    Pix7 = file.read().replace('\n', ' ')
    Pix7 = np.fromstring(Pix7, dtype=float, count=-1, sep= ' ')
    Pix7 = np.reshape(Pix7, (27, 1024))
file.close()

with open('KeckDataPix8_rough.csv', 'r') as file: #This reads in the file from 
    Pix8 = file.read().replace('\n', ' ')
    Pix8 = np.fromstring(Pix8, dtype=float, count=-1, sep= ' ')
    Pix8 = np.reshape(Pix8, (27, 1024))
file.close()

with open('KeckDataPix9_rough.csv', 'r') as file: #This reads in the file from 
    Pix9 = file.read().replace('\n', ' ')
    Pix9 = np.fromstring(Pix9, dtype=float, count=-1, sep= ' ')
    Pix9 = np.reshape(Pix9, (27, 1024))
file.close()

with open('KeckDataPix10_rough.csv', 'r') as file: #This reads in the file from 
    Pix10 = file.read().replace('\n', ' ')
    Pix10 = np.fromstring(Pix10, dtype=float, count=-1, sep= ' ')
    Pix10 = np.reshape(Pix10, (27, 1024))
file.close()

with open('KeckDataPix11_rough.csv', 'r') as file: #This reads in the file from 
    Pix11 = file.read().replace('\n', ' ')
    Pix11 = np.fromstring(Pix11, dtype=float, count=-1, sep= ' ')
    Pix11 = np.reshape(Pix11, (27, 1024))
file.close()

with open('KeckDataPix12_rough.csv', 'r') as file: #This reads in the file from 
    Pix12 = file.read().replace('\n', ' ')
    Pix12 = np.fromstring(Pix12, dtype=float, count=-1, sep= ' ')
    Pix12 = np.reshape(Pix12, (27, 1024))
file.close()

with open('KeckDataPix13_rough.csv', 'r') as file: #This reads in the file from 
    Pix13 = file.read().replace('\n', ' ')
    Pix13 = np.fromstring(Pix13, dtype=float, count=-1, sep= ' ')
    Pix13 = np.reshape(Pix13, (27, 1024))
file.close()

with open('KeckDataPix14_rough.csv', 'r') as file: #This reads in the file from 
    Pix14 = file.read().replace('\n', ' ')
    Pix14 = np.fromstring(Pix14, dtype=float, count=-1, sep= ' ')
    Pix14 = np.reshape(Pix14, (27, 1024))
file.close()

with open('KeckDataPix15_rough.csv', 'r') as file: #This reads in the file from 
    Pix15 = file.read().replace('\n', ' ')
    Pix15 = np.fromstring(Pix15, dtype=float, count=-1, sep= ' ')
    Pix15 = np.reshape(Pix15, (27, 1024))
file.close()

with open('KeckDataPix16_rough.csv', 'r') as file: #This reads in the file from 
    Pix16 = file.read().replace('\n', ' ')
    Pix16 = np.fromstring(Pix16, dtype=float, count=-1, sep= ' ')
    Pix16 = np.reshape(Pix16, (27, 1024))
file.close()

with open('KeckDataPix17_rough.csv', 'r') as file: #This reads in the file from 
    Pix17 = file.read().replace('\n', ' ')
    Pix17 = np.fromstring(Pix17, dtype=float, count=-1, sep= ' ')
    Pix17 = np.reshape(Pix17, (27, 1024))
file.close()

with open('KeckDataPix18_rough.csv', 'r') as file: #This reads in the file from 
    Pix18 = file.read().replace('\n', ' ')
    Pix18 = np.fromstring(Pix18, dtype=float, count=-1, sep= ' ')
    Pix18 = np.reshape(Pix18, (27, 1024))
file.close()

with open('KeckDataPix19_rough.csv', 'r') as file: #This reads in the file from 
    Pix19 = file.read().replace('\n', ' ')
    Pix19 = np.fromstring(Pix19, dtype=float, count=-1, sep= ' ')
    Pix19 = np.reshape(Pix19, (27, 1024))
file.close()

with open('KeckDataPix20_rough.csv', 'r') as file: #This reads in the file from 
    Pix20 = file.read().replace('\n', ' ')
    Pix20 = np.fromstring(Pix20, dtype=float, count=-1, sep= ' ')
    Pix20 = np.reshape(Pix20, (27, 1024))
file.close()

with open('KeckDataPix21_rough.csv', 'r') as file: #This reads in the file from 
    Pix21 = file.read().replace('\n', ' ')
    Pix21 = np.fromstring(Pix21, dtype=float, count=-1, sep= ' ')
    Pix21 = np.reshape(Pix21, (27, 1024))
file.close()

with open('KeckDataPix22_rough.csv', 'r') as file: #This reads in the file from 
    Pix22 = file.read().replace('\n', ' ')
    Pix22 = np.fromstring(Pix22, dtype=float, count=-1, sep= ' ')
    Pix22 = np.reshape(Pix22, (27, 1024))
file.close()

with open('KeckDataPix23_rough.csv', 'r') as file: #This reads in the file from 
    Pix23 = file.read().replace('\n', ' ')
    Pix23 = np.fromstring(Pix23, dtype=float, count=-1, sep= ' ')
    Pix23 = np.reshape(Pix23, (27, 1024))
file.close()

with open('KeckDataPix24_rough.csv', 'r') as file: #This reads in the file from 
    Pix24 = file.read().replace('\n', ' ')
    Pix24 = np.fromstring(Pix24, dtype=float, count=-1, sep= ' ')
    Pix24 = np.reshape(Pix24, (27, 1024))
file.close()