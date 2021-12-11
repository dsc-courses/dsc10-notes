#!/usr/bin/env python
# coding: utf-8

# # Strings

# Think about the type of data that you're likely to see as a data scientist. Does it only contain numbers? Of course not! Much of the data you'll see comes in the form of *text*. Most programming languages have a special data type for storing text, called {dterm}`strings`. In this section, we'll move beyond using Python as a simple calculator and use it to do some simple text analysis.

# ## Creating Strings
# 
# To create a string in Python, write some text surrounded by quotation marks: `"`:

# In[1]:


"Word"


# In[2]:


"More than one word, and punc-tu-a-tion!"


# In[3]:


# not a number, since we're using quotes!
"3"


# Notice that Python displays our string with single quotes around it -- this is its way of letting us know that it is indeed a string.
# As before, we can use the `type` function to check what type Python believes these pieces of data to be:

# In[4]:


type("Word")


# In[5]:


type("3")


# Of course, `str` is short for "string".

# As with numbers, we can use variables to store strings:

# In[6]:


s = "Hello world!"
s


# If you don't like double-quotes, you're in luck: you can write strings using single quote marks just the same:

# In[7]:


'Word'


# In[8]:


'More than one word, and punc-tu-a-tion!'


# Unlike in other languages, there is no difference between using single quotes and double quotes in Python.

# What happens if you don't put anything inside of the quotes?

# In[9]:


''


# This is fine! We call it an *empty string*.

# ## More on single vs. double quotes

# We said above that there is no real difference between using single quotes and double quotes to create strings, but there are instances where one is preferable over the other.

# For instance, what if we wanted to turn the following piece of text into a string?
# 
# > JavaScript is a "real" programming language.
# 
# Notice that the text itself includes quotation marks. If we try to wrap the whole piece of text with double-quotes, Python will get upset:

# In[10]:


"JavaScript is a "real" programming language.


# When Python sees the first `"`, it thinks to itself: OK, this is a string. It continues reading until it find the second `"`, right before `real`. It then thinks the string is over -- but it isn't.
# 
# To avoid confusing Python, we can instead use single-quotes to delineate the string:

# In[11]:


'JavaScript is a "real" programming language'


# In this case, single-quotes were preferable, but that's not always the case. For instance, suppose we want to represent the string:
# 
# > Python: a data scientist's best friend.
# 
# We can't use single quotes here because of the apostrophe in "scientist's". So we surround the string with double quotes:

# In[12]:


"Python: a data scientist's best friend"


# There is another way we can handle strings containing single- and double-quotes: We can "escape" the character by prefixing it with a backslash `\`.  This will tell Python to treat the character differently than it normally would -- in this case, it tells Python not to end the string.
# This is very helpful when both single quotes *and* double quotes appear in the string!

# In[13]:


'They said, "escaping isn\'t so bad," and I believe them!'


# ## String Methods

# What are some things you might want to do with strings? For one, you might want to combine two strings into one longer string. Doing so in Python is easy: we can simply use `+`.

# In[14]:


s1 = 'Data'
s2 = 'Science'
s1 + s2


# Combining two strings in this way is called *concatenation*.

# ````{hiddenanswer}
# ---
# question: |
#     Given the following variables, write an expression that concatenates the two strings and adds a space in between. The output should be `'red fish blue fish'`
# 
#     ```
#     string1 = "red fish"
#     string2 = "blue fish"
#     ```
# answer: |
#     ```
#     string1 + ' ' + string2
#     ```
# ````

# What else might you want to do with a string? Capitilizing a string seems like a common task. Luckily, Python provides a function to do just this. However, unlike the functions we have seen so far (like `abs()` and `round()`), the `capitalize()` function is *attached to the string itself*. We call it in a slightly different way:

# In[15]:


'data science is awesome'.capitalize()


# Functions that are attached to the things they operate on are called *methods* -- but don't worry too much about the difference in name. Just remember that methods are by placing a dot after the string, and then writing the function name.

# Methods can be called directly on a string, or the variable name of a string. 

