#!/usr/bin/env python
# coding: utf-8

# # Querying
# 
# The 2018 wildfire season was the worst in California history. How many fires were in 2018? What was their combined size? How many were in San Diego County? These questions could be easily answered if we had a table consisting only of fires from 2018, but our dataset has fires from all years. Creating a new table by selecting only certain rows from an existing table which satisfy some condition is called a {dterm}`query`. In this section, we'll see how to perform queries.

# ## Querying with Boolean Arrays
# 
# Let's start with a simple example. Below, we have created a table containing the population of the five largest cities in California. The table is arranged in alphabetical order:

# In[1]:


import babypandas as bpd
populations = (
    bpd.DataFrame()
    .assign(
        City=['Fresno', 'LA', 'SD', 'SF', 'SJ'],
        Population=[502_000, 4_094_000, 1_376_000, 856_000, 1_023_000]
        )
    .set_index('City')
)
populations


# ```{tip}
# 
# To create a table by hand, start by creating an empty DataFrame with `bpd.DataFrame()`, then use `.assign` to add columns to the table.
# ```

# Suppose we want to know which cities have populations larger than 1 million. We can do so with the following **query**, the result of which is a new table consisting only of the cities whose population is greater than 1 million.

# In[2]:


populations[populations.get('Population') > 1_000_000]


# Let's take a deeper look at what is going on insider of a query. At it's heart is a *comparison*: `populations.get('Population') > 1_000_000`. Recall from {doc}`../01-getting_started/data_types-bool` that a comparison between two numbers results in a {dterm}`Boolean` value (that is, the result is either `True` or `False`). For instance, is we ask if 2 million is larger than 1 million, we get:

# In[3]:


2_000_000 > 1_000_000


# Now, in this case of `populations.get('Population') > 1_000_000`, we are comparing an entire column of the table to a single number, `1_000_000`. What will be the result? As with arithmetic on a table column, comparisons are performed elementwise:

# In[4]:


populations.get('Population') > 1_000_000


# The result is a Series with one entry for every row of the original table. The Series is `True` where the comparison is true and `False` where the comparison is not true. Because each entry of the Series is a Boolean, the result is called a {dterm}`Boolean array` (or, more precisely, a **Boolean series**). The entries of the Boolean array tell us exactly which rows to keep and which rows to discard. If an entry is `True`, we want to keep the corresponding row of the table -- if it is `False`, we should discard that row.

# We can carry out the query and produce a new table by passing the Boolean array into the table using square bracket notation:

# In[5]:


populations[populations.get('Population') > 1_000_000]


# ````{tip}
# Using square brackets on a table can be read aloud as "*where*".
# 
# So the expression
# ```python
# populations[populations.get('Population') > 1_000_000]
# ```
# is read as "the rows *where* the populations is greater than 1 million".
# ````

# It should be mentioned that *any* Boolean array whose length matches the number of rows in the table can be used to select a subset of the table's rows. For instance, we could construct our own Boolean array by hand and get the same result:

# In[6]:


populations[[False, True, True, False, True]]


# Of course, it's usually much more convenient to create the Boolean arrays with comparisons, like `populations.get('Population') > 1_000_000`.

# Lastly, note that if no row satisfies your condition, an empty table will be returned. For instance, no cities have more than 10 million people:

# In[7]:


populations[populations.get('Population') > 10_000_000]


# ## Examples

# Let's get some practice with querying on a larger data set. For this, we'll use the full dataset of California wildfires. While the wildfire dataset we saw previously contained only the 50 largest fires in California history, this dataset will contain *all named fires* since the late 1800's. It is in a file called `calfire-full.csv` in the `data` directory:

# In[8]:


calfire = bpd.read_csv('data/calfire-full.csv')
calfire


# Notice that we haven't set the index of the table. The natural choice of index would be the `'name'` column, but it turns out that several fires have the same name. Remember that row labels should be unique!

# ### How many fires were there in 2018?

# We can determine how many fires there were in 2018 by selecting only those rows where the `'year'` value is equal to 2018 and calculating the size of the resulting table. Remember: to ask if two values are equal, we use `==`, not `=`.

# In[9]:


calfire[calfire.get('year') == 2018]


# The resulting table has 397 rows, which means that there were 397 fires in 2018. We could also get this information with code by using the `.shape` attribute:

# In[10]:


calfire[calfire.get('year') == 2018].shape[0]


