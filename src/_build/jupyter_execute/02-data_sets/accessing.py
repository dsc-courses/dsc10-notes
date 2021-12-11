#!/usr/bin/env python
# coding: utf-8

# In[1]:


import babypandas as bpd


# # Accessing and Sorting

# The Cedar Fire left an indelible mark on San Diego county. When it happened in 2003, it was the largest wildfire in California history. Just how big was the fire? And what caused it? The data set we saw in the previous section has these answers, but we still need to learn how to retrieve this information.

# ```{figure} ../images/cedar.jpg
# ---
# height: 300px
# ---
# Cars scramble to leave the 15 as the Cedar Fire crosses the highway and approaches Miramar.
# 
# ```

# ## Accessing with `.loc`

# Let's begin by reading our dataset from a CSV and setting the `'name'` column to be the index:

# In[2]:


calfire = bpd.read_csv('data/calfire.csv').set_index('name')
calfire


# How big was the Cedar Fire? We know that we can retrieve the `'acres'` column using the `.get` method:

# In[3]:


calfire.get('acres')


# The result is a series. We don't see the Cedar Fire listed; it *is* there, just hidden within the `...`. 
# 
# We can retrieve an element from a Series using its row label and the special `.loc` attribute. Since it looks like all the fires have their names capitalized, the row label for the Cedar Fire will be `CEDAR`:

# In[4]:


calfire.get('acres').loc['CEDAR']


# Notice the square brackets in `.loc['CEDAR']`. This is by analogy with using square brackets to retrieve elements from an array.
# 
# To repeat, we can retrieve a particular element in a table, such as the size of the Cedar Fire, by first `.get`ting the column containing the fire sizes, then using `.loc` to retrieve the size corresponding to the Cedar Fire. This is a pattern that we'll be using over and over:
# 
# 1. `.get()` with the column label; then
# 2. `.loc[]` with the row label
# 
# Let's try it again: what was the cause of the Cedar Fire?

# In[5]:


calfire.get('cause').loc['CEDAR']


# Originally, the Cedar Fire was to believed to be caused by a lost hunter shooting their rifle to get the attention of rescuers -- thus the cause is listed as "Equipment Use". However, the hunter later admitted that they had started a signal fire to alert rescuers, and that it quickly spread out of control.

# ```{hiddenanswer}
# ---
# question: What code would you write to determine the county in which the Frying Pan Fire occurred?
# answer: |
#     `calfire.get('county').loc['FRYING PAN']`

# ### Example

# The Cedar Fire was truly huge, stretching from the Cuyamaca Mountains in eastern San Diego County, almost to the Pacific Ocean. But most of us don't have a good sense of what an "acre" is. Instead, let's frame the size of the fire in terms of other things we might be more familiar with. For instance, a soccer field is 1.32 acres. Therefore, the Cedar Fire burned:

# In[6]:


print(calfire.get('acres').loc['CEDAR'] / 1.32, 'soccer fields.')


# Other comparisons are perhaps more surprising. The Cedar Fire burned:

# In[7]:


print(calfire.get('acres').loc['CEDAR'] / 1_976, 'times the size of UCSD\'s campus.')
print(calfire.get('acres').loc['CEDAR'] / 14_600, 'times the size of Manhattan.')
print(calfire.get('acres').loc['CEDAR'] / 382_000, 'times the size of the island of Oahu.')
print(calfire.get('acres').loc['CEDAR'] / 2.9e6 * 100, 'percent of San Diego county.')


# ## Sorting
# 
# While the Cedar Fire was the largest fire in California history when it occurred in 2003, it has since been surpassed. If it wasn't the largest fire, what was?
# 
# One way to answer this question is to sort the table by the size of the fires. We can do this with the `.sort_values` DataFrame method. The method requires one keyword argument, `by=`, which should be given a string with the name of the column to sort by:

# In[8]:


calfire.sort_values(by='acres')


