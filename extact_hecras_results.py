import os
wd=os.getcwd() #request what is the current working directory
print(wd) #show what is the current working directory

# import required libraries
import h5py as h5
import numpy as np
    
# Read H5 file
f = h5.File("model_output.p01.hdf", "r")
print(f.name)
# Get and print list of datasets within the H5 file
datasetNames = [n for n in f.keys()]
for n in datasetNames:
    print(n)

print("################")
l='Results/Unsteady/Output/Output Blocks/Base Output/Unsteady Time Series/Cross Sections/Water Surface'.split('/') 
print(l)
print(f[l[0]][l[1]][l[2]][l[3]][l[4]][l[5]][l[6]][l[7]])
array = np.array(f[l[0]][l[1]][l[2]][l[3]][l[4]][l[5]][l[6]][l[7]][:])
print(array)
print("################")
f.close()

