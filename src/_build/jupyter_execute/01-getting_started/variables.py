#!/usr/bin/env python
# coding: utf-8

# # Variables
# 
# When performing a long computation, it is often useful to store the result of a calculation so that we can do this later. In most programming languages, we can do this by giving a *name* to the result of an expression.
# 
# As always, remember that you can follow along by clicking the link under the rocket icon at the top of the page to launch the Jupyter notebook version of this page!

# ## Assigning Names
# 
# The result of an expression can be given a name using `=`. For example:

# In[1]:


the_answer_to_everything = 21 * 2


# This line of code stores the number `42` in a **variable** named `the_answer_to_everything`. We can later reference this values by name in expressions contained in other cells:

# In[2]:


the_answer_to_everything + 12


# Multiple variables can be defined in the same cell:

# In[3]:


a = 1
b = 2
c = 3


# And multiple variables can be used in the same expression:

# In[4]:


a + b + c


# Notice that a cell containing only an assignment has no output:

# In[5]:


seconds_in_a_year = 60 * 60 * 24 * 365


# This might seem strange: in the previous section, the result of our expressions was displayed as the cell's output. What gives?
# 
# The reason we see no output is because the code `seconds_in_a_year = 60 * 60 * 24 * 365` is not an **expression**, it is a **statement**. While expressions have values, statements do not. When a notebook cell is run, the value of the last line in the cell is used as the output. But since an assignment statement has no value, there is no value to print.
# 
# However, the line of code consisting only of a variable's name *is* an expression -- its value is the value of the variable. For instance:

# In[6]:


seconds_in_a_year


# This suggests the following workaround to the fact that assignments result in no output:

# ````{jupytertip}
# 
# To have Jupyter display the value of a variable that has just been assigned, write the variable's name as the last line of the cell. For example:
# 
#     number_of_seconds_in_a_year = 60 * 60 * 24 * 365
#     number_of_seconds_in_a_year
# 
# 
# ````

# Testing it out:

# In[7]:


seconds_in_a_year = 60 * 60 * 24 * 365
seconds_in_a_year


# Valid names may include letters, underscores, and numbers -- but they must start with a letter or underscore. Names are **case-sensitive**, meaning that `My_variable` and `my_variable` are two different, distinct names.

# You can experiment with variable assignments in order to get a better feeling for how Python works. For instance, suppose we define two variables, `a` and `b`, and a third variable `c` to be their sum:

# In[8]:


a = 5
b = 3
c = a + b
c


# We see that, as expected, the value of `c` is 8. Now suppose we create and run a new code cell containing:

# In[9]:


a = 42


# If we were to print the value of `c`, what would we see? Would it still be 8? Or now it "update" to become 45 now that `a` has changed? Try it by creating a new cell and writing the necessary code. The answer is below:

# ```{hiddenanswer}
# ---
# question: Suppose we were to print the variable `c`. What would we observe its value to be?
# answer: 8. 
# ```

# ## The Kernel: The "Brains" of a Notebook
# 
# When we define a new variable, we expect the notebook to remember its value. But where is this value kept, precisely?
# 
# It might help to understand a little more about how notebooks work. When you launch a Jupyter notebook, an instance of Python called a **kernel** is started on a remote server. When you run a cell, the code is sent over the internet to the kernel, which then evaluates the code and sends back the result for display in our browser. In this way, the kernel is the "brain" of the notebook, since it not only does the calculations, but also remembers the values of the variables we have defined.
# 
# Just knowing that the kernel exists can help us better understand how notebooks work, and therefore avoid some common mistakes. Consider the following problematic situation. You need to calculate the area of a triangle, so your first define variables `base` and `height` as such:

# In[10]:


base = 3
height = 4


# You then use the formula for the area of a triangle, but make a mistake: you forget to multiple by 1/2:

# In[11]:


area = base * height


# Unfortunately, you don't recognize your mistake immediately. You continue on, creating new code cells and executing them. At some point, you write a piece of code that converts a person's height to feet from inches:

# In[12]:


height = 72 / 12


# Now suppose that something makes you realize that you got the formula for the area of a triangle wrong. You go back and fix the cell and re-run it. The question is: which value of `height` is used? The value 4, from above the cell? Or the value 6 from below (calculated from 72 / 12)? Try it and see!' You'll find that the new value of `height` is what is used when re-computing the area. This is obviously not what we wanted.
# 
# It turns out that it isn't the order of the cells within the notebook that matters, it is the order in which they are executed. Typically, cells are executed in the order in which they appear in the notebook, but there are many instances where the cells are executed out-of-order. In such instances, weird "bugs" can occur, such as the one described above.
# 
# Luckily there is a simple fix to this problem. Select "Kernel -> Restart and Run All" from the menu. This will restart the kernel, causing it to forget the value of all variables it currently knows. All of the cells will also be re-run, from top to bottom. Restarting a kernel like this is like pushing "reset".
# 
# ```{jupytertip}
# 
# If you notice strange behavior while working with a Jupyter notebook, remember the number one rule of debugging: try turning it off and then back on. The equivalent of this with a Jupyter notebook is selecting "Kernel -> Restart and Run All" from the top menu.
# ```

# ## Example
# 
# A lightyear is a unit of measurement equal to the distance that light travels in one Earth year. Because light is very fast, a lightyear is quite a large distance.
# 
# Suppose we want to calculate the number of lightyears between the Earth and the Sun. Let's start by assuming that we know two things:
# 
# 1. The speed of light is 186,000 miles per second
# 2. The Earth is 93 million miles away from the sun
# 
# Here's our strategy: we'll first calculate how long a lightyear is in miles, then we'll divide 93 million miles by this number to find how many lightyears are between the Sun and the Earth.
# 
# So how long is a lightyear, in miles? That is, how far does light travel in one year. Well, it travels 186,000 miles per second. We have already calculated the number of seconds in a year above, and stored the result in a variable called `seconds_in_a_year`. Therefore, light travels:

# ```{margin}
# 
# The underscore in `186_000` does nothing -- Python ignores it. But it makes it easier for us humans to see how large the number is. If you'd like, you can omit it entirely.
# ```

# hours in one day. And since there are 365 days in a (normal) year, light travels

# In[13]:


186_000 * seconds_in_a_year


# miles in one year. Now we can get what we came for. Dividing 93 million by this number will give us the distance to the Sun in lightyears:

# In[14]:


93_000_000 / 5865696000000


# The result is a relatively small number expressed in scientific notation. Remember that `1.585e-5` is shorthand for $1.585 \times 10^{-5}$.
# 
# ```{tip}
# 
# Giving names to variables makes your code easier to understand. It's often a good idea to break a long calculation up into intermediate steps and give names to the result of each part.
# ```
