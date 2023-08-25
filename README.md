[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# [Automation of Strategic Data Prioritization in System Model Calibration: Sensor Placement](https://doi.org/10.1287/ijoc.2022.0128)

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are the software and data used in the research 
(https://doi.org/10.1287/ijoc.2022.0128) by Tianyi Li and Munther Dahleh.

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2022.0128

https://doi.org/10.1287/ijoc.2022.0128.cd

Below is the BibTex for citing this snapshot of the repository.

```
@article{Automation of Strategic Data Prioritization in System Model Calibration: Sensor Placement,
  author =        {T. Li and M. Dahleh},
  publisher =     {INFORMS Journal on Computing},
  title =         {Automation of Strategic Data Prioritization in System Model Calibration: Sensor Placement},
  year =          {2023},
  doi =           {10.1287/ijoc.2022.0128.cd},
  url =           {https://github.com/INFORMSJoC/2022.0128},
}  
```

## Description

The goal of this software is to document the files for conducting sensor placement at system model calibration. 

## Source files

The software is written in Python. The Python package networkx is needed, besides basic packages.

To edit the functions (not recommended):

```
vim funcs.py
```

To edit the parameters (key parameters to edit: handle, k, solver, Matlab_file):

```
vim params.py
```

To run the algorithm:

```
python3 main.py
```

In the data folder, two data files of system models are stored in .mat format. To input a new system model, please convert the model structure into the same format (e.g., using Matlab).

## Results

Show figures in the main text and the online supplement.

## Scripts for replication

Show sample script for replicating the results in Figure 7. 

Change parameters: handle (method for sensor placement), k_max (maximum number of sensors to be placed), d (existing data availability).

## Contact

Please contact tianyi.li@cuhk.edu.hk for questions regarding the software or the paper.
