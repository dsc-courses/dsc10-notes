#!/usr/bin/env python
# coding: utf-8

# In[1]:


import babypandas as bpd
calfire = bpd.read_csv('data/calfire-full.csv')


# # GroupBy

# What is the most common cause of wildfires in California? We can count the number of fires due to a particular cause, such as lightning, using a query:

# In[2]:


calfire[calfire.get('cause') == '1 - Lightning'].shape[0]


# This query retrieves a table containing only those fires caused by lightning, and `.shape[0]` returns the number of rows in this table, effectively counting the number of such fires.
# To determine the number of fires due to *each* cause, we *could* write a query for each different type of fire:

# ```
# calfire[calfire.get('cause') == '1 - Lightning'].shape[0]
# calfire[calfire.get('cause') == '2 - Equipment Use'].shape[0]
# calfire[calfire.get('cause') == '3 - Smoking'].shape[0]
# ...
# calfire[calfire.get('cause') == '14 - Unknown'].shape[0]
# ```

# But there is a better way. As we'll see in this section, the powerful `.groupby` method allows to quickly *group* a table's rows and perform the same analysis on each group.

# ## Split, Aggregate, Combine

# Let's count the number of fires due to each cause using `.groupby`:

# In[3]:


calfire.groupby('cause').count()


# This result tells us that there were 2550 fires caused by lightning, 399 caused by vehicles, and so forth. But why do all of the columns contain exactly the same information? And what is going on with the column labels? Let's dissect this piece of code to understand what, exactly, is going on.

# Three things happen when we run `calfire.groupby('cause').count()`:
# 
# 1. The table's rows are **split** into groups according to cause. All of the rows whose cause is `'1 - Lightning'` are placed into one group, all of the rows whose cause is `'2 - Equipment Use'` are placed into another group and so on.
# 2. Each group is **aggregated** into a single row by counting the number of entries in each of the group's columns.
# 3. The resulting rows are **combined** to form a new table, with one row for every group.
# 
# {numref}`split-agg-combine` below demonstrates this process on a small example table.

# ```{figure} ../images/split-agg-combine.png
# ---
# name: split-agg-combine
# ---
# caption: The split-aggregate-combine pattern.
# ```

# ### `.groupby`

# The "split" part of the "split-aggregate-combine" process is performed by the `.groupby` method. It accepts a single argument: the column whose values should be used to form groups. When we call `.groupby('cause')`, *babypandas* looks through our table and separates the rows into groups by their value in the `cause` column -- all of the rows whose cause is `'1 - Lightning'` are placed into one group, all of the rows whose cause is `'2 - Equipment Use'` are placed into another group and so on.

# ```{margin}
# 
# To be precise, *babypandas* doesn't immediately create groups when you run `calfire.groupby('cause')`. Instead, it only does this work later, when you use the groups. The technical term for such a function is **lazy**, because it procrastinates. In some cases, being lazy helps the function avoid doing extra work that doesn't need to be done.
# ```

# The result of `.groupby` is something called a `DataFrameGroupby` object:

# In[4]:


calfire.groupby('cause')


# A `DataFrameGroupBy` object doesn't look all that useful by itself. We need to tell *babypandas* what action should be taken on each group. We do this by specifying an **aggregator**.

# ### Aggregators
# 
# After we have grouped the table's rows using `.groupby`, we must next apply an **aggregator**. An aggregator takes each group, aggregates it into a single row, and finally combines these rows to form a new table, with one row for each group with the group's name as its label.  There are several aggregators to choose from, namely:
# 
# - `.mean()`
# - `.median()`
# - `.max()`
# - `.min()`
# - `.count()`

# We have already seen how the `.count()` aggregator can be used to count the number of fires due to each cause. If we instead wanted to find the average size of each type of fire, we could use the `.mean()` aggregator:

# In[5]:


calfire.groupby('cause').mean()


# The average size of each kind of fire is contained in the `'acres'` column.
# 
# When an aggregator is applied to a group, it performs its operation on *each column independently*. For example, the `.mean()` aggregator computes the mean of the `'year'` column, the mean of the `'month'` column, and so forth. So what we see in the table above is the mean year of all fires caused by lightning, the mean month, mean size in acres, and so on.
# 
# Notice that some columns are apparently missing. For instance, the original table has columns called `'name'` and `'county'`, but the table above does not have these columns. This is because they contain strings, and it doesn't make sense to find the mean of a collection of strings. As such, *babypandas* has automatically dropped these column from the result. Likewise, these columns will be dropped if we use the `.sum()` aggregator.
# 
# What if we use the `.max()` aggregator? You might be surprised to find the `'name'` and `'county'` columns in the result:

# In[6]:


calfire.groupby('cause').max()


# Here, *babypandas* adopts the view that the maximum of a collection of strings is the last string in the alphabetical ordering. So for instance, the `ZACA` fire was the fire whose name was alphabetically last among all fires caused by vehicles. Likewise, the `.min()` aggregator will produce the name that is alphabetically first within the group.

# ```{warning}
# 
# The aggregator is applied to each column **independently**. A common mistake is to believe that, after running `calfire.groupby('cause').max()`, the `'acres'` column will contain the size of the largest fire in each group, and the `'name'` column contains its name. This is not the case: the `'name'` column contains the name that appears last in the alphabetical ordering of names within the group.
# 
# ```

# Let's take another look at the count aggregator. Recall the result of our first groupby:

# In[7]:


calfire.groupby('cause').count()


