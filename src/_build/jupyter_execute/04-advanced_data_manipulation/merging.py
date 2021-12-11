#!/usr/bin/env python
# coding: utf-8

# ## Merge

# We often find the need to work with data from multiple tables, even when that data is about the same topic! For example, both our wildfire data and our climate data had rows about 2019, or in a separate setting a store might keep track of their sales in one table but keep info on each item sold in a separate table. In either case, we'll likely find it useful to combine the tables and put the data in one place so that we can conduct our analysis. This is called 'merging' or 'joining'.
# 
# Let's entertain the second example in order to see how merging works. Suppose we're a paint retailer, and we keep a table of transactions and a separate table of the paints we sell.

# In[1]:


import babypandas as bpd


# In[2]:


orders = bpd.DataFrame().assign(
    order_number=range(111,111+5),
    item=['BEHR-N2', 'BEHR-N2', 'KM-D4', 'SW-K3', 'VALS-N2'],
    sale=[35.98, 31.08, 28.99, 35.98, 39.77]
)
orders


# In[3]:


paints = bpd.DataFrame().assign(
    item_id=['BEHR-N2', 'KM-D4', 'SW-K3', 'SW-Q0', 'VALS-N2'],
    brand=['Behr', 'Kelley-Moore', 'Sherwin-Williams', 'Sherwin-Williams', 'Valspar'],
    color=['blue', 'red', 'green', 'black', 'blue'],
    weight=[11.4, 8.9, 10.0, 10.1, 9.2]
)
paints


# A logical course of inquiry would be to figure out what kind of paint our customers like to buy, so that we can prioritize marketing and stocking that paint. Congrats, you've just discovered the field of business analytics! You've also discovered the need to merge these two tables.
# 
# Currently we don't know how to write code that would calculate which color of paint sells the most. However, notice that each table has a column with the paints' serial number. We can utilize this to join the tables such that every time a serial number shows up in `orders`, we also include the columns from `paints`.
# 
# We accomplish this with the `.merge` method, and just need to specify the names of the shared column.

# In[4]:


merged = orders.merge(paints, left_on='item', right_on='item_id')
merged


# In calling this method, we're telling Babypandas to take a 'left' and 'right' table and merge the two tables based on shared values in a specific column.
# 
# ![](merging.jpg)
# 
# Notice that an item only shows up in this merged table if it shows up in *both* tables. And an item can show up multiple times if either table has multiple entries for it.

# ```{margin}
# The technical term for this type of merge, where data only shows up if its in both tables, is called an 'inner join'.
# ```

# Since this table join looks at both tables to decide whether to include a row, it doesn't actually matter which table we use as the left versus the right. The only thing that will change is the order of our columns.

# In[5]:


paints.merge(orders, left_on='item_id', right_on='item')


# With the table merge complete, we can easily perform calculations which rely on features from both `orders` and `paints`, such as the distribution of orders across each color of paint, or the average price-per-pound of the paints in our store.

# ````{hiddenanswer}
# ---
# question: What code could you write to plot the categorical distribution of orders of each paint color?
# answer: |
#     ```python
#     merged.groupby('color').count().plot(kind='bar', y='order_number')
#     ```
# ````

# If we're following good table practices, we should really be setting the indices of our tables. So, orders would be indexed by order_number, and paints would be indexed by item_id.

# In[6]:


orders = orders.set_index('order_number')
orders


# In[7]:


paints = paints.set_index('item_id')
paints


# In this case, we'd need to merge using the 'item' column from `orders`, but the *index* of `paints`. To merge on an index, instead of specifying `left_on` or `right_on` we just specify `left_index=True` or `right_index=True`.

# In[8]:


orders.merge(paints, left_on='item', right_index=True)


# Merging is an integral part of data management, and serves as an intermediate step in our analysis. By aggregating data from multiple tables into a single table, we can feel confident in our ability to work with organized data, or even pull in and combine data from various sources!
