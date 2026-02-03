# Assignment 2: Python Conda Environments

## Overview

This assignment demonstrates creating and managing conda environments with various Python packages for data science and machine learning.

## Files

| File | Description |
|------|-------------|
| [a2_env_versions.ipynb](a2_env_versions.ipynb) | Jupyter notebook displaying package versions |
| [my_env_versions.py](my_env_versions.py) | Python script displaying package versions |
| [testenv.yml](testenv.yml) | Exported conda environment specification |

## Skill Sets (SS1-SS3)

The following skill sets demonstrate Python data structures using a two-file, "separation of concerns" design principle.

| SS1 - Python Lists | SS2 - Python Tuples | SS3 - Python Sets |
|:---:|:---:|:---:|
| [main.py](../skill_sets/ss1_lists/main.py) | [main.py](../skill_sets/ss2_tuples/main.py) | [main.py](../skill_sets/ss3_sets/main.py) |
| [functions.py](../skill_sets/ss1_lists/functions.py) | [functions.py](../skill_sets/ss2_tuples/functions.py) | [functions.py](../skill_sets/ss3_sets/functions.py) |
| ![SS1 Output](img/ss1_lists.png) | ![SS2 Output](img/ss2_tuples.png) | ![SS3 Output](img/ss3_sets.png) |

## Conda Environment

The `testenv` environment was created with Python 3.9 and includes the following packages:

**Installed via conda:**
- jupyterlab
- pandas
- pandas-datareader
- numpy
- matplotlib
- scikit-learn
- django
- seaborn
- nltk
- statsmodels
- scipy

**Installed via pip:**
- tensorflow
- opencv-python
- keras

### Environment List

![Conda Environment List](img/conda_env_list.png)

## Running the Version Script

Activate the environment and run the script:

```bash
conda activate testenv
python my_env_versions.py
```

### Output

![my_env_versions.py Output](img/a2_env_versions_demo.gif)

## Environment Setup Commands

To recreate this environment:

```bash
# Create environment with conda packages
conda create -n testenv python=3.9 jupyterlab pandas pandas-datareader numpy matplotlib scikit-learn django seaborn nltk statsmodels scipy

# Activate environment
conda activate testenv

# Install pip packages
pip install tensorflow
pip install opencv-python
pip install keras

# Export environment
conda env export > testenv.yml
```

Or import from the YAML file:

```bash
conda env create -f testenv.yml
```