# Notice that the table has been sorted in *ascending* order (from smallest to largest) using the values in the `'acres'` column. Therefore, we see that the largest fire in California history was the Ranch Fire. At 410,202 acres, the Ranch fire was *double* the size of the Cedar Fire. It was part of the Mendocino Complex Fire, which burned in 2019. Although the cause of the fire is listed here as undetermined, it was later discovered that it began when a person tried to plug the entrance of wasp's nest with a hammer and a metal stake. When they hammered the stake, sparks flew and caught the ground on fire. The fire resulted in $250 million in damages.

# What if we want to come to the same conclusion *programatically*, without having to look at the table? After sorting, the last row of the table corresponds to the largest fire, and we want the fire's name. This is stored in the {dterm}`table index`. Remember that the index is essentially an array, and so we can get the last element of the array using square bracket notation:

# In[9]:


calfire.sort_values(by='acres').index[-1]


# Here, we are using {dterm}`method chaining` to save typing.

# ```{margin}
# 
# Actually, we do not need to include the `by=` in this case: calling `.sort_values('acres')` will work just fine. But writing `by=` makes the code more *readable*.
# ```

# ### Sorting in *descending* order

# We could have also made the same discovery by sorting the table in *descending* order. This is done by passing a second keyword argument: `ascending=False`:

# In[10]:


calfire.sort_values(by='acres', ascending=False)


# If this keyword argument isn't given, it defaults to `ascending=True`.
# 
# When sorting in descending order, we could get the fire's name from the index by asking for the first row label:

# In[11]:


calfire.sort_values(by='acres', ascending=False).index[0]


# We can also sort by columns containing strings. In this case, the rows are sorted *lexicographically* -- that is, in dictionary order:

# In[12]:


calfire.sort_values(by='county')


# ### Sorting by multiple columns

# If you look at the help message for `.sort_values`, you'll see that it can also accept a *list* of column names to sort by, like this:

# In[13]:


calfire.sort_values(by=['year', 'acres'])


# In this case, the resulting table will be sorted by the `'year'` column, but within each year the fires will be grouped by their size in the `'acres'` column. Take a look: the fires occurring in 2018 are organized from smallest to largest. Sorting like this is mostly used for presentation purposes.

# ## Accessing with `.iloc`

# How large was the oldest fire in the data set? There are two approaches to answering this question. The first approach uses tools that we already know, but it requires a little extra work. The second approach uses something new: `.iloc`.

# ### Approach #1: with `.loc`.

# In the first approach, we'll first find the name of the oldest fire in the data set. We'll then use this name to ask for the size of the fire using our `.get().loc[]` pattern.
# 
# To get the name of the oldest fire, we'll sort by year and look at the first element of the index:

# In[14]:


oldest_fire_name = calfire.sort_values(by='year').index[0]
oldest_fire_name


# Now we'll use this as the row label in looking up the acreage:

# In[15]:


calfire.get('acres').loc[oldest_fire_name]


# This approach works, but there is a faster way.

# ### Approach #2: with `.iloc`

# After we sort the table by year, we know that the row we're interested in is the first row in the table. But to access the entries of this row with `.loc`, we need to first find out that row's label. Instead of performing this intermediate step, we can get the first row's information directly with `.iloc`.
# 
# Whereas `.loc` looks up a row by its label, `.iloc` looks up a row by its *integer position* (thus the *i* in `iloc`). For instance, suppose we have sorted the table by year and retrieved the acreage column:

# In[16]:


sizes = calfire.sort_values(by='year').get('acres')
sizes


# To get the size of the first fire, we can use `.iloc` directly, without knowing the fire's name.

# In[17]:


sizes.iloc[0]


# This is equivalent to using `.loc` with the column name:

# In[18]:


sizes.loc['GLASS MOUNTAIN']


# To summarize, `.loc` retrieves information using the row label. `.iloc` retrieves information using integer position. It is typically more convenient to use `.loc` with the row label, but sometimes `.iloc` is preferable.