# In reality, there were probably many more wildfires than this: the dataset contains only those fires which were large enough to be named.

# ### What was the combined size of all fires in 2018?

# We know how to retrieve only those fires from 2018; we did this above with `calfire[calfire.get('year') == 2018]`. Now we simply ask for the sum of the `'acres'` column:

# In[11]:


area_burned_2018 = calfire[calfire.get('year') == 2018].get('acres').sum()
area_burned_2018


# That certainly *seems* like a large number, but let's put it in perspective. The island of Manhattan is 14,600 acres in area. Therefore, the area burned in 2018 was:

# In[12]:


print(area_burned_2018 / 14_600, 'times the size of Manhattan.')


# ### What percentage of all fires are caused by "arson"?

# We want to select the rows where the cause is due to someone deliberately setting the fire. The `'cause'` column, however, contains strings in a special format, such as `1 - Lightning`, `2 - Eqipment Use`, and so on. To select the fires caused by arson we need to know the exact string to search for.
# 
# We can get this information by asking for the unique values that appear in a column with the `.unique` Series method:

# In[13]:


calfire.get('cause').unique()


# It looks like the right string for arson is `7 - Arson`. Let's perform the query:

# In[14]:


arsons = calfire[calfire.get('cause') == '7 - Arson']
arsons


# To find the percentage of fires caused by arson, we divide the size of this table by the size of the original table:

# In[15]:


arsons.shape[0] / calfire.shape[0]


# So about 5-6% of all wildfires are known to be caused by arson.

# ### How many fires from 2018 occurred in San Diego County?

# We can answer this question by first selecting only the rows from 2018. Using this smaller table, we'll select the rows from San Diego County. This two step process is slightly cumbersome, however -- in the next section, we'll see a better way of performing the same query.
# 
# First, we'll get the fires from 2018:

# In[16]:


fires_from_2018 = calfire[calfire.get('year') == 2018]


# Now we'll select only the fires from San Diego County, making sure to use `fires_from_2018`, and not `calfires`:

# In[17]:


fires_from_2018[fires_from_2018.get('county') == 'San Diego']


# It seems that there were 13 such fires.

# ## Multiple Conditions

# How many fires did San Diego County have in 2018? We saw above that this can be answered with two queries, one after the other. But a more direct and arguably better way is to construct a query with *multiple conditions*, as we'll do now.

# ### The `&` Operator

# Let's begin with another simple example. Below is the table of city populations that we saw at the beginning of this section, but with an additional column containing the region of California that the city is in:

# In[18]:


with_regions = bpd.DataFrame().assign(
    City=['Fresno', 'LA', 'SD', 'SF', 'SJ'],
    Population=[502_000, 4_094_000, 1_376_000, 856_000, 1_023_000],
    Region=['Central Valley', 'SoCal', 'SoCal', 'NorCal', 'NorCal']
).set_index('City')
with_regions


# Suppose we want to select only those cities which 1) have population larger than 1 million, and 2) are in NorCal (Northern California).
# 
# We know how to make Boolean arrays for both queries individually:

# In[19]:


is_more_than_a_million = with_regions.get('Population') > 1_000_000
is_more_than_a_million


# In[20]:


is_in_norcal = with_regions.get('Region') == 'NorCal'
is_in_norcal


# But we want a Boolean array where an entry is `True` if (and only if) *both* of the corresponding entries from `is_more_than_a_million` and `is_in_norcal` are `True`. In other words, an entry should be true if the population is above 1 million *and* the region is NorCal.
# 
# We can construct such an array using the *binary and* `&` operator. `&` takes two Boolean arrays of the same size and returns a new Boolean array that is True only when the input arrays are *both* True.

# In[21]:


is_more_than_a_million & is_in_norcal


# You can check that each entry in this new Boolean array is `True` if and only if the corresponding entries in `is_more_than_a_million` and `is_in_norcal` are both `True`.

# We can now pass this new array into the table to select only the desired rows:

# In[22]:


with_regions[is_more_than_a_million & is_in_norcal]


# In this case, we've assigned each of the two queries to intermediate variables, `is_more_than_a_million` and `is_in_norcal`. This is totally fine, but many times we'll save ourselves the extra typing by writing the query in one line of code:

# In[23]:


with_regions[
    (with_regions.get('Population') > 1_000_000) & (with_regions.get('Region') == 'NorCal')
]


# Notice the `()` around each individual comparison. These are extremely important! If you don't include these, you'll get yelled at by Python:

