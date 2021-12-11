#!/usr/bin/env python
# coding: utf-8

# # Functions and Imports
# 
# Python is capable of more than just simple arithmetic, of course. It provides many **functions** for performing other operations, like finding the absolute value of a number to computing the cosine of an angle.

# ## Function Call Expressions
# 
# A **function** is a named piece of code that takes in zero or more inputs called **arguments** and (usually) returns something as output. One of Python's simplest functions is called `abs`. Unsurprisingly, it computes the absolute value of the number it is given as input. We can evaluate a function by writing its name, followed by the arguments inside parenthesis, like this:

# In[1]:


abs(-42)


# A function call is an expression, meaning that it it evaluates to a value. Since it is an expression, we can store the result in a variable, as usual:

# In[2]:


my_lucky_number = abs(-7)
my_lucky_number


# The arguments can be expressions themselves, meaning that things like this work:

# In[3]:


x = 4
abs(2*x - 12)


# And since function calls are expressions, they can be combined with other function calls:

# In[4]:


abs(-4) + abs(-2)


# ## Multiple Arguments
# 
# Some functions take more than one argument. `round`, for instance, takes in a (decimal) number as well as the number of decimal places to round to. When we call a function with more than one argument, we separate the arguments with a comma:

# In[5]:


round(3.14159, 2)


# In[6]:


round(3.14159, 4)


# Suppose we want to round a number like 721 to then tens' place, so that it becomes 720. How do we do this with `round`? To get a hint, we can ask Python for help:

# In[7]:


help(round)


# ```{margin}
# 
# You might have noticed that `help` is itself a function. It accepts as its argument *another function*, and prints a help message.
# ```

# This helpful message tells us that the second argument (which is here called `ndigits`) may be negative. What happens if we try that?

# In[8]:


round(721, -1)


# In[9]:


round(721, -2)


# ```{tip}
# 
# A big part of learning to program is experimenting with code to see what does (and doesn't) work. Luckily, Jupyter notebooks make this easy!
# ```

# ```{jupytertip}
# 
# Another way to see a function's help message in a Jupyter notebook is to write the function name, followed by `?`. For instance, to see the documentation for the `round` function, write
# 
#     round?
#     
# by itself in a code cell.
# ```

# ## Importing
# 
# Suppose we need to calculate the base-2 logarithm of a number. Since `abs` finds the absolute value, and `round` rounds, we might expect `log` to find the logarithm. Let's try:

# In[10]:


log(1024)


# Uh oh, we get a `NameError`. This is Python's way of saying that the name we are referring to -- in this case, `log` -- isn't defined, meaning that the kernel doesn't know of such a name.
# 
# It turns out that finding the logarithm isn't popular enough to necessitate a **built-in** function. A built-in function is a function that is available by default in Python. But Python provides many more functions in what are called **modules**. Python comes with plenty of modules, but they are not loaded by default. Instead, we must **import** them.
# 
# For example, Python provides a whole variety of mathematical functions in the `math` module (you can see all of them in the [Python documentation](https://docs.python.org/3/library/math.html)). To import the math module, we write

# In[11]:


import math


# Now we can use the various functions within the module. From looking at the Python documentation, we see that there is a function named `log2` that supposedly calculates the base-2 logarithm of a number. Let's try it out. To call a function in a module, we must preface the function's name with the module name followed by a dot, like this:

# In[12]:


math.log2(1024)


# The math module has many other useful functions, like `math.sin` for computing the sine of an angle, and `math.comb` which will "Return the number of ways to choose k items from n items without repetition and without order." The math module also contains variables, like `math.pi`:

# In[13]:


math.pi


# ## Example
# 
# We saw in the previous section that the number of seconds in a year is

# In[14]:


seconds_in_a_year = 60 * 60 * 24 * 365
seconds_in_a_year


# It turns out that an easy approximation to the number of seconds in a year is $\pi \times 10^7$:

# In[15]:


approximation = math.pi * 10**7
approximation


# How far away is the approximation from the true answer?

# In[16]:


abs(approximation - seconds_in_a_year)


# It appears to be about 120,000 seconds off.

# ```{hiddenanswer}
# ---
# question: How many days is 120,073 seconds? Write some code to calculate the answer and round it to two decimal places.
# answer: |
#     `round(120_073 / (60 * 60 * 24), 2)`, which evaluates to 1.39 days.
# ```

# In[ ]:




