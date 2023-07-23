## Automation of Strategic Data Prioritization in System Model Calibration: Sensor Placement ##
     
## sample: replication of results in Figure 7

import networkx as nx
import collections
import operator
import math
import numpy as np
import random
from itertools import permutations 
from itertools import combinations 
import copy
import scipy.io as sio
import time

from params import *
from funcs import *

print('-------------------------------------------------------')
print('[Sensor Placement for System Model Calibration (LD2023)]')
print('------------------------ Start ------------------------')
print('------- Sample: replication of Figure 7 results -------')


# Model: O2004 #

Matlab_file = sio.loadmat('../data/O2004.mat')  

# Existing data availability #

d = np.array([1,0,1,0,0,0,0])     # Data availability vector -- vertex_name_list = ['Br','B','P','Dr','D','Pd','A']

# Initialization and FVS #

r,FVS,para,G = Initialization(A,d,r,l,0)  # 1/0:  do/do not print info

##############################################################################

handle = 'Q'            # Q - information entropy; M - missed probability; U - Li & Dahleh (2023)
solver = 1              # 1 - brute force; 2 - simulated annealing; 3 - sequential optimal

print('----> Method:  ' + handle) 
print('----> Solver:  ' + solver) 

## Run ##

for i in range(3):
    
    k = i + 1            # number of sensors to be placed

    print('----> Number of sensors to be placed:  ' + str(k))

    ##############################################################################

    print('----------------------- Running -----------------------')

    # Solver 

    if solver == 1:
        output = Func_Brute_Force_Optimal(A,d,r,l,k,r_new,l_new,handle,1) 

    if solver == 2:
        output = Func_Simulated_Annealing_Optimal(A,d,r,l,k,r_new,l_new,handle,simu_step,1)

    if solver == 3:
        output = Func_Sequential_Optimal(A,d,r,l,k,r_new,l_new,handle,1)

    ##############################################################################

    # Output

    print('----> RESULT: Optimal sensor locations (candidates) ')

    for i in range(len(output)):

        print(output[i])
        
    print('-------------------------------------------------------')

print('------------------------- End -------------------------')