# In[24]:


with_regions[
    with_regions.get('Population') > 1_000_000 & with_regions.get('Region') == 'NorCal'
]


# ```{warning}
# 
# Always include parentheses `()` around separate conditions in a query with multiple conditions. If you are performing a query, and you see a `TypeError` complaining about an "unsupported operand type", it is likely due to forgetting the parentheses.
# ```

# ```{jupytertip}
# If you forgot parentheses and want to add them quickly, you can select the section of code you want to surround in parentheses and then type `(`. Jupyter will wrap your entire selection in a single pair of parentheses.
# ```

# Lastly, Python is all about readability and &nbsp;a&nbsp;e&nbsp;s&nbsp;t&nbsp;h&nbsp;e&nbsp;t&nbsp;i&nbsp;c.
# 
# If we're inside of parentheses or brackets, we can break up long lines of code to make them easier to read and understand:

# In[25]:


with_regions[
    (with_regions.get('Population') > 1_000_000)
    &
    (with_regions.get('Region') == 'NorCal')
]


# ````{hiddenanswer}
# ---
# question: How would you use `&` to select all 'Class E' fires -- fires which burned at least 300 acres (inclusive) but less than 1000 acres?
# answer: |
#     ```python
#     calfire[(fires.get('acres') >= 300) & (fires.get('acres') < 300)]
#     ```
# ````

# ### The `|` Operator

# Suppose we wanted to select all fires which occurred in either San Diego County *or* Imperial County. In this situation,
# we use the *binary or* operator, `|`. This operator takes two Boolean arrays of the same size as input and creates a new array in which a particular entry is `True` if *at least one* of the corresponding entries in the input arrays is true.

# In[26]:


in_san_diego = calfire.get('county') == "San Diego"
in_imperial = calfire.get('county') == "Imperial"

calfire[in_imperial | in_san_diego]


# ### Never use `and` / `or`!

# You might know that `and` and `or` are valid Python keywords and might wonder why we use `&` and `|` instead. In fact, `and` and `or` *do not* perform the right type of comparison when working with arrays. Your code *will* run, but it will give you the wrong result. Here's a quick example. Suppose we want to get all cities in NorCal with populations larger than 1 million. We write a compound query, but use `and` instead of `&`. The code runs, but is the result correct?

# In[27]:


with_regions[
    (with_regions.get('Population') > 1_000_000) and (with_regions.get('Region') == 'NorCal')
]


# Notice that SF has been included, even though its population is less than 1 million! Why is this? The short answer is that `and` does not do the same thing as `&`. Remember that `&` works elementwise on arrays, returning a new array which is `True` only where both of the input arrays are `True`:

# In[28]:


bpd.Series(data=[True, True, False]) & bpd.Series(data=[False, True, True])


# Now let's try the same thing, but with `and` instead of `&`:

# In[29]:


bpd.Series(data=[True, True, False]) and bpd.Series(data=[False, True, True])


# That's not what we expected!
# 
# For the purposes of this textbook, it's enough to know that `and` doesn't do the same thing as `&`. But if you're curious as to why this happens, here's the short version. We know that Python has Boolean literals `True` and `False`, and `and` works with them as you'd expect:

# In[30]:


True and False


# In[31]:


True and True


# But Python also assigns truth value to other things, like lists and strings. For instance, it is often useful to treat an empty list as if is is `False`, and a non-empty list as if it is `True`. We can see the truth value Python assigns to something by using the `bool` function to convert it to a Boolean:

# In[32]:


bool([1, 2, 3])


# In[33]:


bool([])


# Because of this, we can use `and` between things that aren't `True` or `False`. For instance, we can put it between two lists to make sure that both are non-empty:

# In[34]:


[1, 2, 3] and [4, 5]


# In[35]:


[1, 2, 3] and []


# Note that the output isn't `True` or `False`, it is a list! If we really wanted `True` or `False` for some reason, we could do so with `bool()`:

# In[36]:


bool([1, 2, 3] and [4, 5])


# In[37]:


bool([1, 2, 3] and [])


# But this is the key:  apparently, `and` will produce the second list if both are non-empty. The same thing happens if we use `and` between Boolean series. Take another look at our example from above:

# In[38]:


bpd.Series(data=[True, True, False]) and bpd.Series(data=[False, True, True])


# Notice that what is returned is actually the array on the right hand side of `and`! This almost never what we want when comparing arrays, so remember the following warning:

