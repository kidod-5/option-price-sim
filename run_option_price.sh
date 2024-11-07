#!/bin/bash
# queueing config taken from AMBER18 exx96 GPU runs http://weirlab.wescreates.wesleyan.edu./index\.php?n=Site.18exGPU
#SBATCH --job-name='runOppy'
#SBATCH --output=runOppy.out
#SBATCH --error=runOppy.err
#SBATCH -N 1
#SBATCH --partition=exx96
#SBATCH -B 1:1:1
#SBATCH --cpus-per-gpu=1

#environment for miniconda taken from Henk's notes
#https://dokuwiki.wesleyan.edu/doku.php?id=cluster:73#miniconda3-py311

export PATH=/share/apps/CENTOS7/miniconda3-py311/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/CENTOS7/miniconda3-py311/lib:$LD_LIBRARY_PATH
which mpirun python conda
conda list
export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib:$LD_LIBRARY_PATH

# job specific commands
# testing a python script that will attempt to run on a GPU
#https://dokuwiki.wesleyan.edu/doku.php?id=cluster:73#miniconda3-py311
chmod u+x optionprice.py
# DOES IT WORK?? YES! :)
python optionprice.py


