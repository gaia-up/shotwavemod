# shotwavemod
Programs for Seismic Wave Simulation <br /> 
Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing) <br /> 
Universitas Pertamina

![gaia banner](https://drive.google.com/uc?export=view&id=1O0lNb8YhU_2u9WwroawwWtNuk1Nq7SBN)

# Requirements
Tested on: 
* OS: Ubuntu 18.04.5 LTS bionic
* Python Ver: 3.6.9
* Required Library
```python
sudo apt-get install libpython3.6-dev
pip install numpy==1.19.5
pip install pyprind==2.11.2
pip install matplotlib==3.0.0
pip install pyvista==0.26.1
pip install pandas==1.1.5
```

# Function
List of programs
* seismic2dfdm: 2D Seismic Wave and Shot Simulation using Finite Difference Method
* seismic2dsem: 2D Seismic Wave and Shot Simulation using Spectral Element Method
* seismic2dsemmulticores: 2D Seismic Wave and Shot Simulation using Spectral Element Method for 2D seismic line by using multicores
* seismic3dfdm: 3D Seismic Wave and Shot Simulation using Finite Difference Method
* seismic3dsem: 3D Seismic Wave and Shot Simulation using Spectral Element Method
* geom2d: Geometry Assignment
* segyout: segy out

# Usage
Each program has complementary parameter file (.par) and should be at the same directory with programs file. In general the steps to conduct the simulation <br />
* Step 1: Define parameter
* Step 2: Run programs
* Step 3: Visualization
<br />Detail usage could seen in example script for simulation.


# Version History
* 1.0.0 (27 Jan 2021): contains programs for wavefield and shot modeling using Finite Difference Method (FDM) and Spectral Element Method (SEM) both 2D and 3D Acoustic case. Numerical dispersion is tackled very well by SEM, eventhough the computation is little expensive. In this version, with and without surface related multiple option is available. Spectral Element Method for P-wave 2D Marmousi model using single and multiprocesors examples are provided, as well as geometry assigment and SEGY export.

# Team
* Agus Abdullah, Ph.D.
* Waskito Pranowo, M.T.
* Dicky Ahmad Zaky, M.T.