# ```{warning}
# 
# Never use `and` when writing comparisons in a query. Always use `&`. Likewise, never use `or`; always use `|`.
# ```

# We will use `and` and `or` later on when writing conditionals.

# ## Searching for a Substring

# Wildfires are typically named after the place where they started. For example, fires that start near the border between California and another state or Mexico are often named something like "BORDER #6", or "BORDER #12", etc. We know how to write a query to select all fires with a specific name. For instance, it turns out that there are multiple fires called "BORDER#2".

# In[39]:


calfire[calfire.get('name') == 'BORDER#2']


# But how do we retrieve all fires with "BORDER" somewhere in their names? It turns out that *babypandas* includes a helpful Series method called `.str.contains` which can help us do exactly this. It accepts one argument -- a string -- and searches for it within each entry of the Series, returning a Boolean array. For instance, to find the fires with "BORDER" in their name, we write:

# In[40]:


calfire[calfire.get('name').str.contains('BORDER')]


# ### A Trick to Avoid Spurious Matches

# Many fires are named after roads. Let's count how many:

# In[41]:


calfire[calfire.get('name').str.contains('ROAD')]


# We see several "good" matches, like "NIELSON ROAD" and "CUTOFF ROAD", but several "spurious" matches, like "ROADRUNNER", and "RAILROAD". How can we exclude these fires?
# 
# Here's a trick: instead of searching for strings containing `'ROAD'`, we'll search for strings containing `' ROAD'`,
# where we have added a space to the beginning of the search string. This will match strings like "CUTOFF ROAD", but not "RAILROAD".

# In[42]:


calfire[calfire.get('name').str.contains(' ROAD')]


# Strings have other useful string methods, as well. In this case, all of the fire names are capitalized, but it is common to find that datasets are inconsistent in their capitalization. For instance:

# In[43]:


cities = bpd.DataFrame().assign(names=[
    'San Diego', 'los angeles', 'san luis obispo', 'Oakland', 'Stockton'
])


# Note that some of the strings are not capitalized, while others are. If we want to retrieve all strings that contain `San`, we'll have to write two queries: one for `San` and another for `san`. But there's an easier way.

# A common practice is to make sure all of your text data for a given column is in the same capitalization before selecting on substrings. We can chain together the `.str.lower` method with the `.str.contains` method to quickly achieve this:

# In[44]:


cities.get('names').str.lower()


# In[45]:


cities[cities.get('names').str.lower().str.contains('san')]


# It's worth noting that if you try using the `.str` methods on a Series that doesn't contain text, you'll encounter a helpful error (once you scroll to the bottom).

# In[46]:


calfire.get('year').str.contains('2019')


# ```{tip}
# Often times, when reading an error message it's most helpful to look at the two ends of the message -- and don't get too worried about the middle bits.
# 
# The very top line points to *where* the error occurred, and the very bottom lines explain *why* the error occurred.
# ```

# ## More Examples

# ### What percentage of fires occurred in September or October?
# 
# We'll use `|` to find those fires whose `'month'` is either 9 or 10:

# In[47]:


sept_or_oct = calfire[(calfire.get('month') == 9) | (calfire.get('month') == 10)]
sept_or_oct.shape[0] / calfire.shape[0]


# ### How many fires occurred between San Francisco and LA in terms of latitude?

# The latitude of San Francisco is 37.7749, while the latitude of LA is 34.0522. Selecting all fires within this range can be done with `&`:

# In[48]:


calfire[
    (calfire.get('latitude') <= 37.7749)
    &
    (calfire.get('latitude') >= 34.0522)
].shape[0]


# ### How many fires larger than 1000 acres did San Diego have in the 1990s?

# Now we're having fun! There are three conditions here: 1) Larger than 1000 acres, 2) in San Diego County, and 3) in the 1990s. The third condition, however, is actually two conditions: after 1990 and before 2000.
# 
# With a complex query like this, it's probably best to make the three Boolean arrays separately and save them in intermediate variables, like this:

# In[49]:


is_gt_1000_acres = calfire.get('acres') > 1000
is_in_sd = calfire.get('county') == 'San Diego'
is_in_1990s = (calfire.get('year') >= 1990) & (calfire.get('year') < 2000)


# Now we can perform the query. All three of these conditions must be true simultaneously, so we use `&`:

# In[50]:


calfire[is_gt_1000_acres & is_in_sd & is_in_1990s]

