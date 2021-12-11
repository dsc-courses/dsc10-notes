#!/usr/bin/env python
# coding: utf-8

# # Booleans

# In this short section, we'll see how to ask Python to compare things and discover that Python's answer is of a new type: `bool`.

# ## Comparison Operators

# Beyond arithmetic, Python allows us to compare numbers. For instance:

# In[1]:


3 < 6


# In[2]:


5 > 7


# In[3]:


3 == 3


# The result of these expressions isn't a string, it is a `bool`:

# In[4]:


type(3 < 6)


# A {dterm}`Boolean` (named after [George Boole](https://en.wikipedia.org/wiki/Boolean_algebra)) is a logical data type, indicating whether something is True or False.
# Boolean values result when we use comparison operators to compare the value of two expressions.
# 
# The standard set of comparisons operators carries over from math,
# 
# - `<`: Less than
# - `<=`: Less or equal
# - `>`: Greater than
# - `>=`: Greater or equal
# - `==`: Equal
# - `!=`: Not equal
# 
# Notice that the equal comparison operator distinguishes itself from the assignment operator by using *two* equal signs.

# In[5]:


2 == 2


# In[6]:


3 == 3.0


# In[7]:


1 == 0


# Any expressions to the left or right of the comparison operator will be evaluated before the comparison is carried out.

# In[8]:


(3 * 4) / 6 < 1 + 2 + 3 + 4


# It turns out that we can use comparison operators on many different types of objects! For example, we can use the `==` and `!=` to check if *any* objects are equal in value.

# In[9]:


'Ronaldo' == 'Waldo'


# In[10]:


True != False


# In[11]:


round == round


# And many objects support greater than/less than comparison too. For instance, a string is less than or greater than another string based on alphabetical order.

# ```{margin}
# Technically, string comparisons compare using **lexicographical** order, which just means that text including numbers and symbols is also ordered.
# ```

# In[12]:


"Avocado" < "Banana"


# In[13]:


'Zzyzx' < 'Yosemite'


# Notice that if you look at a dictionary, words like "Fire" will show up before "Fireplace" -- the same holds true with string comparisons in Python.

# In[14]:


"Fire" < "Fireplace"


# ## Summary
# 
# - Lots of objects can be compared using **comparison operators**, `<` `<=` `>` `>=` `==` `!=`, which will return a boolean value.
