import numpy as np
import lightkurve as lk

#filters --> g, i, r, u, z

path = 'path_of_dataste' 
#previously converted by adding 245000.5 to every date then converted using: https://astroutils.astronomy.osu.edu/time/utc2bjd.html 
#for KIC 10274244 using HiPERCAM
    #RA = 219.93632
    #Dec = +47.30971 = 47 18' 34.956"
    #Obs = Roque de los Muchachos, La Palma
datepath = 'converted_dates_to_bjd' #all of the filters are collected at the same time so you can use the same bjd
#opening datasets and defining what values go with what
data = np.loadtxt(path)
date = np.loadtxt(datepath)
bjd = date[:]
phase = data[:,0]
dtr = data[:, 1]
dtrerr = data[:,2]

#taking outof phase data to normalize this to 1
endflux = dtr[-1000:]  
flux_max = endflux.max()  

#normailization
nflux = dtr/flux_max  
nferr = dtrerr/flux_max  

#making sure output looks good
lc = lk.LightCurve(time = bjd, flux = nflux, flux_err = nferr)
lc.plot()

#save path in format for exofast to read with proper spacing etc
savepath = 'path/nDATE.SloneFILTER.kic10274244.lc.dat'
with open(savepath, 'w') as f:
    for bjd_value, flux_value, flux_err_value in zip(bjd, nflux, nferr):
        f.write(f"{bjd_value} {flux_value} {flux_err_value}\n")
