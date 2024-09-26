import numpy as np
import lightkurve as lk

#g, i, r, u, z

path = '/home/mrdecesare/Desktop/kic10274244/hypercam/not_using/z.dat' 
datepath = '/home/mrdecesare/Desktop/kic10274244/hypercam/not_using/bjd.dat'
data = np.loadtxt(path)
date = np.loadtxt(datepath)
bjd = date[:]
phase = data[:,0]
dtr = data[:, 1]
dtrerr = data[:,2]

endflux = dtr[-1000:]  
endfluxerr = dtrerr[-1000:]  

flux_max = endflux.max()  

nflux = dtr/flux_max  
nferr = dtrerr/flux_max  

lc = lk.LightCurve(time = bjd, flux = nflux, flux_err = nferr)

lc.plot()


savepath = '/home/mrdecesare/Desktop/kic10274244/hypercam/n20240924.SloneZ.kic10274244.lc.dat'

with open(savepath, 'w') as f:
    for bjd_value, flux_value, flux_err_value in zip(bjd, nflux, nferr):
        f.write(f"{bjd_value} {flux_value} {flux_err_value}\n")
#np.savetxt(savepath, np.column_stack((bjd, nflux, nferr)), delimiter=',', fmt = '%f')
