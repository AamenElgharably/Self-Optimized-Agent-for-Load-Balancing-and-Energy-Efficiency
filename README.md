# Self-Optimized-Agent-for-Load-Balancing-and-Energy-Efficiency
# Installation
## Installing Prerequisites

1- Install Python 3.8.10 (Do Not use the virtual environment)

2- Install [ns-3.30](https://www.nsnam.org/wiki/Installation) (Follow prerequisites steps and then manual installation (Do not use bake)).
 Notice that:  1- some of the packages to be installed are deprecated with higher Ubuntu versions
			         2-(./build.py) is not applicable for versions less than 3.36. skip it and use (Configuration with Waf) commands. 
			         3- Make sure you run (./waf -enable-tests --enable-examples configure) and (./waf build) before running the test (./test.py)

3- Download [ns3gym](https://apps.nsnam.org/app/ns3-gym/). For versions less than 3.36 download the package in this [link](https://github.com/tkn-tub/ns3-gym/tree/app)


4- Follow installation steps: [ns3gym installation](https://github.com/tkn-tub/ns3-gym). For versions less than 3.36 use the instructions in this [link](https://github.com/tkn-tub/ns3-gym/tree/app)


5- Install tensorflow 2.8.0 and keras 2.8.0. (Do Not use the virtual environment, use pip3). 

6- Install [Stablebasline3](https://github.com/DLR-RM/stable-baselines3).

7- Install mobility models from [here](https://drive.google.com/file/d/1fyL4PGqiqbIlOouuoAEH4TrHVXOqhQWG/view?usp=sharing) and [here](https://drive.google.com/file/d/11UdEeDm5oidBuLs9Ud9w5zmWwloGh8Z3/view?usp=sharing) in /Scratch directory
