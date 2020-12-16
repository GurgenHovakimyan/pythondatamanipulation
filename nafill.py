#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def nafill(df, *colnames):
    columns = list(colnames)
    n = len(columns)
    height = df.shape[0]
    for i in range(n):
        for j in range(height):
            if np.isnan(df[columns[i]][j]):
                df[columns[i]][j] = df[columns[i]].mean()
    return df

