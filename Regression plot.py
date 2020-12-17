import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('diamonds').sample(frac=1).head(100)
print df

sns.lmplot('price', 'carat', df).savefig('regression plot image1.png')

#modify
sns.lmplot('price', 'carat', df, scatter_kws={'marker': 'o', 'color': 'green'}, line_kws={'color': 'red', 'linewidth': 1}).savefig('regression plot image2.png')

#higher oder trend line
sns.lmplot('price', 'carat', df, order=4, scatter_kws={'marker': 'o', 'color': 'green'}, line_kws={'color': 'red', 'linewidth': 1}).savefig('regression plot image3.png')

#scatter plot without trend line
sns.lmplot('price', 'carat', df, fit_reg=False).savefig('regression plot image4.png')

#hue argurments
sns.lmplot('price', 'carat', df, hue='cut', markers=['^', 'v', '*', '.', '5']).savefig('regression plot image5.png')
sns.lmplot('price', 'carat', df, hue='cut').savefig('regression plot image6.png')

#local regression
sns.lmplot('price', 'carat', df, lowess=True).savefig('regression plot image7.png')

#regplot
sns.lmplot('price', 'carat', df).get_figure().savefig('regression plot image8.png')

#sub plots
image, (plt1, plt2) = plt.subplots(1, 2, sharey=True)

sns.regplot('price', 'carat', df, ax=plt1).get_figure().savefig('regression plot image9.png')
sns.boxplot(df['carat'], df['depth'], color='green', ax=plt2).get_figure().savefig('regression plot image9.png')

