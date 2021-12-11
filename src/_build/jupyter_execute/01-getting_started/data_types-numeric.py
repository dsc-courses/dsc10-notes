#!/usr/bin/env python
# coding: utf-8

# # Numbers

# It might seem that we have only seen one type of data so far: *numbers*. However, Python actually has *two* types of numbers -- *integers* and *floating point numbers* (or *floats*, for short). We have seen both already! Understanding the differences between integers and floats is crucial for any data scientist, as we'll see in this section.

# ## Two Types of Numbers

# Python recognizes two types of numbers: *integers* and *floating point numbers* (or *floats* for short).
# An {dterm}`integer` is a number without decimals. For instance:

# In[1]:


42


# In[2]:


-7


# A {dterm}`float` is a number that *does* have decimals (even if that decimal component is zero), like:

# ```{margin}
# The term 'float' comes from "floating point number", since they're represented by the computer as a value and the position of the decimal point -- so the decimal point can 'float' to any position in the value.
# ```

# In[3]:


3.14159265


# In[4]:


42.0


# When floats get really big or really small they might be printed in scientific notation. You can write floats in scientific notation, too.

# In[5]:


1000000000000000000.0


# In[6]:


1e18


# ```{tip}
# 
# You can place underscores in large numbers to make them easier to read -- Python will ignore them. For instance, it is hard to read `10000000000`, but somewhat easier to read `10_000_000_000`.
# 
# ```

# When we write a number, Python automatically determines whether it is a *float* or an *integer*. We can see the type that Python has determined using the `type` function:

# In[7]:


type(42)


# In[8]:


type(-7)


# In[9]:


type(3.14159265)


# In[10]:


type(42.0)


# We can also use the type function to ask the type of a variable:

# In[11]:


x = 42
type(x)


# In[12]:


y = 7
z = 2
type(y + z)


# ## Types and Arithmetic

# Every value in Python has a type. Since an expression results in a value, we can ask about its type:

# In[13]:


type(1 + 4)


# As we see above, adding and subtracting integers results in an integer. However, if we add an integer and a float, the result will be a float:

# In[14]:


type(1 + 3.1415)


# This makes sense: the result of `1 + 3.1415` is `4.1415`, and so Python treats it as a float because it is a decimal number. But consider this:

# In[15]:


type(1.2 + 3.8)


# Mathematically-speaking, the result of $1.2 + 3.8$ is just $5$, which has no fractional component. But Python treats the result as a float instead of an integer! This might surprise you at first, but Python is following a simple rule here: if the result of arithmetic *could* be a decimal number, the result is a float.
# 
# Let's put that to to the test. Suppose we add two integers. The result cannot have a decimal component, so it will be an integer. But if we add an integer and a float, the result *could* be a decimal number, depending on the exact number used. Therefore the result will be a float.
# 
# ```{margin}
# 
# Why is the result of combining a `float` and an `int` always a `float`? Python doesn't want to make you guess what type something is, so it wouldn't be nice to have the result sometimes be an `int` and sometimes a `float`. If we have to choose between the two, the best choice is clearly `float`.
# ```

# Now you try:

# ```{hiddenanswer}
# ---
# question: Suppose we perform the division `6/3`. What is the type of the result?
# answer: |
#     `float`. Always and forever.
# ```

# Since dividing two integers *could* result in a decimal number, the result is *always* a `float`, even when the answer is mathematically-speaking an integer.

# ```{tip}
# 
# If you find this rule confusing, you can replace it with these two equivalent rules instead:
# 
# 1. When two numbers are combined, with one of them being a float, the result is a float.
# 2. Dividing two numbers results in a float, even if both numbers are integers.
# 
# ```

# ## Conversions

# Sometimes we *know* that something Python thinks is a float should be an integer, or *vice versa*. For instance, we have seen that `6/3` will be a float, even though we know that (mathematically-speaking) the result has no decimal place. We can *convert* a float to an integer using the `int` function, like so:

# In[16]:


int(4/2)


# Likewise, if we want to convert an integer to a float, we use the `float` function:

# In[17]:


float(42)


# Suppose you try to convert a number like `3.14` to an integer. What do you think will happen?

# In[18]:


int(3.14)


# It looks like Python is rounding the number -- but be careful. To be precise, Python is rounding the number *towards* zero:

# In[19]:


int(3.9999)


# In[20]:


int(-2.9999)


# Now you try:

# ```{hiddenanswer}
# ---
# question: Which of the two is bigger? `int(-3.9999)` or `int(-4.0001)`?
# answer: |
#     `int(-3.999)`
# ```

# Since Python rounds the numbers *towards* zero, `int(-3.9999)` will evaluate to `-3` while `int(-4.0001)` will evaluate to `-4` and we know that `-3>-4`.

# ## Integers and Floats *Redux*

# There are some important differences between integers and floats. First, integers can be *arbitrarily* large, while floats can *overflow*. For instance, let's compute $2^{10{,}000}$, first using integers, and then using floats.
# 
# With integers, we write `2**10_000`. The result will be an integer (and a big one, too):

# In[21]:


2**10_000


# Now let's try it with floats. We can do this by writing `2.0**10_000`:

# In[22]:


2.0**10_000


# `OverflowError`! This is Python's way of telling us that the result of the expression is too big for Python to compute using floats.

# ```{margin}
# 
# Without getting too deep into the details, the reason Python can represent huge integers, but not huge floats, has to do with *memory*. Python allows integers to take up as much memory as they want, but requires floats to take up a specific, fixed amount of memory. In the case of an overflow, it would require more memory than allowed to compute the result of the expression. Python limits the memory given to a float in order to ensure that doing computations with floats is very fast.
# ```

# Floating point numbers are also of a fixed precision, meaning that only so many digits can be stored. If we try to compute or store a number with too many decimal places (say, more than 16), Python will "forget" the digits beyond a certain point:

# In[23]:


0.12345678901234567890123


# Here's another example. $1/(2^{10{,}000})$ is a very small decimal number, but it isn't zero. It is too small for Python to calculate using floats, however:

# In[24]:


1/(2**10000)


# Because floats lack some precision, small arithmetic errors called *floating point errors* can result from float operations:

# In[25]:


# should be 251, exactly!
2.51 * 100


# This also means that sometimes something that *should* be zero doesn't seem to be zero, but instead appears to be a super small number.

# In[26]:


(3.0 * 1.2) - 3.6


# This might look like a bug in Python, but it isn't! This is an inherent limitation of *all* programming languages which use floating point numbers (which is most of them). It usually isn't that big of an issue, as long as you're aware of the problem and are careful. For instance, you should get an uneasy feeling when you write code like `int(2.51 * 100)`, because it may not behave the way you'd first expect:

# In[27]:


# "should" be 251!
int(2.51 * 100)


# Now you try:

# ```{hiddenanswer}
# ---
# question: "Python supports a `round()` function that (in simple terms) rounds a decimal to an integer like we do with hand so 3.7 gets rounded to 4 and 3.1 gets rounded to 3. With this in mind, answer the following question:
# 
# Do `int(2.51*100)` and `round(2.51*100)` equivalent?"
# answer: |
#     False
# ```

# As we saw earlier, Python evaluates `2.51*100` to `250.99999999999997`.
# - `int(250.99999999999997)` evaluates to `250`
# - `round(250.99999999999997)` evaluates to `251`

# ## Summary
# 
# - Everything in Python has a type -- these are called **data types**.
# - We can find the type of an object by calling `type` function on an object or expression.
# - Python has two basic number types: `float` and `int`.
# - When faced with division or an expression that involves any floats, the end result will be a float.
