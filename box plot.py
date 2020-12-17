import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series

#box plot is very useful when u are trying to do stock analysis or market analysis
ds1 = randn(80)
# sns.boxplot(ds1, orient='h').get_figure().savefig('box plot image1.png')
sns.boxplot(ds1, whis=np.inf).get_figure().savefig('box plot image2.png')


