import numpy as np
import phoebe 
import sys

kic_path = '/home/mrdecesare/Desktop/kic4847832/04847832.00.lc.data' #path of full data with all collumns from kebs
data = np.loadtxt(kic_path)
bjd = data[:, 0]
phase = data[:,1]
dtr = data[:, 6]
dtrerr = data[:,7]

#sort so only in phase data is outputted and convert to standard notation
m = np.argsort(phase) #"every point" in said columm
bjd = bjd[m] + 2400000
phase = phase[m]
dtr = dtr[m]
dtrerr = dtrerr[m]


m = ((phase > -0.015) & (phase < 0.015)) #adjust per lc
m |= ((phase < -0.44) & (phase > -0.48)) # #adjust per lc
#m |= ((phase > -0.48) | (phase < -0.44))
# & for off half | for on half
 
#redefining based on what part of  phase it is
time = bjd[m]
phase = phase[m]
dtr = dtr[m]
dtrerr = dtrerr[m]

#restack
in_phase = np.column_stack([time,dtr,dtrerr])

#save
#exofast expects name of file to follow nYYYYMMDD.filter.whatever.whatever
savepath = '/home/mrdecesare/Desktop/kic4847832/n20240614.Kepler.kic4847832.lc.dat'
np.savetxt(savepath, in_phase, fmt = '%f') #outputs bjd, dtr, dtrerr in standard notation

#check and refine m parameters
b = phoebe.default_binary()
b.add_dataset('lc', 
              times = phase, #if times = times then i have every eclipse if times = phase it stacks
              fluxes = dtr, 
              sigmas = dtrerr)
b.plot(show = True)
