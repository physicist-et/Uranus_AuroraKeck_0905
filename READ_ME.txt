This is currently the alpha version of the Uranus_AuroraKeck_0905 code used to detect the IR aurora at Uranus

To correctly use the following scripts please ensure the latest versions (as of 15/01/2022) of matplotlib, numpy, math, h3ppy, lmfit, PIL


To begin using the above data, you will need to reduce raw Keck data from https://koa.ipac.caltech.edu/cgi-bin/KOA/nph-KOAlogin, in this instance this was completed by the use of RedSpec https://www2.keck.hawaii.edu/inst/nirspec/redspec. 



The text files DataKeck06 contains the Times of all data points in this study, along with their approximate longitude and latitude positions on Uranus (as determined by Horizons https://ssd.jpl.nasa.gov/horizons/app.html#/)

The folder named Headers contains all the header information of spectras taken during the night of observations (including Neptune observations in the first quarter)

(Keck_Pixel_SelectionY script has been left to show where MiddlePointData's data comes from)

For data figures from prospective paper, please compile 2D_3D conversion scripts 