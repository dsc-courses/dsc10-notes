#!/usr/bin/env python
# coding: utf-8

# # DataFrames

# Most of the data sets that we are interested in are more complex that simple lists of numbers. For instance, consider a data set containing information about California wildfires. It might contain multiple pieces of data about each fire, including its name, size, location, and cause.
# 
# How would we store and analyze such a data set? While we could use NumPy arrays -- one holding the fire's name, another holding the size, etc. -- there is a much better way: We will use a *table* to contain the data, like this:

# In[1]:


import babypandas as bpd
fires = bpd.read_csv('../../data/calfire.csv')
fires


# ## Pandas DataFrames

# Like NumPy arrays, tables are provided by a third-party extension. The Python package which provides tables is called [pandas](https://pandas.pydata.org/). Pandas is *the* tool for doing data science in Python, and it is immensely popular -- as of Summer 2020, it was downloaded nearly *1 million* times per day. It is without a doubt a powerful tool, and you'll need to know how to use it if you want to do serious data science. But there's a problem: pandas is complicated. There are numerous ways to do even the simplest tasks. This makes it hard to learn, especially if you're new to programming.
# 
# This leaves us in an interesting situation. On one hand, we want to learn pandas, because it is *the* tool used by actual data scientists. On the other hand, we don't want to be thrown into the deep end. The solution? We'll take pandas and remove everything that isn't absolutely necessary, resulting in something simpler and easier to learn. What's left is still *pandas* -- just not all of it. Because this new package is a smaller (and cuter) version of pandas, we're calling it *babypandas*.
# 
# To get access to the functionality that *babypandas* provides, we'll need to import it:

# In[2]:


import babypandas as bpd


# ```{margin}
# 
# Remember that the syntax `import something as new_name` imports the package named `something`, giving it the new name `new_name`.
# It is a convention among data scientists to rename `pandas` to `pd` by writing `import pandas as pd`, so we will rename `babypandas` to `bpd`.
# ```

# ```{note}
# 
# We're going to be using *babypandas* in the rest of this book, but it should be stressed that *babypandas* is *pandas*, just a smaller version of it. So if someone asks if you have experience working with *pandas* (during a job interview, for instance), you'll be able to say "yes!".
# ```

# In *babypandas* (and *pandas*), a table is called a {dterm}`DataFrame` (though we'll use the two terms interchangeably). Since DataFrames are often used to store very large data sets, they are not typically created by typing their entries one by one -- instead, they are usually read from a file. We'll see how to do that in a moment, but for now we assume that we have already loaded a DataFrame into a variable called `fires`. If we type `fires` in our Jupyter notebook cell and execute it, it will display the table with nice formatting:

# In[3]:


fires


# If we ask for the `type` of `fires`, Python will tell us that it is a DataFrame:

# In[4]:


type(fires)


# A DataFrame consists of *columns* and *rows*. Almost always, a row represents a single thing -- in this case, a fire -- and the columns provide different pieces of information about that thing. In this case, we have a column describing the name of the fire, another describing the cause, and so on.

# We can get the number of rows and columns in a *DataFrame* by asking for its {dterm}`shape`:

# In[5]:


fires.shape


# This tells us that there are 50 rows and 9 columns. If for whatever reason we just wanted the number of rows, we could ask for the first element of this pair:

# In[6]:


fires.shape[0]


# Every row and column in a DataFrame has a *label*. We will use the row and column labels to refer to particular parts of the table and retrieve information from within it. The columns of the above DataFrame are labeled "year", "name", "cause", and so on. The rows of the above table are simply labeled "0", "1", "2", and so forth.

# ## The Index

# Together, the row labels are called the {dterm}`table index`.
# By default, a table's rows are labeled by numbering them. However, in many cases it makes more sense to label the rows in some other way. For example, each row in our current data set is a single fire. Perhaps it makes more sense to use the fire's name as its row label. We can ask *babypandas* to use a particular column as the row labels with the `.set_index` method:

# ```{margin}
# 
# You might know that NumPy arrays can be two-dimensional, too, so they *could* be used to store tables. But NumPy arrays do not have an *index*.
# ```

# In[7]:


fires.set_index('name')


