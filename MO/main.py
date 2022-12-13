import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set()

train = pd.read_csv('E://Programming study/Python study/MO/Life Expectancy Data.сsv')
test = pd.read_csv("E:/Programming study/Python study/MO/test.csv")

train.head()