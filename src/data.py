# https://www.geeksforgeeks.org/data-analysis/exploratory-data-analysis-in-python/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

wr.filterwarnings('ignore')

print('hello')

df = pd.read_csv('../data/train.csv')
print(df.head())
print(df.shape)
print(df.info())
print(df.describe().T)