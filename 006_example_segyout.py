# This script performs segy out
# Tested under Ubuntu 18.04.5 LTS
# Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing)
# Agus Abdullah, Ph.D. Waskito Pranowo, M.T. Dicky Ahmad Zaky, M.T.
# Universitas Pertamina - Indonesia  2021
# HOW TO RUN
# Step1: Define parameterization in  segyout.par   (Parameters are from  row 7 to 10 !)
# Step2: Run this Python script via Python IDE or Ubuntu Terminal:  python  006_SEGYOUT.py
# Input:  segyout.par
import subprocess
print("gaiaup 1.0.2 Center for Geosciences Artifical Intelligence and Advanced Computing Universitas Pertamina")
subprocess.run(["./segyout"])

