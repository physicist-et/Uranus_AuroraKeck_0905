# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:49:34 2021

@author: snowy
"""
import numpy as np
#Now to approximate the scaling of LoS with Rosie's Work
#Testing script for how to get Uranus at Keck 2006 and IRTF 2016
uranus_seangleK = (5.075900 + 5.065686)/2
uranus_seangleI = (35.784010 + 35.773649)/2
#stretch yy to become a sphere
flattening =0.0229
uranus_seangleK_Rads = (uranus_seangleK*np.pi)/180
uranus_seangleI_Rads = (uranus_seangleI*np.pi)/180
losflattening=flattening*(1-np.sin(uranus_seangleK_Rads))
eq_po_ratioK=1-losflattening

y_Keck = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
x1_Keck = -0.68240
x2_Keck = 0.68240

y_Keckadj = y_Keck/eq_po_ratioK

r1_P = []
r1_N = []

for i in range(23):
    r1_Keck = np.sqrt(x1_Keck**2 + y_Keckadj[i]**2)
    r2_Keck = np.sqrt(x2_Keck**2 + y_Keckadj[i]**2)
    r1_N.append(r1_Keck)
    r1_P.append(r2_Keck)

r_Pr = 11.491436449930903
r_pathway = np.concatenate((r1_N, r1_P))

LOSc_array = []
for i in range(46):
    LOSc = np.cos(r_pathway[i]/r_Pr)
    LOSc_array.append(LOSc)

#%%Using Tom's Method

# =============================================================================
# a1 = 11.491436449930903*eq_po_ratioK
# deltah = (3000-1300)/1127
# b1 = 11.491436449930903
# a2 = a1 + deltah
# b2 = b1 + deltah
# 
# DeltaX = []
# 
# for i in range(23):
#     SUM1 = np.sqrt((a2**2)*(1-(y_Keckadj[i]**2/b2**2)))
#     SUM2 = np.sqrt((a1**2)*(1-(y_Keckadj[i]**2/b1**2)))
#     deltax = SUM1 - SUM2
#     DeltaX.append(deltax)
#     
# Fractions = []
# for i in range(23):
#     Fractions.append((1/(DeltaX[i]/DeltaX[11])))
# 
# =============================================================================
#%% Now lets try Henriks version
# =============================================================================
# 
# Re = 60268
# Rp = 54890
# h = 400
# y_Keckadj_x = []
# y_Keckadj = 0
# 
# for i in range(1):
# #    y_Keckadj_x.append(y_Keckadj*Re)
#     B = np.sqrt(((Re+h)**2)-(0**2) - np.sqrt(Re**2-(0**2)))
#     b = B
#     a = (np.sqrt(Re**2 - 0**2))
#     c =((Rp*a)/Re)
# 
# SEL = (45/180)*np.pi
# z = np.linspace(-1.0, 1.0, num=200)
# k1Pa = []
# k2Pa = []
# k3Pa = []
# ya_P = []
# ya_b_P = []
# 
# #Positive z longitude
# for i in range(200):
#     k1 = (c**2)*(np.cos(SEL)**2) + (a**2)*(np.sin(SEL)**2)
#     k1Pa.append(k1)
#     k2 = (2*z[i])*np.cos(SEL)*np.sin(SEL)*(a**2 - c**2)
#     k2Pa.append(k2)
#     k3 =  (z[i]**2)*(c**2)*(np.sin(SEL)**2) + (z[i]**2)*(a**2)*(np.cos(SEL)**2) - (a**2)*(c**2)
#     k3Pa.append(k3)
#     
# for i in range(200):
#     ya_P.append((-k2Pa[i]+np.sqrt(k2Pa[i]**2-(4*k3Pa[i]*k1Pa[i])))/2*k1Pa[i])
#     ya_P.append((-k2Pa[i]-np.sqrt(k2Pa[i]**2-(4*k3Pa[i]*k1Pa[i])))/2*k1Pa[i])
# 
# k1Pb = []
# k2Pb = []
# k3Pb = []
# 
# for i in range(200):
#     k1 = (np.cos(SEL)**2)*(c+b)**2 + (a+b)**2*(np.sin(SEL)**2)
#     k1Pb.append(k1)
#     k2 = (2*z[i])*np.cos(SEL)*np.sin(SEL)
#     k2 = k2*((a+b)**2 - (c+b)**2)
#     k2Pb.append(k2)
#     k3 = (z[i]**2)*((c+b)**2)*(np.sin(SEL)**2) + (z[i]**2)*((a+b)**2)*(np.cos(SEL)**2) - ((a+b)**2)*((c+b)**2)
#     k3Pb.append(k3)
# 
# for i in range(200):
#     ya_b_P.append((-k2Pb[i]+np.sqrt(k2Pb[i]**2-(4*k3Pb[i]*k1Pb[i])))/2*k1Pb[i])
#     ya_b_P.append((-k2Pb[i]-np.sqrt(k2Pb[i]**2-(4*k3Pb[i]*k1Pb[i])))/2*k1Pb[i])
# 
# L_P = []
# D_P = []
# 
# for i in range(200):
#     L_p = ya_b_P[i] - ya_P[i]
#     L_P.append(L_p)
#     D_P.append(h/L_p)
# =============================================================================
