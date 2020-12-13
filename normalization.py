#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[1]:


def normalization(df, type = "zscore"):
    """
    with normalization function you can normalize you data with two methods
    by defualt it's zscore method and the second one is minmax normalization
    """
    if type == "zscore":
        for i in range(len(df.columns)):
            a = df.columns
            if np.issubdtype(df[a[i]].dtype, np.number):
                avg = df[a[i]].mean()
                sd = df[a[i]].std()
                for j in range(len(df[a[i]])):
                    df[a[i]][j] = (df[a[i]][j] - avg)/(sd)
            else:
                continue
    elif type == 'normalization':
        for i in range(len(df.columns)):
            a = df.columns
            if np.issubdtype(df[a[i]].dtype, np.number):
                maximum = df[a[i]].max()
                minimum = df[a[i]].min()
                for j in range(len(df[a[i]])):
                    df[a[i]][j] = (df[a[i]][j] - minimum)/(maximum - minimum)
            else:
                continue
    else:
        Print("Only two types of normalization are available: zscore and normalization")
    return df
    


# In[ ]:




