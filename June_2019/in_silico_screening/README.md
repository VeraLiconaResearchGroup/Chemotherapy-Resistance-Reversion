### <i>in silico</i>\_screening
SFA can originally be described in [Lee and Cho, 2018](https://www.nature.com/articles/s41598-018-23643-5). The source code in this repository has been modified from [This Github repository](https://github.com/dwgoon/sfa)
- SFA_FCperturbations.py: code to predict signal propagation, modified to perform in silico screenings of FC perturbations. This code requires an input network, a set of readout nodes, their steady state value at a given attractor, the network nodes, their basal values, and the FC nodes. The code will compute steady state attractor from the network nodes' basal values + FC perturbation (inhibitions or activations) that satisfies that a user set number of readout nodes are flipped in steady state value from the input (negative to positive, vice versa). The code will output 1) the FC perturbation 2) the steady state values of the readout nodes, 3) the steady state values of all network nodes. This code will be updated to automate the process, and setting the threshold for a successful perturbation pattern. The steady state values are computed as in the following equation:
```x_s=αWx_s+(1−α)b(1−α)(I−αW)−1b
````
where x_s is the log of the activity of node x at the steady state.

- SFAoutput_ron_FC1_2.txt: output of FC perturbation with readout nodes' steady state values, and the computed direction of activity change (DAC) between the perturbation steady state value and input steady state value. The DAC is the difference between these two described values, which is analagous to a logFC.