# In[16]:


s = 'data science is awesome'
s.capitalize()


# Note that the string method does not *change* the string itself, but rather creates a new string. We can see this by printing out `s`:

# In[17]:


s


# We observe that this is the original value of `s` as it was before we called the method. If we wanted instead to save the result, we would need to give it a name:

# In[18]:


t = s.capitalize()
t


# We could also *overwrite* `s` with the new value:

# In[19]:


s = s.capitalize()
s


# Strings have plenty of methods -- you can see them by typing "'some string'." and hitting tab. Here are a few examples:

# In[20]:


"why am i yelling?".upper()


# In[21]:


"THIS IS A LIBRARY PLEASE BE QUIET".lower()


# In[22]:


"dive into data science".title()


# ```{jupytertip}
# You can see all of Python's string methods by typing `"some string".` then hitting {kbd}`Tab`.
# ```

# In particular, the `replace` method is extremely powerful, since it allows us to find and replace sections of a string. The previous string methods we looked at took no arguments, but the `replace` methods takes two arguments: *the text to find*, and *the text to replace it with* (in that order).

# In[23]:


'found you'.replace('you', 'Waldo')


# Remember the empty string `''`? It's used a lot with `replace` in order to get rid of parts of text entirely! Notice that the text must match *exactly*, and is case sensitive.

# In[24]:


'Hello, my name is **SNEEZE** Justin'.replace('**SNEEZE** ', '')


# In[25]:


'where\'s Waldo'.replace('w', '')


# Since the string methods we've looked at return more strings, we can even call more string methods on the result!

# In[26]:


s = 'started with words'
t = s.replace('started', 'ended')
u = t.replace('words', 'a sentence')
v = u.capitalize()
v


# But here's a shortcut: we don't need to assign each result to intermediate variables. We can do it "all at once" with *method chaining*:

# In[27]:


s = 'started with words'
s.replace('started', 'ended').replace('words', 'a sentence').capitalize()


# ## Conversion

# Data scientists sometimes get their data by {dterm}`scraping <web scraping>` a webpage. For instance, suppose we want to know the water temperature in La Jolla (either to study the effects of climate change, or to know whether the water is nice for surfing). We can find the information we want on [the NOAA's website](https://www.ndbc.noaa.gov/station_page.php?station=ljac1). We can write some code to download this webpage and extract the data we need.
# There's just one problem: webpages are just globs of text (that is, they are strings), but we want the temperature as a *number* (preferably a float). Luckily, converting back and forth between these types is easy.
# 
# Suppose we have a isolated the current ocean temperature as a string:

# In[28]:


ocean_temp = '72.8'
ocean_temp


# While this might look like a number, notice the quotation marks: this means that Python thinks of it as a piece of text.

# In[29]:


type(ocean_temp)


# As a result, we can't do math with the ocean temperature:

# In[30]:


ocean_temp + 2


# Here, Python has complained with a `TypeError`. Python is saying that it doesn't know how to combine objects of these types: `str` and `int`. To do the arithmetic, we need to convert the string to a float. We can do so with the `float` function:

# In[31]:


float(ocean_temp)


# In[32]:


float(ocean_temp) + 2


# We can also convert a string to an integer using `int`:

# In[33]:


days_since_last_beach_visit = '4'
days_since_last_beach_visit


# In[34]:


int(days_since_last_beach_visit)


# Be careful, though -- if you try to convert a string that doesn't look like an integer using `int`, Python will yell at you:

# In[35]:


int('3.14')


# If we *really* wanted to convert `'3.14'` to an integer, we would need to convert it to a float first:

# In[36]:


int(float('3.14'))


# ## Summary
# 
# - Multiple strings can be glued together using `+`.
# - Strings own a handful of **methods** -- functions that belong solely to the data type of strings.
# - String methods are called using {dterm}`dot notation`, by placing a dot after a string or variable name of a string, then calling the function: `my_string.function_name(arguments, ...)`
# - Some string methods allow you to create new strings that change capitalization or find and replace snippets of text.
