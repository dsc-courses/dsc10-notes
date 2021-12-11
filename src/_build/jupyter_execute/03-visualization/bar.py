#!/usr/bin/env python
# coding: utf-8

# In[1]:


import babypandas as bpd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

climate = bpd.read_csv('../../data/climate.csv')


# # Bar charts

# Whereas scatter plots and line graphs are useful for visualizing the relationship between two *numerical* variables, {dterm}`bar charts` are used to plot a numerical quantity for each value of a *categorical* variable. To create a bar chart, we first pick a categorical variable, then provide a single number for each possible category. We then draw a bar for each category, the height of which is determined by the number we've assigned to eac
