## 1. Preliminary Information and Software Setup details

Latest version of this workshop will be available from the following GitHub site,
https://github.com/ravichas/SRWkshp1a. I have used [BINDER](https://mybinder.org/) server to convert workshop materials into dynamic Jupyter notebook(s). The BINDER instance can be accessed (look for launch binder logo) from the [GitHub](https://github.com/ravichas/SRWkshp1a) site. 

GitHub site contains information on how to install Python libraries (via conda) and run the Jupyter notebook on your system. To be clear, you do not need to install any software if you are using our BINDER instance. At a later time, if you want to run the notebook from your computer, then 
[click on this link](software-setup.ipynb).

Please note that this workshop is a continuation of NIH.AI ML Workshop-1 on generating molecular descriptors, [Workshop-1](https://github.com/ravichas/SRWkshp1). Some of the concepts used here are covered in Workshop-1. Please check out the GitHub repository.

I will demonstrate how to build Machine-Learning classification models for predicting small-molecule (drug-like) function (ex., CNS, GI Agent etc.). This is part of the knowledge-transfer efforts of NCI-DOE Pilot projects, [JDACS4C](https://datascience.cancer.gov/collaborations/joint-design-advanced-computing). We will be covering the results of Pilot projects in separate workshop(s). For this workshop, I will use the procedures, tools (python rdkit libraries) and results from the [AMPL](https://arxiv.org/abs/1911.05211) and other Pilot projects to guide us through this effort. Towards this goal, we will follow the AMPL feature steps, data curation (Data; SMILES), featurization (fingerprints), model-training and tuning (Hyperparameter optimization using [CANDLE](https://datascience.cancer.gov/collaborations/joint-design-advanced-computing/candle) and the analysis.

For this workshop, I will use SMILES string data for small molecules from the paper, **Learning Drug Function from Chemical Structure with Convolutional Neural Networks and Random Forests**, *Journal of Chemical Information and Modeling (2019)* You can read details of the work from here, https://www.ncbi.nlm.nih.gov/pubmed/31518132. 