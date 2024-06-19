import numpy as np
import phoebe #using PHysics Of Eclipsing BinariEs to easily stack and see how everything looks

kic_path = '' #path of full data with all collumns from kebs
data = np.loadtxt(kic_path)
bjd = data[:, 0]
phase = data[:,1]
dtr = data[:, 6]
dtrerr = data[:,7]

#sort so only in phase data is outputted 
m = np.argsort(phase) #"every point" in said columm
bjd = bjd[m] + 2400000 #kebs.vilanova drops this exofast wants it though
phase = phase[m]
dtr = dtr[m]
dtrerr = dtrerr[m]


m = ((phase > -0.015) & (phase < 0.015)) #adjust per lc
m |= ((phase > -0.48) | (phase < -0.44))
# & for off half | for on half this depends on the orbit's eccentricity
 
#redefining based on what part of  phase it is
time = bjd[m]
phase = phase[m]
dtr = dtr[m]
dtrerr = dtrerr[m]

#restack
in_phase = np.column_stack([time,dtr,dtrerr])

#save
#exofast expects name of file to follow nYYYYMMDD.filter.whatever.whatever
# ie: n20240606.Kepler.kicname.lc.dat
savepath = ''
#have this commented out until you have set m such that the inphase data is left
np.savetxt(savepath, in_phase, fmt = '%f') #outputs bjd, dtr, dtrerr in standard notation

#check and refine m parameters
b = phoebe.default_binary()
b.add_dataset('lc', 
              times = phase, 
              #if times = times then shows every eclipse in dataset
              #if times = phase then stacks all the eclipses
              fluxes = dtr, 
              sigmas = dtrerr)
b.plot(show = True)
