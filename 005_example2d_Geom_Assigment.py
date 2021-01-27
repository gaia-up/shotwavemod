# This script performs Geometry Assignment
# Tested under Ubuntu 18.04.5 LTS
# Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing)
# Agus Abdullah, Ph.D. Waskito Pranowo, M.T. Dicky Ahmad Zaky, M.T.
# Universitas Pertamina - Indonesia  2021


import subprocess
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
subprocess.run(["./geom2d"])

filein = np.genfromtxt('geom2d.par', dtype=str, skip_header=12)
geomfile =  pd.read_csv(filein[9])
print(geomfile)
