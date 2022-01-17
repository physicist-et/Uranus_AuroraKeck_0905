"""
k) gaussstar --- translation of the gaussstar.pro (IDL) written by James O'Donoghue. Informs the user of a factor by which to divide spectral data to account for light not captured from a target object by the instrument slit
"""
def gaussstar(slitwidth=0.43, seeing=0.7, pixelslit=0.144):
    """
    Input/(s):
        slitwidth --- the width of the instrument slit, default value set to 0.432 (wonder which instrument?...)
        seeing --- the arcsecond(?) seeing on the night, default value set to 0.8
        pixelslit --- number of arcseconds per pixel in the instrument slit, default value of 0.144
    Output/(s):
        gaussstar_factor --- the factor by which the data array has to be divided
    """
    #Modules for import
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    
    #Float the sigma and mu values
    sigma = seeing/2.355
    mu = 0
    
    #Float the arrays which will store some intermediary values
    xarr = (np.arange(10000)/1000.)-5.
    parr = []
    for x in xarr:
        parr_x = (1 / (sigma * math.sqrt(2 * math.pi))) * np.exp((-1 * (x - mu)**2) / (2 * sigma**2))
        parr.append(parr_x)
        
    #Next set of values
    L = mu - (slitwidth / 2)
    L2 = L - (2 * pixelslit)
    R = mu + (slitwidth / 2)
    R2 = R + (2 * pixelslit)
    #The intermediary awkward values...
    xarr_minus_L = xarr - L
    xarr_minus_L2 = xarr - L2
    xarr_minus_R = xarr - R
    xarr_minus_R2 = xarr - R2
    #The awkward variables!
    LHwh = np.argmin(abs(xarr_minus_L))
    LHwh2 = np.argmin(abs(xarr_minus_L2))
    RHwh = np.argmin(abs(xarr_minus_R))
    RHwh2 = np.argmin(abs(xarr_minus_R2))
    #print(LHwh, LHwh2, RHwh, RHwh2)
    #Penultimate variables
    LH = parr[LHwh]
    LH2 = parr[LHwh2]
    RH = parr[RHwh]
    RH2 = parr[RHwh2]
    #print(LH, LH2, RH, RH2)
    
    #Percentages
    perc = sum(parr[LHwh:RHwh])/sum(parr)
    perc2 = sum(parr[LHwh2:RHwh2])/sum(parr)
    
    #Plots
    #plt.figure(figsize=[10,6])
    #plt.plot(xarr, parr, 'black')
    #plt.xlabel('Arcseconds', fontsize=14)
    #plt.xlim([-5,5])
    #plt.title('Spread of data around your instrument slit', fontsize=14)
    #plt.vlines(R, 0, RH, 'red')
    #plt.vlines(L, 0, LH, 'red')
    #plt.vlines(R2, 0, RH2, 'blue')
    #plt.vlines(L2, 0, LH2, 'blue')
    #plt.text(R+(R*1.5), RH, str(round(perc*100, 2))+'% slit throughput', fontsize=14)
    #plt.text(R2+(R2*0.75), RH2, str(round(perc2*100, 2))+'% +2 pix throughput', fontsize=14)
    #plt.show()
    
    #Print the final instruction from the program, the point of the whole thing...
    #print('Divide your data by:', round(perc, 6), ', making it larger.')
    
    ##Final two variables that don't appear to be used for anything else ever again
    #center_intensity = np.argmax(parr)
    #center_arcsecs = np.argmax(parr)
    
    #Final variable to return
    gaussstar_factor = perc
    
    return gaussstar_factor



