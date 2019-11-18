'''
This file contains code to run FVS. originally published in  doi: 10.1073/pnas.1617387114
adapted from https://github.com/yanggangthu/FVS_python/blob/master/FVS_test.py written by Gang Yang
Default parameters:
T_0 = 0.6, alpha = 0.99, maxMvt_factor = 5, maxFail = 50, randomseed=None
The default values are suggested by the author of the paper.

To identify all minimal FVS, we run 100 simulations with randomseed 1-100
'''

import networkx as nx
import random
import FVS
import re
import csv



outputfile=open('231_FVS_output.txt','w+') #open output file
edges=open('network.txt').readlines() #open file with network edges edges
data=[tuple(line.strip().split()) for line in edges] #creates tuple from file
G3=nx.DiGraph() #initiate networkx graph
G3.add_edges_from(data) #populate networkx graph with edges
#calculate FVS
FVS_sets=[]
i=1
for i in range(1,100):
    G3_FVS1=FVS.FVS(G3, T_0=0.6, alpha=0.99, maxMvt_factor=5, maxFail=50, randomseed=i)
    FVS_sets.append(G3_FVS1)
FVS_set=set(FVS_sets) #only write out unique FVSes
outputfile.write("\n".join(FVS_set))
outputfile.close()
