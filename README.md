# CRCGMMeta-Predictor
The model can be implemented by following the steps.
# Installation
## Requirements
Install the required packages in the Python environment
* RDkit
* pandas
* numpy
* pickle
* bz2file
## Cloning the repository
This model is built as a Python package and can be used in the Python environment.<br/>
Clone the repository and set it as the working directory. <br/>
```
git lfs clone https://github.com/Hema9798/CRCGMMeta-Predictor
```
# Implementation
```
from implementation import CRCGMMetaPredict
res = CRCGMMetaPredict('input puchem SMILES of the query compound')
```
The result will be saved in the res variable.  



