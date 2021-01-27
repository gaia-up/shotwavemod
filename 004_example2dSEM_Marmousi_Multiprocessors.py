# This script performs 2D Seismic Wave and Shot Simulation using Spectral Element Method for 2D seismic line by using multicores
# Tested under Ubuntu 18.04.5 LTS
# Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing)
# Agus Abdullah, Ph.D. Waskito Pranowo, M.T. Dicky Ahmad Zaky, M.T.
# Universitas Pertamina - Indonesia  2021
# HOW TO RUN
# Step1: Define parameterization in  seismic2dsemmulticores.par   (Parameters are from  row 22 to 40!)
# Step2: Run this Python script via Python IDE or Ubuntu Terminal:  python  004_example2dSEM_Marmousi_Multiprocessors.py
# Input:  seismic2dsemmulticores.par  and marmousi_vel.npy (size: nx,nz  numpy format) you may change it nx,nz must be even!

import subprocess
import numpy as np
import matplotlib.pyplot as plt

subprocess.run(["./seismic2dsemmulticores"])
filein = np.genfromtxt('seismic2dsemmulticores.par', dtype=str, skip_header=21)

xmax= float(filein[0])
zmax= float(filein[1])
dx= float(filein[2])
dz= float(filein[3])
model= filein[10]
path= filein[11]
shotfile= filein[17]
noofshots = 731   #check from the output
shotke = np.arange(0,noofshots,1)

shots=[]
nears=[]
for i in shotke:
    shot = np.load('%s/%s_%i.npy' % (path,shotfile, i)).T
    shots.extend(shot)
    nears.extend(shot[30:31, :])
nears = np.asarray(nears).T
shots = np.asarray(shots).T
np.save('shot2dmarmousi', shots)


plt.subplot(2,1,1)
model = np.load(model)
plt.imshow(model, cmap='jet', interpolation='bilinear',aspect='auto', vmin=1000, vmax = 4000)
plt.title('Marmousi Model Vp')


v = 0.0000005
plt.subplot(2,1,2)
plt.imshow(nears, cmap='bwr', interpolation='bilinear',aspect='auto', vmin=-v, vmax = v)
plt.title('Near Traces (unmigrated)')
plt.show()