# Notice that all of the columns contain *exactly* the same information. We now know why this is: when we apply `.count()`, it counts the number of entries within the `'year'` column, the `'month'` column, `'name'` column, etc. There are the name number of entries within each column, so we get the same number for each. Also notice that the column names are no longer very meaningful. The `'year'` column no longer contains years -- it contains the *count* of entries in the `'year'` column within each group.
# 
# If our goal is to count the number of fires due to each cause, we could use *any* column in the result -- I usually just pick the one that is easiest to type:

# ```{margin}
# 
# To be precise, the `.count()` aggregator counts the number of *non-null* values in the column. So if there is a `NaN` entry, it will not be counted.
# ```

# In[8]:


calfire.groupby('cause').count().get('year')


# ## Examples
# 
# ***Which year had the largest number of fires?***
# 
# We can count the number of fires from each year with `.groupby()` and `.count()`. But this time we want to group by the year column, so that fires from the same year are placed within the same group.

# In[9]:


calfire.groupby('year').count()


# Notice that the index now contains the different years, since we have grouped by year. To find the year with the largest number of fires, we'll do what we've done before: sort the table and return the last entry in the index:

# In[10]:


calfire.groupby('year').count().sort_values(by='month').index[-1]


# If you're confused why we are sorting by the `'month'` column, remember: all of the columns contain the exact same information after `.count()`! So we could have sorted by the `'county'` column to get the same result:

# In[11]:


calfire.groupby('year').count().sort_values(by='county').index[-1]


# ***What is the median fire size in each county?***
# 
# We'll group by the `'county'` column, and apply the `.median()` aggregator:

# In[12]:


calfire.groupby('county').median()


# If we want just the fire size, we could `.get` the `'acres'` column:

# In[13]:


calfire.groupby('county').median().get('acres')


# ***What was the size of the largest fire in 1995?***

# We will group by year and apply the max aggregator:

# In[14]:


calfire.groupby('year').max()


# Now we want to retrieve the size (in acres) of the fire from 1995. We'll do this with our familiar `.get().loc[]` pattern:

# In[15]:


calfire.groupby('year').max().get('acres').loc[1995]


# ```{tip}
# 
# When method chaining, it is useful to keep in mind what *type* of object you are working with at each step. Any time you write `.`, you should be able to stop and say whether the piece of code to the left evaluates to a table, a series, a number, etc. For instance, `calfire.groupby('year').max()` evaluates to a table, so whatever follows should be a table method.
# ```

# ## `.groupby` versus querying

# In the last example above, we found the size of the largest fire from 1995. We did this with `.groupby()` and the `.max()` aggregator. While this worked, you might have noticed that we can obtain the same result with a simple *query*:

# In[16]:


calfire[calfire.get('year') == 1995].sort_values(by='acres').get('acres').iloc[-1]


# Which is better? And how do we choose which method to use?
# 
# In many cases like this one, both approaches work equally well. In general, however, queries are most useful when asking a question about a *single* group (or subset) of a table, and `.groupby` is most useful when your question is about *each group*. As a rule of thumb, if you question contains the word "each" -- like in "What was the size of the largest fire in each county?" -- you probably want to use `.groupby`.
# 
# Queries have many advantages over `.groupby`. For one, queries can be performed with complex, compound conditions, while `.groupby`'s is limited to forming groups using the values in a particular column. For instance, suppose we want to find the size of the largest fire between 1990 and 2000. We can do this with a query, but not with `.groupby` directly. Second, a query results in a full DataFrame object, while `.groupby` must be followed by one of a limited number of available aggregators.

# ````{jupytertip}
# 
# If you'd like to know how efficient a particular piece of code is, you can use the `%%timeit` "magic function". This runs a cell over and over, printing the average time it takes to execute. Create a new cell with `%%timeit` and the code you'd like to time, like so:
# 
# ```
# %%timeit
# calfire.groupby('year').max().get('acres').loc[1995]
# ```
# 
# This will print something like the following:
# 
# ```
# 62.4 ms ± 161 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
# ```
# 
# This tells us that the code took 62.4 milliseconds to run on average. Not bad!
# ````

# ## Subgroups

# Which month of which year had the most wildfires in California history? To answer this question, we'd like to count the number of wildfires for each month of every year. So for instance, the number of fires in January 1991, February 1991, ..., January 1992, February 1992, ..., and so on.
# 
# This looks like a job for `.groupby` with the `.count` aggregator. But what do we group by? If we group by year, we'll get the number of fires in each year. If we just group by month, we'll get the number of fires in each month *over all years*, which isn't quite what we want:

# In[17]:


calfire.groupby('month').count()


# What we'd like to do is to group rows which are in the same year *and* in the same month. It turns out that `.groupby` supports this via *subgrouping*. We can specify *two* columns to group by using a list. First, "outer" groups will be formed using the first column, then "inner" groups will be formed *within* each outer group using the values in the second column. Here is how it looks in action:

# In[18]:


calfire.groupby(['year', 'month']).count()


# We see something new in the result: *both* the year and the month are being used as the row label. This called a **hierarchical index** (or **multi-index**). Hierarchical indices are quite powerful, but introduce extra complexity. Instead of using multi-indexes, we'll use the `.reset_index()` method to move each level of the index to its own column:

# In[19]:


by_month = calfire.groupby(['year', 'month']).count().reset_index()
by_month


# Which month of which year had the most wildfires? We'll solve this by sorting, as usual:

# In[20]:


by_month_sorted = by_month.sort_values(by='name')


# In[21]:


by_month_sorted.get('year').iloc[-1]


# In[22]:


by_month_sorted.get('month').iloc[-1]

