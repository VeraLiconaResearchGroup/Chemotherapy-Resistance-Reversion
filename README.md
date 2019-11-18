# Structure-based Control to Reverse Cisplatin Resistance in Triple Negative Breast Cancer
In this repository we have available the source code for our analysis pipeline to reverse chemotherapy resistance.

Triple-negative breast cancers (TNBCs) are a unique group of clinically aggressive breast cancers for which surgery and chemotherapy are the only available therapeutic modalities. Dr. Ed Liu and his lab, identified a genomic configuration called the tandem duplicator phenotype (TDP) that defines a major subgroup of TNBC. TDP tumors are initially highly sensitive to cisplatin. Despite their initial responsiveness, they develop resistance to cisplatin therapy. The challenge addressed by the proposed project is to test and validate an analysis pipeline to identify therapeutic interventions to reverse cisplatin resistance in TNBC. The objective is to apply structure-based control approaches to identify network node overrides in the form of multiple gene interventions that have the effect of preventing the development of resistance.

## June_2019
This folder contains computations and results for June_2019 grant submission, with multi-omics data from cell lines MDA-MB-231 and MCF10A . There are two subfolders.

### FC_Analysis
This folder contains the results of FC FC_Analysis on the putative intracellular signaling network for MDA-MB-231.
The FC node set of a network is composed of the source nodes (nodes without incoming edges) and of the feedback vertex set problem (FVS) of the network. The FVS problem for a directed graph consists on finding minimal sets of vertices that intersect all cycles of the graph.
The code in this repository has been modified from [Zanudo et al., 2016](https://www.pnas.org/content/114/28/7234):
- FVS_search_10_python.py, FVS.py: code provided by Zanudo et al., 2016 to run FVS module, for other requirements for this code see the [Github repository](https://github.com/yanggangthu/FVS_python)

### <i>in silico</i>\_screening
To trace the dynamics of a signaling network, we can deﬁne a ‘network state’ as a tuple of values of network components at a speciﬁc time point. When there is no change in the input signal of the network system, the network state will follow the inherent network dynamics determined by interactions between network components. Eventually, the network state will converge to a steady state called an attractor.  Using only the static network, we will perform a topological estimation of signal flow, Signal Flow Analysis (SFA), to perform systems’ simulations.

SFA can originally be described in [Lee and Cho, 2018](https://www.nature.com/articles/s41598-018-23643-5). The source code in this repository has been modified from [This Github repository](https://github.com/dwgoon/sfa)
