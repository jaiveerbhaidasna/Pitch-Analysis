# -*- coding: utf-8 -*-
"""pitchanalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tnP2e88G9Usv0PZs6rdjUuzNywHrWvQv
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install pybaseball
# %pip install --upgrade ipykernel

# Commented out IPython magic to ensure Python compatibility.
# %pip install Cmake
# %pip install wheel
# %pip install coincurve
# %pip install tensorflow
!pip3 uninstall --yes torch torchaudio torchvision torchtext torchdata
!pip3 install torch torchaudio torchvision torchtext torchdata

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

import pybaseball as pb
from pybaseball import statcast

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pb.cache.enable()

data = statcast(start_dt="2023-03-30", end_dt="2023-11-01")

dataframe = data[['pitch_type', 'release_speed', 'release_pos_x', 'release_pos_z', 'p_throws', 'pfx_x', 'pfx_z', 'plate_x', 'plate_z']]

pitchSet = set(['CH','CU','FC','EP','FO','FF','KN','KC','SC','SI','SL','SV','FS','ST'])

class PitchDataset(Dataset):

  def __init__(self, dataframe):
    self.pitch_type = dataframe['pitch_type']

  def __len__(self):
    pass

  def __getitem__(self, index):
    return

dataframe = dataframe.sort_values(by = ['pitch_type'])
dataframe['pitch_type'] = dataframe['pitch_type'].astype('category')
pitch_dict = dict(zip(dataframe.pitch_type.cat.codes, dataframe.pitch_type))
dataframe['pitch_type'] = pd.factorize(dataframe['pitch_type'])[0]
dataframe = dataframe[dataframe.pitch_type != -1]

dataframe = dataframe.sort_values(by = ['p_throws'])
dataframe['p_throws'] = dataframe['p_throws'].astype('category')
p_throws_dict = dict(zip(dataframe.p_throws.cat.codes, dataframe.p_throws))
dataframe['p_throws'] = pd.factorize(dataframe['p_throws'])[0]

print(p_throws_dict)

print(pitch_dict)

print(dataframe)
#print(dataframe.pitch_type.unique())