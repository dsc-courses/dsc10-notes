#!/usr/bin/env python
# coding: utf-8

# In[1]:


import babypandas as bpd
calfire = bpd.read_csv('data/calfire-full.csv')


# # Defining and Applying Functions

# We have seen that Python comes with a bunch of useful functions for performing common tasks. For instance, the built-in `round` function rounds a number to a specified number of decimal places.

# In[2]:


round(3.1415, 2)


# We have also seen that we can access even more functions by installing and importing a library, like *NumPy* or *babypandas*.
# 
# In some cases, however, there might not be a library providing the function that you need. Luckily, Python allows us to define our own functions. In this section, we'll see how to create functions and apply them to tables.

# ## Defining Functions

# Suppose you are working with a dataset containing a bunch of street addresses, such as the following address of the University of California, San Diego:

# In[3]:


ucsd = '9500 Gilman Dr, La Jolla, CA 92093'


# Suppose we only care about the city and state. That is, we'd like to extract the string `'La Jolla, CA'` from the full address. Python doesn't come with a function that does exactly this, but we can write our own without too much work.
# 
# ### Splitting Strings
# 
# A typical address has several parts: the street address, the city name, the state, and the zip code. The parts are separated by commas (with the exception of the state and zip code). Python strings have a helpful `.split` method which will split a string into parts according to whatever delimiter we provide. To split by a comma, we write:

# In[4]:


ucsd.split(',')


# The result is a list of strings, each of them a part of the original list.
# 
# If we do not provide a delimiter, the default behavior of `.split` is to split based on whitespace (such as spaces):

# In[5]:


ucsd.split()


# We can use `.split` to retrieve the city and state name. Notice that when we split by commas, the city name will always be the second-to-last entry of the resulting list. This is because the last comma separates the city from the state and zip code. Remember that we can retrieve the second-to-last element of a list using square bracket notation, combined with using `-2` as the index:

# In[6]:


city = ucsd.split(',')[-2]
city


# The result has a leading space that we might want to get rid of -- we'll deal with that in a moment. For now, let's retrieve the state name. To do this, it might be easiest to split based on whitespace -- then the state abbreviation will again be the second-to-last element of the list:

# In[7]:


state = ucsd.split()[-2]
state


# We'd like to put the city and state together into a single string, like `'La Jolla, CA'`. To do so, remember that the `+` operator *concatenates* strings:

# In[8]:


city_and_state = city + ', ' + state
city_and_state


# This is almost perfect, but let's get rid of the leading space. We can do this with the `.strip()` string method, which removes leading and trailing whitespace.

# In[9]:


city_and_state.strip()


# Great! Putting it all together, here's the code we used to retrieve the city and state:

# In[10]:


city = ucsd.split(',')[-2]
state = ucsd.split()[-2]
city_and_state = city + ', ' + state
city_and_state.strip()


# This code might seem simple enough, but suppose we have another address that we'd like to process:

# In[11]:


lego = 'LEGOLAND California Resort 1 Legoland Dr, Carlsbad, CA 92008'


# We *could* copy and paste the code above, but there is a better way: let's define a function.

# ### The `def` statement
# 
# In Python, new functions are created using the `def` statement. Here is an example of a function which retrieves the city and state name from an address:

# In[12]:


def city_comma_state(address):
    """Return CITY, ST from an address string."""
    city = address.split(',')[-2]
    state = address.split()[-2]
    city_and_state = city + ', ' + state
    return city_and_state.strip()


# There is a lot to say about this, but first let's test the function to see if it works. We call user-defined functions just like any other function:

# In[13]:


city_comma_state('9500 Gilman Dr, La Jolla, CA 92093')


# In[14]:


city_comma_state(ucsd)


# In[15]:


city_comma_state(lego)


# Let's take a closer look at the anatomy of a function definition. {numref}`function` below shows all of the different parts.

# ```{figure} ../images/function.svg
# ---
# width: 80%
# name: function
# ---
# The anatomy of a function.
# ```

# #### Name
# 
# A function definition starts with a name. Above, we've named our function `city_comma_state`, but any valid variable name would do. A function's name should be short but descriptive.
# 
# #### Arguments
# 
# Next come the function's arguments. These are the "inputs" to the function. In this case, there is only one argument: the address that will be processed. We'll see how to define functions with more than one argument in a moment. A function can also have zero arguments, in which case we would write `def function_with_no_args():`. The arguments can be named anything, as long as they are valid variable names. The arguments are surrounded by parentheses, and separated by commas.
# 
# #### Body
# 
# The body of the function contains the code that will be executed when the function is called. The arguments can be used within the body of the function. The body of the function must be indented -- we usually do this with the tab key.
# 
# #### Docstring
# 
# The docstring is a piece of documentation that tells the reader what the function does. Including it is optional but recommended. If you ask Python for information on your function using `help`, the docstring will be displayed!

