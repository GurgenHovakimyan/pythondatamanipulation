#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from secondary_module import isNaN
from collections import Counter


# In[2]:


def nafill(df, *colnames):
    """
    nafill function fills nan cells with mean of each column.
    df -> dataframe
    *colnames -> names of the columns whete nans' must be filled
    """
    columns = list(colnames)
    n = len(columns)
    height = df.shape[0]
    for i in range(n):
        for j in range(height):
            if np.isnan(df[columns[i]][j]):
                df[columns[i]][j] = df[columns[i]].mean()
    return df


# In[3]:


def dropna(df):
    """
    Delete rows that contain nans.
    df -> dataframe.
    """
    lst = []
    nd = np.array(df)
    for i in range(nd.shape[0]):
        for j in range(nd.shape[1]):
                if isNaN(nd[i][j]):
                     lst.append(i)
    indx = set([i for i in range(len(df))])
    not_nan = list(set(indx).difference(set(lst)))
    drop_nan = nd[not_nan]
    return drop_nan


# In[4]:


def summary(df):
    """
    The summary function summarizes the dataframe by columns.
    df -> dataframe
    """
    a = df.columns
    for i in range(len(df.columns)):
        if np.issubdtype(df[a[i]].dtype, np.number):
            keys = ["Count","Min","1st Q","Median","3rd Q", "Max", "Mean", "St. dev"]
            values = [df[a[i]].count(), df[a[i]].min(), np.quantile(df[a[i]], 0.25), df[a[i]].median(), 
                      np.quantile(df[a[i]], 0.75), df[a[i]].max(), df[a[i]].mean(), df[a[i]].std()]
            
        elif np.issubdtype(df[a[i]].dtype, np.datetime64):
            keys = ["Min","Mean", "Max"]
            values = [df[a[i]].min(), df[a[i]].min(), df[a[i]].max()]

        elif np.issubdtype(df[a[i]].dtype, np.bool_):
            keys = ["Levels", "Frequency"]
            values = [np.unique(df[a[i]]),np.unique(df[a[i]], return_counts=True)]
        elif np.issubdtype(df[a[i]].dtype, np.object_):
            keys = ["Count", "Unique"]
            values = [df[a[i]].count(), len(np.unique(df[a[i]]))]

        else:
            continue
            
        d = dict(zip(keys, values))
        print(a[i])
        
        for k, v in d.items():
                      print(k,": ", v)
        print('\n')  


# In[5]:


def normalization(df, type = "zscore"):
    """
    Normalization function can normalize the data by two methods. 
    df -> dataframe
    type -> The method used for normalization. The defualt option is the z-score method. And the optional one is the 
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
    elif type == 'minmax':
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
        Print("Only two types of normalization are available: zscore and minmax")
    return df
    


# In[6]:


def change(df, old, new, symmetry_type = 'symmetric', difference_type = 'logarithmic'):
    """
    With this function you can calculate difference(change) between two variables expressed in percentages.
    df -> dataframe
    old -> old value column denominator
    new -> new value column numerator
    symmetry_type -> contains three types of symmetries. 1)symmetric: takes values from the same row. 
                     2)Updown: takes the values for numerator from row below and the values for denominator 
                                from the row above.
                     3)lag: calculates the difference between current and previous(lagged) values
    difference_type -> logarithmic is the most important approach. However, the only problem is that all the variables 
                        must be either negative or positive. 
                        Otherwise, there will be an error. In that case the difference will be calculated
                        in the classical way.
    
    """
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


# In[7]:


def pivoting(df, row, column, values):
    """
    Pivoting function helps to look at the dataframe in the shape that the user wants.
    df -> dataframe
    row -> which column must be transformed into a row in pivot
    column -> which column must be transformed into a column in pivot
    values -> the variable the pivot must be filled with    
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


# In[8]:


def pivvottable(df, row, column, value, function = 'median'):
    """
    pivvottable creates a pivot table and makes a summary grouped by a row and a column
    df -> dataframe
    row -> which column must be transformed into a row in pivot
    column -> which column must be transformed into a column in pivot
    values -> the variable the pivot must be filled with 
    function -> function that aggregates the pivot table
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
            if function == 'mean':
                c = b[value].mean()
            elif function == 'min':
                c = b[value].min()
            elif function == 'max':
                c = b[value].max()
            elif function == 'median':
                c = b[value].median()
            elif function == 'standard deviation':
                c = b[value].std()
            else:
                print("Please enter 'min' or 'max' or 'mean' or 'median' or 'standard deviation'")
            new_list.append(c)                  
    pivottable = np.array(new_list).reshape(len(rows), len(cols))
    return pivottable


# In[9]:


def grouppby(data, colname, function):
    """
    Group by groups data frame by a specified column and aggregates by specified function.
    data ->  dataframe
    colname -> column that the groupping is based on.
    function -> aggregation function.
    """
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


# In[ ]:




