#!/usr/bin/env python
# coding: utf-8

# # Expressions
# 
# Now that we know the basics of Jupyter notebooks, we can start exploring Python itself. Before we do, it might interest you to know that most of the pages in this textbook were actually written as Jupyter notebooks -- including this page! In fact, you can see the notebook version of this page by hovering over the rocket icon above and selecting "JupyterHub". This will open the current page as a notebook on JupyterHub.

# ```{figure} ../images/open_as_notebook.gif
# ---
# height: 400px
# name: open-as-notebook
# ---
# Open this page as a notebook.
# 
# ```
# 

# 
# Feel free to experiment by changing the notebook's code cells and running them. Don't worry: the changes will only appear in your notebook, and won't affect the textbook.

# ```{note}
# 
# Keep in mind the philosophy of this book: we'll learn only as much Python as necessary to do data science. This chapter will discuss the absolute basics, and we'll introduce other Python features later in the book when they become necessary.
# ```

# ## Python as a Calculator
# 
# In {doc}`tools`, we mentioned that data scientists use computers as if they are advanced calculators. As such, we'll start our exploration of Python by doing some basic mathematical calculations. At first it might seem like Python isn't any more useful than the calculator app on your phone, but by the end of this chapter you'll start to see why it is such a powerful tool.
# 
# 
# In the last section, we saw how to add two numbers with Python:

# In[1]:


3 + 8


# The first line shows the Python code we write in our notebook's code cell, and the line below shows the output we would see if we were to run that code cell.

# If this isn't amazing enough, Python can subtract, multiply, and divide, too:

# In[2]:


3 - 8


# In[3]:


3 * 8


# In[4]:


3 / 8


# Notice that multiplication is performed by writing an asterisk, `*`, in between two numbers. This is opposed to writing something like `3 x 8`. In fact, if we were to write `3 x 8`, Python would complain:

# In[5]:


3 x 8


# This angry message is called an **exception**. In this case, the exception is a `SyntaxError`. This is Python's way of telling us that we've written some code that it doesn't understand. Remember, a human might understand what is meant by `3 x 8`, but Python doesn't. We have to be careful to use the precise *syntax* that Python expects when writing code -- in this case, it's as simple as writing `3 * 8` instead of `3 x 8`. We'll see more about exceptions later.
# 
# Two other arithmetic operators might be useful to you. To exponentiate a number (raise it to a power), use `**`:

# In[6]:


5**2


# In[7]:


4**.5


# To find the remainder when dividing two numbers, use `%`:

# In[8]:


14 % 5


# The above lines of Python are examples of **expressions**. An expression is a piece of code that can be evaluated to produce a **value**. For instance, `3 - 8` is an expression which evaluates to `-5`. While these examples are of arithmetic expressions, general Python expressions do not need to evaluate to numbers -- they could produce text, matrices (from math), images, etc.
# 
# More complex expressions can be built by combining simpler expressions, as we'll see throughout this textbook.
# In particular, arithmetic expressions can be combined just as you might imagine. For instance:

# In[9]:


(12 + 3)*5 + 40


# Notice the use of parenthesis to group the expression `12 + 3`. Python follows the same order of operations you learned in kindergarten: expressions within parenthesis are evaluated first, then exponentiation, then multiplication, division, addition, and subtraction.

# ```{hiddenanswer}
# ---
# question: Suppose the parenthesis are removed from `(12 + 3)*5 + 40`. What is the result?
# answer: 67
# ```

# ## Example
# 
# How many seconds are in one year? There are 60 seconds in a minute, 60 minutes in an hour, 24 hours in a day, and 365 days in a year, for a total of

# In[10]:


60 * 60 * 24 * 365


# seconds in a normal year.

# ```{hint}
# 
# It is sometimes useful to include a **comment** alongside your code, explaining what it does. In Python, a line starting with `#` is treated as a comment, and is effectively ignored. For instance:
# 
#     # (seconds in a minute) * (minutes in an hour) * (hours in a day) * (days in a year)
#     60 * 60 * 24 * 365
#    
# It is good to comment your code, but don't go overboard -- it is possible to have too many comments! For example, the comment below probably doesn't help:
# 
#     # multiply three and five
#     3 * 5
# 
# ```