# The `.set_index` method accepts one argument: the label of the column that should be used as the index. It then creates a *new* DataFrame in which the index has been replaced with the information from this column; the old DataFrame is not changed. In order to save the results, we'll need to assign the new table to a variable, like so:

# In[8]:


fires_by_name = fires.set_index('name')
fires_by_name


# Notice that the fire names have been moved all the way to the left, and have been made bold -- this is *babypandas*' way of showing that these names are now the index.

# ```{warning}
# 
# The index is *not* a column -- it is it's own separate thing. When we use `.set_index`, the old index is thrown out and number of columns decreases by one.
# ```

# Since we will later use row labels to refer to specific rows by name, the labels should be unique. In this case, that means that every fire should have a unique name. In this case, every fire is uniquely named, and it is fine to use the fire name as the index. Later, we'll see a larger version of this data set in which there are multiple fires with the same name. In that case, the name should probably not be used as the index.

# A table's index is essentially an array. We can get the index by writing:

# In[9]:


fires_by_name.index


# We can then access individual elements of the index using the same notation as used with arrays, remembering that Python starts counting from zero:

# In[10]:


# the first element
fires_by_name.index[0]


# In[11]:


# the second element
fires_by_name.index[1]


# In[12]:


# the last element
fires_by_name.index[-1]


# ## Series

# ### Getting a column with `.get`

# We can retrieve a particular column from the table with the `.get` method. For instance, to get the column labeled "acres", we would write:

# In[13]:


fires_by_name.get('acres')


# The result might look like a DataFrame with one column, but it's actually a new type of object called a *Series*:

# In[14]:


type(fires_by_name.get('acres'))


# A *Series* is basically an array, but with an index. A *Series* represents a column in a *DataFrame*. This means that we can think of the columns of a DataFrame as being arrays (more or less).

# ### Arithmetic

# Because a Series is like an array, we can do similar things with it. For instance, we can perform elementwise arithmetic with a Series. Let's try it out by converting the fire sizes from acres to square miles. Each acre is 0.0015625 square miles, so we can do the conversion with a simple multiplication:

# In[15]:


fires_by_name.get('acres') * 0.0015625


# We can also perform arithmetic with two series, assuming that they are the same size.

# ### Series methods: `.mean`, `.max`, `.describe`, etc.

# *Series* objects also come with a bunch of useful methods attached, like `.mean` and `.max`. For example, the average size of a fire in this data set is:

# In[16]:


fires_by_name.get('acres').mean()


# The largest fire burned this many acres:

# In[17]:


fires_by_name.get('acres').max()


# And the earliest fire in the data set was in the year:

# In[18]:


fires_by_name.get('year').min()


# A very useful *Series* method is `.describe`. It gives us a quick look at the basic statistics of the data in a particular column:

# In[19]:


fires_by_name.get('year').describe()


# From this, we can see that there are 50 fires in the data set, the earliest from 1910 and the latest from 2019. The 25%, 50%, and 75% refer to *percentiles*. That is, 25% of the fires occurred during or before 1996, and half occurred during or before 2007. This also means that half occurred between 2007 and 2019!

# We will see more Series methods throughout this textbook, but only when we need to use them.

# ```{jupytertip}
# 
# You can ask Jupyter for some information on all of the Series methods available by writing `help(bpd.Series)`. The methods starting with two underscores (`__`) are called "dunder" methods, and implement special behavior. You're not meant to call them direcly, so you can pretty much ignore them.
# ```

# ## Adding and removing columns

# Above, we saw that we could convert the `'acres'` column to square miles using a little bit of array math. But doing so doesn't change the table. What if we want to add this column to our table?
# 
# ### Adding a column with `.assign`
# 
# Adding a column can be done with the `.assign` method, like this:

# In[20]:


fires_by_name.assign(sqmiles=fires_by_name.get('acres') * 0.0015625)


# There's a lot going on here, so let's break it down. First, the assign method takes a single argument: a series that will become the new column. But the way that we pass this argument is new. Instead of simply passing the argument itself, we also give the argument a name by writing `sqmiles=`. This will be the column's label. Arguments written in the form `argument_name=argument_value` are called {dterm}`keyword arguments`.
# 
# We can call the column anything we like, as long as it is a valid python variable name. This means that the variable name cannot contain spaces, or start with a number. If you try, you'll get a `SyntaxError`:

