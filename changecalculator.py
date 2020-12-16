#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def change(df, old, new, symmetry_type = 'symmetric', difference_type = 'logarithmic'):
    change = []
    n = df.shape[0]
    if symmetry_type == 'symmetric':
        if difference_type == 'logarithmic':
            for i in range(n):
                a = np.log(df[new][i] / df[old][i])
                change.append(a)
        else:
            for i in range(n):
                a = (df[new][i] - df[old][i]) / df[old][i]
                change.append(a)
    elif symmetry_type == 'updown':
        if difference_type == 'logarithmic':
            for i in range(n-1):
                a = np.log(df[new][i+1] / df[old][i])
                change.append(a)
        else:
            for i in range(n-1):
                a = (df[new][i] - df[old][i]) / df[old][i]
                change.append(a)
    elif symmetry_type == 'lag':
        print("Warning!!! for lag type function use only old column and calculate lag")
        if difference_type == 'logarithmic':
            for i in range(n-1):
                a = np.log(df[old][i+1]/df[old][i])
                change.append(a)
        else:
            for i in range(n-1):
                a = (df[new][i] - df[old][i]) / df[old][i]
                change.append(a)
    return change

