# Conda Installation Instructions.

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

##  Linux

Tested on Ubuntu 18.04

**Anaconda**:

    wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
    sh Anaconda3-5.2.0-Linux-x86_64.sh -b
    echo export PATH=\"${HOME}/anaconda3/bin:\$PATH\" >> ${HOME}/.bashrc

**Miniconda**:

    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-Linux-x86_64.sh -b
    echo export PATH=\"${HOME}/miniconda3/bin:\$PATH\" >> ${HOME}/.bashrc

## Update

    conda update -n base conda

