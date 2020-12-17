import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series

ds = randn(100)
# fig = sns.distplot(ds, bins=15).get_figure()
# fig.savefig('multiple plots image1.png')

# fig2 = sns.distplot(ds, hist=False, rug=True, bins=10).get_figure()
# fig2.savefig('multiple plots image2.png')

#change parameter of each graph
# fig3 = sns.distplot(ds, bins=15,
#                     kde_kws={'color': 'red', 'label': 'KDE graph'},
#                     hist_kws={'label': 'Histogram Label', 'color': 'green', 'alpha': 0.5}
#                     ).get_figure()
# fig3.savefig('multiple plots image3.png')

s1 = Series(ds, name='s1')

fig4 = sns.distplot(s1, bins=15).get_figure()
fig4.savefig('multiples plots image4.png')