# In[16]:


help(city_comma_state)


# #### Return
# 
# A function should usually return some value -- this is done using the `return` statement, followed by an expression whose value will be returned.

# ### Function Behavior
# 
# The code we include in a function behaves differently than the code we are used to writing in a couple of key ways.

# #### Functions are "recipes"
# 
# The code inside of a function is not executed until we call the function. For instance, suppose we try to do something impossible inside of a function -- like dividing by zero:

# In[17]:


def foo():
    x = 1/0
    return x


# If you run the cell defining this function, everything will be fine: you won't see an error. But when you *call* the function, Python let's you know that you're doing something that is mathematically impossible:

# In[18]:


foo()


# This is because function definition are like recipes in the sense that handing someone a recipe is not the same as following the recipe and preparing the meal.

# #### Scope
# 
# Variables defined within a function are available only inside of the function. We can define variables inside a function just as we normally would:

# In[19]:


def foo():
    x = 42
    y = 5
    return x + y


# If we run the function, we'll see the number `47` displayed:

# In[20]:


foo()


# However, if we try to use the variable `x`, Python will yell at us:

# In[21]:


x


# This is because variables defined within a function are accessible only within the function. If we want to use that variable outside of the function, we need to pass it back to the caller using a `return` statement.

# ```{margin}
# 
# It is a very good thing that the variables defined inside of a function do not exist outside of a function. For one, good programming practice stresses **encapsulation** -- that is, to keep things simple, we shouldn't need to know exactly what is going on inside of a function to be able to use it. Second, if every variable used inside of a function were available outside of the function, things would get messy very fast. Having a bunch of extra variables -- most of which you'll never use -- is called **namespace pollution**. 
# 
# ```

# Note that arguments count as "variables defined within a function". For instance:

# In[22]:


def foo(my_argument):
    return my_argument + 2


# If we call the function, everything will act as expected:

# In[23]:


foo(42)


# But if we try to access `my_argument` outside of the function, Python tells us that we can't:

# In[24]:


my_argument


# On the other hand, variables defined outside of a function are available inside the function. Consider for instance:

# In[25]:


x = 42
def foo():
    return x + 10


# In[26]:


foo()


# Use this behavior sparingly -- it is usually better to "isolate" a function from the outside world by passing in all of the variables that it needs.

# #### `return` exits the function
# 
# As soon as Python encounters a `return` statement, it stops executing the function and returns the corresponding value. As an example, consider the code below which has three `return`s. Only the first return statement will ever run:

# In[27]:


def foo():
    print('Starting execution.')
    return 1
    print('Hey, I made it!')
    return 2
    print('On to number three...')
    return 3


# In[28]:


foo()


# #### `print`ing versus `return`ing
# 
# As we saw above, functions are somewhat isolated from the rest of the world in the sense that variables defined within them cannot be used outside of the function. The "correct" way of transmitting values back to the world is to use a `return` statement. However, a common mistake is to think that `print` does the same thing. This is understandable, since `print`ing and `returning` looks similar in a Jupyter notebook. For example, let's define a function that both `print`s and `return`s:

# In[29]:


def foo():
    x = 42
    y = 52
    print(y)
    return x


# When we run this function, we'll see both values:

# In[30]:


z = foo()
z


# Only `42` is the *output* of the cell and can be "saved" to a variable. `52`, on the other hand, is simply displayed to the screen and is afterwards lost forever. This can be checked by displaying the value of `z`:

# In[31]:


z


# Nevertheless, using `print` inside of a function can be helpful in "debugging" -- more on that in a moment.
# Lastly, if you truly want to return two values from a function, the right way to do so is by separating them with a comma, as follows:

# In[32]:


def foo():
    x = 42
    y = 52
    return x, y


# When the function is run, it will return a **tuple** of two things:

# In[33]:


foo()


# A **tuple** is like a list, so we can use square bracket notation to retrieve each element:

# In[34]:


foo()[0]


# In[35]:


foo()[1]


# We won't usually need to return more than one thing from a function, though.

# ## Examples
# 
# ***Given a year, produce the decade***

# Given a year, such as 1994, we'd like to retrieve the decade; in this case, 1990. At first we might think that `round` is useful:

# In[36]:


round(1994, -1)


# But it won't work for years like 1997, since it will round up:

# In[37]:


round(1997, -1)


# There are a few approaches that do work. One way is to use the `%` operator. Remember that `x % y` returns the *remainder* upon dividing `x` by `y`. For example:

