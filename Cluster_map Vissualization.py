import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')
df2 = df.pivot('year', 'match', 'passengers')
print(df2)

sns.clustermap(df2).savefig('cluster1.png')

# sns.clustermap(df2, col_cluster=False).savefig('cluster2.png')

#standardize by rows
# sns.clustermap(df2, standard_scale=0).savefig('cluster3.png')