# In[21]:


fires_by_name.assign(square miles=fires_by_name.get('acres') * 0.0015625)


# Instead of spaces, we can use underscores:

# In[22]:


fires_by_name.assign(square_miles=fires_by_name.get('acres') * 0.0015625)


# The second thing to note is that `.assign` creates an entirely new table containing the new column. It does not change the old table, as we can verify by recalling the value of `fires_by_name`:

# In[23]:


fires_by_name


# ```{note}
# 
# Wherever possible, DataFrame and Series methods return *new* objects instead of modifying existing ones. Creating copies like this results in code that is easier to reason about helps prevent strange bugs in your code.
# ```

# In order to permanently add the column to the table, we need to save the result of `.assign` to a variable.

# In[24]:


fires_with_sqmiles = fires_by_name.assign(
    sqmiles=fires_by_name.get('acres') * 0.0015625
)
fires_with_sqmiles


# ### Removing a column with `.drop`

# Columns can be removed using the `.drop` method. It accepts one keyword argument: `columns`. The argument can either be the label of a single column as a string, or a list of column labels. As with `.assign`, the result is a new DataFrame (a copy).
# 
# For example, to get rid of the `'sqmiles'` column:

# In[25]:


fires_with_sqmiles.drop(columns='sqmiles')


# If we didn't want the cause or the county:

# In[26]:


fires_with_sqmiles.drop(columns=['cause', 'county'])


# Note that the argument name (`columns`) is not something we can change, unlike the keyword argument name used in `.assign`. We *must* use `columns=...`, or else Python will not understand us. And if you don't use the keyword name, Python will be upset:

# In[27]:


fires_with_sqmiles.drop('county')


# ### Renaming columns

# How do we rename a column? Suppose we want to rename `sqmiles` to `square_miles`. To do so, we:
# 
# 1. Add a new column with the desired name by copying the old column.
# 2. Drop the old column

# For instance:

# In[28]:


fires_with_new_name = fires_with_sqmiles.assign(
    square_miles=fires_with_sqmiles.get('sqmiles')
)
fires_with_new_name.drop(columns='sqmiles')


# We can also do this in a single piece of code, without intermediate variables:

# In[29]:


(
    fires_with_sqmiles
    .assign(square_miles=fires_with_sqmiles.get('sqmiles'))
    .drop(columns='sqmiles')
)


# ```{tip}
# 
# You can break up long expressions by surrounding the whole expression with parentheses and inserting line breaks wherever makes sense. We'll often break right at a method call.
# ```

# This trick of applying two methods, one after the other, in one line of code is called {dterm}`method chaining`. It works because the result of `.assign` is itself a table. When Python evalautes the expression, it first evaluates the `.assign`, then uses this table during the call to `.drop`.
# 
# Method chaining is useful and can save us some typing, but it can be overused. It is sometimes better to save intermediate results.
# 
# ```{tip}
# If your method-chaining code isn't working as you'd expect, break apart the code and save intermediate variables. Print out the values of these variables to do some debugging.
# ```

# ## Reading CSV files

# As mentioned above, DataFrames are not typically created by typing their entries by hand, one-by-one. Instead, we usually download a data set in a standard format and read it from disk. One such standard format is {dterm}`CSV`, or *comma-separated values*.

# A CSV file is simply a text file in a certain format. Here are the first few lines of the CSV file containing our wildfire data:

# In[30]:


get_ipython().system('head ../../data/calfire.csv')


# As it's name suggests, a CSV file consists of values, separated by commas. The first line of the file usually contains the column labels. CSV is a widely-used format, and can be read by many pieces of software, including Excel and Google Sheets.

# We can read a CSV file into a *babypandas* DataFrame using the `bpd.read_csv` function. We give this function a string containing the filepath to the CSV file we want to read. For example, our wildfire data exists in a file called `calfire.csv` contained in the `data/` directory. We can read it into a DataFrame as follows:

# In[31]:


calfire = bpd.read_csv('data/calfire.csv')
calfire


# Modifying the DataFrame will not affect the data on disk in any way.

# ```{margin}
# 
# If you do want to save your changes, you can do so with the `.to_csv` DataFrame method.
# ```
