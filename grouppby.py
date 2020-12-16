#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


def grouppby(data, colname, function):
    df = data.copy()
    b = data.columns
    a = []
    for i in range(len(b)):
        if np.issubdtype(df[b[i]].dtype, np.number):
            a.append(b[i])
    print(a)
    n = len(a)
    uniques = data[colname].unique()
    u = len(uniques)
    full = [[None] * n] * u
    for k in range(u):
        filtered = data[data[colname] == uniques[k]]
        for j in range(n):
            if function == 'minimum':
                full[k][j] = filtered[a[j]].min()
            elif function == 'maximum':
                full[k][j] = filtered[a[j]].max()
            elif function == 'mean':
                full[k][j] = filtered[a[j]].mean()
            elif function == 'median':
                full[k][j] = filtered[a[j]].median()
            elif function == 'standard deviation':
                full[k][j] = filtered[a[j]].std()
            else:
                print("Please enter 'min' or 'max' or 'mean' or 'median' or 'sd'")
        print(uniques[k], full[k])

