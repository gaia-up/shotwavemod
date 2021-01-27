# This script performs 3D Seismic Wave and Shot Simulation using Finite Difference Method
# Tested under Ubuntu 18.04.5 LTS
# Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing)
# Agus Abdullah, Ph.D. Waskito Pranowo, M.T. Dicky Ahmad Zaky, M.T.
# Universitas Pertamina - Indonesia  2021
# HOW TO RUN
# Step1: Define parameterization in  seismic3dfdm.par   (Parameters are from  row 25 to 46 !)
# Step2: Run this Python script via Python IDE or Ubuntu Terminal:  python  003_example3dFDM.py
# Input:  seismic3dfdm.par  and velocityoneshot3d.npy (size: nx,ny,nz  numpy format)

import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv


filein = np.genfromtxt('seismic3dfdm.par', dtype=str, skip_header=24)
xmax= float(filein[0])
ymax= float(filein[1])
zmax= float(filein[2])
dx= float(filein[3])
dy= float(filein[4])
dz= float(filein[5])
path= filein[14]
shotfile= filein[21]
nx = int(xmax / dx)  # number of grid points in x-direction
ny = int(ymax / dy)  # number of grid points in y-direction
nz = int(zmax / dz)  # number of grid points in z-direction


###3D VELOCITY FIELD : USER MAY CHANGE IT ################################
model = np.ones((nx,ny,nz))*2000 # # LAYER  1
model[0:nx, 0:ny, 50:100]  = np.ones((nx, ny, 50)) * 3000  # LAYER  2
model[0:nx, 0:ny, 100:150] = np.ones((nx, ny, 50)) * 2500  # LAYER  3
model[0:nx, 0:ny, 150:200] = np.ones((nx, ny, 50)) * 4500  # LAYER  4
np.save('velocityoneshot3d', model)
subprocess.run(["./seismic3dfdm"])



data = np.load('%s/%s.npy' % (path,shotfile))


shot = []
for i in range(6):
    shot.extend(data[i,:,:].T)
shot = np.asarray(shot).T
rmstr = shot[:, int(shot.shape[1] / 3):int(shot.shape[1] / 2)]
rms = np.std(rmstr - rmstr.mean(axis=0))
scale = 0.5
plt.suptitle('3D SHOT RECORD FINITE DIFFERENCE METHOD')
plt.imshow(shot, interpolation='bilinear', cmap='bwr', aspect='auto',  vmin=-rms*scale, vmax = rms*scale)
plt.show()



############### WAVEFIELD  VISUALIZATION #############################
i = 2  #wavefield nth
values = np.load('%s/wavefieldFDM_%s.npy'%(path,i) )
values = values[:,:,::-1] #upside-down

vs = values.shape

slice = values[:,int(vs[1]/2),:]
vmin = np.min(slice)
vmax = np.max(slice)


grid = pv.UniformGrid()
grid.dimensions = values.shape
grid.origin = (0, 0, 0)  # The bottom left corner of the data set
grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis
grid.point_arrays["Amplitudes"] = values.flatten(order="F")  # Flatten the array!
slices1 = grid.slice_orthogonal(x=int(vs[0]/2), y=int(vs[1]/2), z=int(vs[2]/2))


values = np.load('%s'%model)
values = values[:,:,::-1] #upside-down
grid = pv.UniformGrid()
grid.dimensions = values.shape
grid.origin = (0, 0, 0)  # The bottom left corner of the data set
grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis
grid.point_arrays["Velocity"] = values.flatten(order="F")  # Flatten the array!
slices2 = grid.slice_orthogonal(x=int(vs[0]/2), y=int(vs[1]/2), z=int(vs[2]/2))

p = pv.Plotter()
sc = 0.2

sargs = dict(height=np.nan, vertical=True, position_x=np.nan, position_y=np.nan)
p.add_mesh(slices1,cmap='Greys', opacity=0.96, clim=[sc*vmin, sc*vmax], scalar_bar_args=sargs)

sargs = dict(height=0.25, vertical=True, position_x=0.05, position_y=0.05)
p.add_mesh(slices2,cmap='jet', opacity=0.96, clim=[1000, 5000], scalar_bar_args=sargs)
p.set_background('black', top=None)
p.show()

