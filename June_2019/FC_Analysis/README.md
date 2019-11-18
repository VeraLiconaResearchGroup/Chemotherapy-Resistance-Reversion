### FC_Analysis
This folder contains the results of FC FC_Analysis on the putative intracellular signaling network for BR1367 before and after cisplatin treatment, and development of resistance to cisplatin.
The FC node set of a network is composed of the source nodes (nodes without incoming edges) and of the feedback vertex set problem (FVS) of the network. The FVS problem for a directed graph consists on finding minimal sets of vertices that intersect all cycles of the graph.

- FVS_search_10_python.py, FVS.py: code provided by Zanudo et al., 2016 to run FVS module, for other requirements for this code see the [Github repository](https://github.com/yanggangthu/FVS_python)
- FVS_calculation.py: code to calculate FVS for BR1367 intracellular signaling network before and after cisplatin treatment, and before and after development of cisplatin resistance.  Requires input of network edges as 'source_node target_node'
- FVS_output.txt: output of FVS_calculation code. each line contains 1 FVS result from FVS_calculation.py
