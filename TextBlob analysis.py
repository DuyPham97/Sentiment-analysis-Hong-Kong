#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Divide into 10 bins
sentiment_df = pd.read_csv('HongKong.csv')

fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram with break at zero
sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="purple")

plt.title("Sentiments from Tweets on Hong Kong")
plt.show()


# In[3]:


#Binary result; 0 or 1
fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram with break at zero
sentiment_df.hist(bins=[-1, 0.0, 1],
             ax=ax,
             color="purple")

plt.title("Sentiments from Tweets on Hong Kong")
plt.show()

