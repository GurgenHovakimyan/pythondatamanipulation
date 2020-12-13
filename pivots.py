#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


def pivoting(df, row, column, values):
    """
    Pivoting function helps to look at data in shape that user want.
    
    """
    data = df[[row, column,  values]].to_numpy()
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)
    row_pos = np.sort(row_pos)
    col_pos = np.sort(col_pos)
    col_pos = np.tile(np.unique(col_pos), len(row_pos))
    pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
    pivot_table[row_pos, col_pos[0:len(row_pos)]] = data[:, 2]
    return pivot_table


# In[6]:


def pivvottable(df, row, column, value):
    """
    pivvottable create pivot table and make summary grouped by row and column 
    """
    data = df[[row, column, value]].to_numpy()
    rows, row_pos = np.unique(data[:, 0], return_inverse = True)
    cols, col_pos = np.unique(data[:, 1], return_inverse = True)
    new_list = []
    for i in range(len(rows)):
        a = df.copy()
        a = a[a[row]== rows[i]]
        for j in range(len(cols)):
            b = a.copy()
            b = b[b[column] == cols[j]]
            c = b[value].mean()
            new_list.append(c)
    pivottable = np.array(new_list).reshape(len(rows), len(cols))
    return pivottable