# In[38]:


1992 % 10


# To find the decade, we can simply subtract the remainder obtained by dividing by ten:

# In[39]:


1992 - (1992 % 10)


# In[40]:


1997 - (1997 % 10)


# In[41]:


2000 - (2000 % 10)


# Placing this code in a function makes it so we don't have to remember this trick, and makes our code more **readable**:

# In[42]:


def decade_from_year(year):
    return year - year % 10


# In[43]:


decade_from_year(1992)


# In[44]:


decade_from_year(1997)


# ***Given height and width, compute the area of a triangle***

# We need to define a function with *two* variables. We do so by separating the argument names with a comma, like so:

# In[45]:


def area_of_triangle(base, height):
    return 1/2 * base * height


# In[46]:


area_of_triangle(10, 5)


# Note that the *order* of the arguments matters. When `area_of_triangle(10, 5)` is executed, Python assigns the value of 10 to `base` and assigns the value of 5 to `height`. If you wish, you can use the keyword argument form to call the function, in which case arguments can be provided in any order. This is slightly more readable, too:

# In[47]:


area_of_triangle(height=4, base=10)


# ***Perform a frequent query***

# Suppose we frequently want to retrieve only those rows of a table whose entries lie between some thresholds. For instance, we
#  might want only those fires in` calfire` from between 1995 and 2000. By writing this query into a function accepting a table, a column, and the thresholds, we make it easy to repeat:

# In[48]:


def between(table, column, start, stop):
    return table[(table.get(column) >= start) & (table.get(column) < stop)]


# For instance, to get only those fires from between 1995 and 2000:

# In[49]:


between(calfire, 'year', 1995, 2000)


# Because this function accepts the column name, it is very reusable. We can use it to get the fires whose size is between 10,000 and 20,000 acres:

# In[50]:


between(calfire, 'acres', 10_000, 20_000)


# Since the `<=` and `>` operators work on strings, too, we can get all of the fires whose name is between A and E:

# In[51]:


between(calfire, 'name', 'A', 'E')


# ## The `.apply` Series Method

# DataFrames come equipped with many useful methods, but defining our own functions allows us to make tables even more powerful. One way to use tables with functions is to pass the table into the function as one of its inputs, as we saw in the example above. In some situations, however, we don't want to apply the function to the entire table, but rather to each entry in one of the table's columns. In these cases, we can use the `.apply` method.
# 
# For instance, suppose we have a table containing a `'year'` column, such as the `calfire` table we have been using, and we want to convert each year into the corresponding decade. We have already written a function that converts a single year to a decade: `decade_from_year`. Recall how it works:

# In[52]:


decade_from_year(1987)


# We'd like to apply this function to each entry in the `'year'` column. To do so, we'll use `.apply`:

# In[53]:


calfire.get('year').apply(decade_from_year)


# Notice the pattern here: we `.get('year')` to retrieve column we wish to work with, and then `.apply(decade_from_year)` to the column. The result is a Series with the same number of entries as the column containing the years. Each entry is the result of applying the function to the corresponding entry of the original column.

# ```{warning}
# 
# Note that we pass the function into `.apply` *without* trailing parentheses. That is, we write `.apply(decade_from_year)` and not `.apply(decade_from_year())` or `.apply(decade_from_year(calfire.get('year')))`. The `.apply` method accepts the name of a function. It will then call the function many times on the given Series.
# ```

# In many cases we'd like to add this new Series back to the table as a new column. We can do so with `.assign`:

# In[54]:


with_decade = calfire.assign(
    decade=calfire.get('year').apply(decade_from_year)
)
with_decade


# The `.apply` method is very useful for **data cleaning**. Data rarely comes to us in the exact form we need or prefer. For instance, we might wish to convert a year to its decade, or remove the leading number code from a fire's cause. A common approach to doing so is to write a function capable of converting or cleaning a single entry, then `.apply`ing this function to the entire column.

# ***Example: clean the `cause` column***

# The `cause` column contains the cause of each fire as string, such as `'14 - Unknown'`. The string contains a number encoding unique to the cause of the fire, but this is redundant since the cause is described immediately after. Let's get rid of the number, leaving only the description.
# 
# First, we'll write a function that accepts a cause and returns only the description:

# In[55]:


def cause_description(cause):
    return cause.split('-')[-1].strip()


# In[56]:


cause_description('2 - Equipment Use')


# Now we `.apply` the function to the `'cause'` column. We'll save it back to the table using `.assign`:

# In[57]:


calfire.assign(
    cause=calfire.get('cause').apply(cause_description)
)

