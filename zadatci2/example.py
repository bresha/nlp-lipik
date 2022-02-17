import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston
boston_housing = load_boston()
print(boston_housing.keys())

boston_df = pd.DataFrame(boston_housing.data, columns = boston_housing.feature_names)

boston_df['TARG'] = boston_housing.target
print(boston_df.head())

sns.set_style("darkgrid")
plt.figure (figsize=(10,6))
sns.distplot(boston_df['TARG'], axlabel = 'srednja vrijednost stanova u vlasništvu u $1000')
plt.show()

boston_corr = boston_df.corr()
plt.figure (figsize=(10,6))
sns.heatmap(boston_corr, annot = True, cmap = 'coolwarm')
plt.show()

plt.figure (figsize=(10,10))
sns.jointplot(x = 'LSTAT', y = 'TARG', data = boston_df, kind = 'reg', size = 10, color = 'orange')
plt.show()

plt.figure (figsize=(10,10))
sns.jointplot(x = 'RM', y = 'TARG', data = boston_df, kind = 'hex', color = 'green', size = 10)
plt.show()