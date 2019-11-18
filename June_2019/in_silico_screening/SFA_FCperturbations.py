import os
import sfa
import numpy as np
import networkx as nx
import random
from pathlib import Path


class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "network input"

        # Specify the file path for network file in SIF.
        dpath = os.path.dirname(__file__)
        fpath = os.path.join(dpath, 'union.sif')
        # Use read_sif function.
        signs = {'pos_interaction':1, 'neg_interaction':-1}
        A, n2i, dg = sfa.read_sif(fpath, signs=signs, as_nx=True)
        self._A = A
        self._n2i = n2i
        self._dg = dg
        self._i2n = {idx: name for name, idx in n2i.items()}

    # end of def __init__
# end of def class

if __name__ == "__main__":
##    initalize SF Class
    data = ThreeNodeCascade()
    algs = sfa.AlgorithmSet()
    alg = algs.create('SP')
    alg.data = data
    alg.params.apply_weight_norm = True
    alg.initialize()


    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))
###################INPUT FILES
#readout nodes
#readout node steady state values
#readout node sslogFC values
#network nodes
#network node state file
#FC set
##read in readout nodes, readout node attractor state file
    ronfile='ron_ResvVeh_invitro_18'
    readout_nodes=open(ronfile).read().split('\n')

    ronssfile='ron_18_res_ss'
    readout_nodes_state_file=open(ronssfile).read()


##  read in full network nodes, and their initial conditions (normalized expression basal activity)
    network=open('network_nodes.txt').read().split('\n')
    attractor1_file='t2res_basal'
    networkstatesfile=open(attractor1_file).read()
    j=0
    g=0

##  read in FC nodes
    FC=open('FC1').read().split('\n')
#######################################



##  create list of node states (normexp)

    nwstates=networkstatesfile.split('\n') #create list of initial state file
    num_readouts=len(readout_nodes)
    print(num_readouts)
    for node in network:
        #print(node)
        nw_state=float(nwstates[0])
        b[data.n2i[node]]=nw_state #set node to it's initial state

        nwstates.pop(0)



    readout_dict={} #initialize dict for readout nodes values
    fullnetwork_dict={}
    lastpercent=0 #initialize variable for percent convergence with readout attractor states
    timeout=False
    while not timeout:
        #create list of the readout node attractor states
        readout_node_state=readout_nodes_state_file.split('\n')



##  Set FC nodes to randomized activation and inhibitions
        FCdict={}
        for FCnode in FC:
            hi=random.randrange(-1,2,2)
            b[data.n2i[FCnode]]=hi
            FCdict[FCnode]=hi
##  SFA
        x = alg.compute(b)



        quantifier=0
##  clear readout dict and simulation dict so it can hold this iteration's results
        readout_dict={}
        foldchangeDict={}
        for i, act in enumerate(x): #for all nodes (i) and their activity (act) in network
           istr=str(data.i2n[i]) #get node name
##  if i is a readout node, save values to readout_dict, and compare values to logFC
           if istr in readout_nodes: #if this is  a readout node
               readout_dict[istr]=act #set readoutnode value to activity
               given_state=float(readout_node_state[0])#get the attractor state of the readout node

               logFC=round((given_state-act),5)
               foldchangeDict[istr]=logFC

               if given_state<0 and act>0:
                   quantifier=quantifier+1
               if given_state>0 and act<0:
                   quantifier=quantifier+1
               readout_node_state.pop(0)
           fullnetwork_dict[istr]=act


        if (quantifier/num_readouts)>.616:
            timeout=True
            print(quantifier/num_readouts)
            print(quantifier)
            outputfile=open('SFAoutput_18ron_FC1_2.txt','w+') #SFA results
            outputfile.write('node\tsteadstate_value\tDAC\n')
            for k,v in readout_dict.items():
                logFCval=foldchangeDict[k]
                outputfile.write(str(k)+'\t'+str(v)+'\t'+str(logFCval)+'\n')

##  writeout FC configuration
##  create output file for FC configuratoin
            FCout=open('SFAoutput_18ron_FCconfig_FC1_2.txt','w+')
            for key,value in FCdict.items():
                FCout.write(str(key)+'='+str(value)+'\n')
            fullnetworkout=open('SFAoutput_18ron_full_FC1_2.txt','w+')
            for key1,val1 in fullnetwork_dict.items():
                fullnetworkout.write(str(key1)+'\t'+str(val1)+'\n')


            FCout.close()
            outputfile.close()
            fullnetworkout.close()


        if j==100:
            print(j)
            g=+1
            j=0
        j=j+1
    print(g*100)
