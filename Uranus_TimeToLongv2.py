# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:47:11 2020

@author: Emma 'Amelia'
"""
#Construct a script that will convert the time of the measurements into arbitarty longitude
import re
import numpy as np

#%% firstly read in the headers to extract the times and save these 

TimeH = []
TimeM = []
TimeS = []

for x in range(224): #We use this list to create a list which holds all the data from Order19
    xi = x + 76
    filename = 'C:/Users/snowy/OneDrive/Documents/Python work/Keck 05Sept06 Data/Keck 05Sept06 Data/Headers/' + str(xi) + '.dat'
    n = 0
    if xi >= 76 and xi < 192:
        with open(filename, 'r') as file: #This reads in the file from 
            for line in file:
                if (line.find('UTC') != -1 and n == 0):
                    result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    TimeH.append(int(result[0]))
                    TimeM.append(int(result[1]))
                    TimeS.append(float(result[2]))
                    n = 1
    elif xi >= 192 and xi < 196:
        pass
    elif xi >= 196 and xi < 296:
        with open(filename, 'r') as file: #This reads in the file from 
            for line in file:
                if (line.find('UTC') != -1 and n == 0):
                    result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    TimeH.append(int(result[0]))
                    TimeM.append(int(result[1]))
                    TimeS.append(float(result[2]))
                    n = 1
    else:
        pass

#%% Now lets work out how many degrees of longitudinal rotation there is in a Uranian day so that time can be converted

Ur_Rotate = 17.24*60*60
Tot_Long = 360

#So Degree of Rotation per minute is
Deg_perSecond = Tot_Long/(Ur_Rotate)

#%% Now we need to find the difference between one stack of data and another 
#In the current situation 216 Data sets gives 54 ABBA sets, in the final data we us 52 sets which are binned into 13 sets

NumSet = (len(TimeH))/4 - 1
AV_Times = []

#for a in range(int(NumSet)):
#    AvTimeH = (TimeH[16*a]*(3600) + TimeH[(16*a)+1]*(3600) + TimeH[(16*a)+2]*(3600) + TimeH[(16*a)+3]*(3600) + TimeH[(16*a)+4]*(3600) + TimeH[(16*a)+5]*(3600) + TimeH[(16*a)+6]*(3600) + TimeH[(16*a)+7]*(3600) + TimeH[(16*a)+8]*(3600) + TimeH[(16*a)+9]*(3600) + TimeH[(16*a)+10]*(3600) + TimeH[(16*a)+11]*(3600) + TimeH[a+12]*(3600) + TimeH[(16*a)+13]*(3600) + TimeH[(16*a)+14]*(3600) + TimeH[(16*a)+15]*(3600))/16
#    AvTimeM = (TimeM[16*a]*60 + TimeM[(16*a)+1]*60 + TimeM[(16*a)+2]*60 + TimeM[(16*a)+3]*60 + TimeM[(16*a)+4]*60 + TimeM[(16*a)+5]*60 + TimeM[(16*a)+6]*60 + TimeM[(16*a)+7]*60 + TimeM[(16*a)+8]*60 + TimeM[(16*a)+9]*60 + TimeM[(16*a)+10]*60 + TimeM[(16*a)+11]*60 + TimeM[(16*a)+12]*60 + TimeM[(16*a)+13]*60 + TimeM[(16*a)+14]*60 + TimeM[(16*a)+15]*60)/16
#    AvTimeS = (TimeS[16*a] + TimeS[(16*a)+1] + TimeS[(16*a)+2] + TimeS[(16*a)+3] + TimeS[(16*a)+4] + TimeS[(16*a)+5] + TimeS[(16*a)+6] + TimeS[(16*a)+7] + TimeS[(16*a)+8] + TimeS[(16*a)+9] + TimeS[(16*a)+10] + TimeS[(16*a)+11] + TimeS[(16*a)+12] + TimeS[(16*a)+13] + TimeS[(16*a)+14] + TimeS[(16*a)+15])/16
#    AVTimes = (AvTimeH + AvTimeM + AvTimeS)
#    AV_Times.append(AVTimes)
 
for a in range(int(NumSet)):
    AvTimeH = (TimeH[4*a]*(3600) + TimeH[(4*a)+3]*(3600))/2
    AvTimeM = (TimeM[4*a]*60 + TimeM[(4*a)+3]*60)/2
    AvTimeS = (TimeS[4*a] + TimeS[(4*a)+3])/2
    AVTimes = (AvTimeH + AvTimeM + AvTimeS)
    AV_Times.append(AVTimes)
   
#Now convert the difference between these times into longitudes
Longitude_Change = []

for a in range(int(NumSet-1)):
    Time_Diff = AV_Times[a+1] - AV_Times[a]
    Deg_Long = Time_Diff*Deg_perSecond
    Longitude_Change.append(Deg_Long)

Long_points = []
#Now we add up each change to get the total degree change over the first to last observations
for a in range(int(NumSet)):
    Long = np.sum(Longitude_Change[0:a])
    #Long = format(Long, '.3f')
    Long_points.append(Long)

#Now to work out how to make it look pretty on the graph layout.
#%% Now to calculate the difference between the start and end of observation times to work out how far they span

Limits = []
TimeIr = []
TimeFr = []
Uranus_Dia = 3.69485  #Angular Diamete
Tabs = 0.144*36/(np.pi*Uranus_Dia)

for a in range(int(NumSet)):
    TimeH1 = TimeH[4*a]*3600
    TimeH2 = TimeH[(4*a)+3]*3600
    TimeM1 = TimeM[4*a]*60
    TimeM2 = TimeM[(4*a)+3]*60
    TimeS1 = TimeS[4*a]
    TimeS2 = TimeS[(4*a)+3]
    TimeI =  TimeH1 + TimeM1 + TimeS1
    TimeF =  TimeH2 + TimeM2 + TimeS2
    Start_Long = (AV_Times[a] - TimeI)*Deg_perSecond
    TimeIr.append(TimeI/3600)
    #print(Start_Long)
    #Start_Long = format(Start_Long, '.3f')
    Finish_Long = (TimeF - AV_Times[a])*Deg_perSecond
    TimeFr.append(TimeF/3600)
    #print(Finish_Long)
    #Finish_Long = format(Finish_Long, '.3f')
    Limits.append(int(round(round(Long_points[a] - Start_Long - Tabs + 1.2, 2)*10)))
    Limits.append(int(round(round(Finish_Long + Long_points[a] + Tabs + 1.2, 2)*10)))

Limits.append(Limits[int(2*NumSet)-1])
Err_TimeDiff = np.sqrt(2)*np.mean(Start_Long)/(Deg_perSecond*3600)
Deg_perSecondErr = (0.01*3600)/Ur_Rotate

#5.971911111111112 is the amount of Time from the start of the investigation to the end
Deg_LongErr = np.sqrt((Deg_perSecondErr)**2+(Err_TimeDiff/5.971911111111112)**2)
Long_Err = np.sqrt(3)*(Deg_LongErr)*100