#!/usr/bin/env python3
"""Display Python and package versions for the testenv conda environment."""

import sys

# Print Python version
print("Python version:")
print(f"{sys.version}\n")

# Import and print package versions
import jupyterlab
print(f"jupyterlab: {jupyterlab.__version__}")

import pandas
print(f"pandas: {pandas.__version__}")

import pandas_datareader
print(f"pandas_datareader: {pandas_datareader.__version__}")

import numpy
print(f"numpy: {numpy.__version__}")

import matplotlib
print(f"matplotlib: {matplotlib.__version__}")

import sklearn
print(f"sklearn: {sklearn.__version__}")

import django
print(f"django: {django.__version__}")

import tensorflow
print(f"tensorflow: {tensorflow.__version__}")

import scipy
print(f"scipy: {scipy.__version__}")

import keras
print(f"keras: {keras.__version__}")

import seaborn
print(f"seaborn: {seaborn.__version__}")

import cv2
print(f"cv2 (opencv-python): {cv2.__version__}")

import nltk
print(f"nltk: {nltk.__version__}")

import statsmodels
print(f"statsmodels: {statsmodels.__version__}")
