#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from collections import Counter


# In[2]:


def summary(df):
    a = df.columns
    for i in range(len(df.columns)):
        if np.issubdtype(df[a[i]].dtype, np.number):
            keys = ["Count","Min","1st Q","Median","3rd Q", "Max", "Mean", "St. dev", ]
            values = [df[a[i]].count(), df[a[i]].min(), np.quantile(df[a[i]], 0.25), df[a[i]].median(),np.quantile(df[a[i]], 0.75), df[a[i]].max(), df[a[i]].mean(), df[a[i]].std()]
            
        elif np.issubdtype(df[a[i]].dtype, np.datetime64):
            keys = ["Min","Mean", "Max"]
            values = [df[a[i]].min(), df[a[i]].min(), df[a[i]].max()]

        elif np.issubdtype(df[a[i]].dtype, np.bool_):
            keys = ["Levels", "Frequency"]
            values = [np.unique(df[a[i]]),np.unique(df[a[i]], return_counts=True)]
        elif np.issubdtype(df[a[i]].dtype, np.object_):
            keys = ["Count", "Unique", "Top"]
            values = [df[a[i]].count(), len(np.unique(df[a[i]])), 1 ]

        else:
            continue
        d = dict(zip(keys, values))
        print(a[i])
        for k, v in d.items():
                      print(k,": ", v)
        print('\n')             
        


# In[ ]:




