from sklearn.decomposition import PCA 
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
from pylab import mpl
import datetime
import time
import math

data = pd.read_csv('./pca/to_one.csv')
# data = pd.read_csv('./pca/data.csv')
pca=PCA(n_components=3, whiten=True)

pca.fit(data)

print (pca.n_components_)

X_new = pca.transform(data)
print(pca.components_)


plt.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2]*10, cmap="jet", marker='o')
plt.show()