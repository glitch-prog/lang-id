# https://www.geeksforgeeks.org/data-analysis/exploratory-data-analysis-in-python/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

from pathlib import Path

wr.filterwarnings('ignore')

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

def load_data(path):
    df = pd.read_csv(path, dtype={"text":"string","labels":"string"})
    return df

df = pd.concat(
    [
      load_data(DATA_DIR / "train.csv"),
      load_data(DATA_DIR / "valid.csv"),
      load_data(DATA_DIR / "test.csv"),
    ], 
    ignore_index=True
  )

print(df.info())