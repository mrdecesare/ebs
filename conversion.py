import numpy as np
import lightkurve as lk

path = 'path to dataset from keplerebs.villanova.edu'
data = np.loadtxt(path)
time = data[:,0] #time in MJD
dtr = data[:,6] #detrended dataset
dtrerr = data[:,7] #detrended dataset error

period = period_value #insert value for the systems period

lc = lk.LightCurve(time = time, flux = dtr, flux_err = dtrerr)
lc.scatter() #check to see that the data set is what we want
lc.fold(period).scatter() #check for outlires we can try and remove from the light curve
lc.remove_outlires(sigma = 2, returnmask = TRUE).scatter() #value of sigma to change with outlires and apply the mask so we no longer have the outliers

nt = lc.time.value + 2400000
nf = lc.flux.value
nfe = lc.flux_err.value

restack = np.column_stack((nt, nf, nfe))
savepath = 'save path where exofast will find all the files needed to execute run'
np.savetxt(savepath, restack, fmt = ('%17.16', '%17.16','%17.16')) #actually save the new data file and make sure it has all the decimal places Kepler outputted
