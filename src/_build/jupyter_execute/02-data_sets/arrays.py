#!/usr/bin/env python
# coding: utf-8

# # Lists and Arrays
# 
# Before we do can do any data analysis, we must first collect a *data set*. For instance, if we want to get a good idea of the typical temperature in San Diego in December, we might collect a large number of recorded temperatures from the past several years. Naturally, we need some way of storing this collection of numbers. Of course, we could store each recorded temperature in its own variable:

# In[1]:


temp_dec_01_2005 = 65
temp_dec_02_2005 = 68
temp_dec_03_2005 = 63
...
temp_dec_31_2020 = 71


# This gets tedious quickly -- can you imagine trying to compute the average temperature this way? Your code would look something like `(temp_dec_01_2005 + temp_dec_02_2005 + ...) / n_days`, where `n_days` is the number of days in the data set. Instead, we'll use *container* data types -- lists and arrays -- that make it much easier to work with sequential data.

# ## Lists

# Python comes with a data type that is purpose-built for storing sequential data: the *list*. Creating a list in Python is done by surrounding a group of items with square brackets, `[ ]`, and separating each item with a comma `,`, like so:

# In[2]:


temperatures = [65, 68, 63, 71]
temperatures


# Any type of data is allowed inside a list (including other lists), and you can include variables:

# In[3]:


x = 42
random_stuff = ['oranges', x, True, [1, 2, 3]]
random_stuff


# Lists are their own data type:

# In[4]:


type(salaries)


# Python's lists are versatile and easy to use, but code that uses lists can be *slow*. As data scientists, we will be working with sequences of millions, if not billions, of entries -- so speed is of the essence. Therefore, will use another type of collection to store our sequential data: the *array*.

# ## Arrays
# 
# Arrays are like lists in that they store sequential data, but they optimized for the types of heavy calculations done in data science. They are blazing fast, and memory-efficient.

# Arrays aren't included with Python, however.
# Remember that Python wasn't originally designed specifically for data scientists. Instead, it is a *general purpose* language, used by web developers, software engineers, artists, etc. So in order to give Python what it needs -- a way of efficiently working with large sequences of numbers -- a group of scientists independently developed an extension to Python called [NumPy](https://numpy.org/) (short for "numeric python").

# ```{figure} ../images/numpy-logo.svg
# ---
# height: 150px
# name: my-figure
# ---
# The *NumPy* logo.
# ```

# ```{tip}
# In case you're curious, it's pronounced "num-pie".
# ```

# Among other thing, NumPy provides a fast array data type. To use NumPy arrays, we'll need to import NumPy, just as we did with the `math` module in the previous chapter:

# ```{margin}
# 
# Note that while the `math` module is included with Python, *NumPy* is not (it has to be installed separately). But we import them the same way.
# ```

# In[ ]:


import numpy as np


# The notation `as np` means that we are giving `numpy` a new, shorter name that will be faster to type. Whenever we want to use a function from the `numpy` package, such as the `sqrt` function, we'll write `np.sqrt` instead of `numpy.sqrt`.

# ```{margin}
# 
# You could change `numpy`'s name to whatever you want, for instance: `import numpy as my_favorite_library`. However importing it as `np` is a *de facto* standard in data science. Don't import it as anything else unless you have a good reason, or else you'll confuse other people who read your code.
# ```

# Let's create an array. We do so by calling the `np.array()` function with a list of data:

# In[ ]:


temperatures = np.array([65, 68, 63, 71])
temperatures


# Note the square brackets! The brackets appear because we are first creating a standard Python *list*. We then pass the list into the `np.array` function as its only argument. In fact, we could create the same array in two steps:

# In[ ]:


# this is a list
temperatures_list = [65, 68, 63, 71]

# and this is an array
temperatures_array = np.array(temperatures_list)
temperatures_array


# ```{warning}
# 
# A common mistake is to write `np.array([temperatures_list])` when attempting to create an array from a list. Do you see what is wrong with this? The square brackets are unnecessary! `temperatures_list` is already a list, so by writing `[temperatures_list]`, we are in fact creating a *list of lists*. The overall result is a two-dimensional array, which is probably not what you wanted. The right way to create an array from a list is to write `np.array(temperatures_list)`.
# ```

# Arrays are their own data type:

# In[ ]:


type(temperatures)


# The array we've created contains numbers, but arrays can also contain other types of data, like strings or bools. For example, we can make an array of strings:

# In[ ]:


np.array(['this', 'is', 'also', 'fine'])


# *But* in order to maximize their efficiency, a single array should contain only a single data type. That is, we shouldn't mix ints with strings, for example. In fact, numpy will sometimes do surprising things to make sure that all of an array's elements have the same data type. 
# Remember what happened when we evaluated expressions that contained both ints and float? The result was always a float. The same thing will happen if we try to make an array containing both ints and floats:

# In[ ]:


np.array([1, 2, 3.0])


# If you look carefully, you'll see that there is a decimal after each number. Numpy has helpfully converted each of the numbers to floats -- even the ones that were provided as ints.
# 
# The following example may be even more surprising:

# In[ ]:


np.array([1, 2, 3, 'banana'])


# Numpy has "helpfully" converted the ints into strings so that all of the items in the list have the same type: string. Why did it convert the ints to strings instead of the string to an integer? There's no natural way to convert "banana" into an integer, but 2 naturally becomes the string `"2"`.

# 
# ```{margin}
# No need to be worried about the weird looking "dtype" -- that just tells us that the data type it contains are stored as [unicode](https://en.wikipedia.org/wiki/Unicode) strings (`U`) with a maximum possible length of 21 characters (`21`).
# ```

# Sometimes it is useful to know how many elements are in an array. We can determine this with the `len` function:

# In[ ]:


arr = np.array([1, 2, 3])
len(arr)


# ## Array Functions and Methods

# Numpy arrays are not only useful because of their speed and memory efficiency -- they also come with plenty of helpful functions and methods for performing the most common data analysis operations, such as summing all of the entries of an array or computing their mean.

# The NumPy functions can be called just like we called the math functions. Once we've imported the `numpy` library (abbreviated as `np`) we can just type `np.` followed by a function name to access the function. For instance, you can use the `np.mean` function to calculate the mean value of a sequence:

# In[ ]:


example_array = np.array([1, 1, 2, 3, 3])
np.mean(example_array)


# There are many functions, such as the `np.diff` function which calculates the difference between each consecutive pair of elements:

# In[ ]:


np.diff(example_array)


# Just like strings, arrays also have special *methods* that can perform calculations. A few useful ones are shown below:

# In[ ]:


example_array.min()


# In[ ]:


example_array.max()


# In[ ]:


example_array.sum()


# In[ ]:


example_array.mean()


# Don't worry, you don't need to memorize all of the different functions/methods (there are a lot!) -- we'll include references when necessary.

# What is the difference between a *function* and a *method*? In short, a method is a function that is "attached" to a particular instance of a type, such as a particular array. An example of a function call is `np.diff(example_array)`; an example of a method call is `example_array.min()`. Notice that in the method call, the variable name comes first.
# 
# Numpy organizes its operations into function and methods. It isn't always clear why something is a method and not a function, or *vice versa*. In fact, some operations are available *both* as functions and methods. For instance, numpy provides both a function and a method for computing the mean:

# In[ ]:


# mean, as a function
np.mean(example_array)


# In[ ]:


# mean, as a method
example_array.mean()


# Methods are useful for a variety of reasons, one being that they enable a coding practice called {dterm}`method chaining`. For example, suppose we wish to round each number in an array of floats and then compute their mean. We can use the `.round` method to round each number in the array. Called with the argument of `0`, it will round each number to zero decimal places (that is, to the nearest whole number):

# In[ ]:


arr = np.array([3.14, 2.71, 99.99])
rounded = np.round(arr, 0)
rounded


# Then we can compute the mean with the `.mean()` method:

# In[ ]:


rounded.mean()


# We could have done this all in one line as follows:

# In[ ]:


arr.round(0).mean()


# This works because the result of each method is returned and used for the next method. That is, `arr.round(0)` returns an array of rounded numbers. This array is never given a name, but it is used for the next method call to `.mean()`.
# 
# Method chaining is sometimes desirable because it concisely captures the "flow" of the calculation. We'll see a lot of method chaining in the coming chapters.

# ### Example
# 
# Every year, the programming community forum [StackOverflow](http://stackoverflow.com) [surveys](https://insights.stackoverflow.com/survey/2019#overview) its users, asking them such important questions as: what is your salary? and, how many computer monitors are on your desk at home? The results are publicly available. Since many of those who respond are data scientists, we can use the data to get an idea of a typical data scientist's salary.

# In[ ]:


salaries = np.loadtxt('../../data/salaries.csv')


# The variable `salaries` is a NumPy array containing the salaries of every US-based data scientist in the survey. How many were there? We can answer that with `len`:

# In[ ]:


len(salaries)


# What was the mean salary?

# In[ ]:


salaries.mean()


# Nice. What about the *median* salary?

# In[ ]:


salaries.median()


# Oops. It turns out that there is no method called "median" in numpy. There is, however, a `median` function:

# In[ ]:


np.median(salaries)


# Notice that the median is about \$10,000 less than the mean. As a data scientist would point out, the mean is more "sensitive to outliers", meaning that a few people who make a very large amount of money can skew the mean. Let's see what the largest salary is:

# In[ ]:


salaries.max()


# 2 million dollars! Remember, though: these salaries are *self-reported*. Presumably no one checked to make sure that they were *accurate*.

# ## Accessing array items

# An array is an *ordered sequence* of items. This means that there is a "first" element, a "second" element, and so on. Therefore, we can retrieve a particular element by providing its place in the order as a number known as the element's {dterm}`index` in the array. To do so, we write the array's name followed by square brackets. Inside the square brackets, we place the index of the element we wish to retrieve. There's one small catch: Python, like many programming languages but unlike most humans, starts counting from zero.
# 
# For example, let's make a list of three names:

# In[ ]:


names = np.array(['Xanthippe', 'Yvonne', 'Zelda'])
names


# To get the first element out of the array, we use the following syntax:

# In[ ]:


names[0]


# To get the second, we write:

# In[ ]:


names[1]


# And to get the third, we write:

# In[ ]:


names[2]


# ```{margin}
# This business of starting at zero instead of one may seem strange, but it has its advantages. For a defense of this approach, see the famous essay *Why numbering should start at zero* by the renowned computer science Edsger Dijkstra.
# ```

# How do we retrieve the last element of the list? We could use the list's length, subtracted by one:

# In[ ]:


names[len(names) - 1]


# But this is a lot of typing! Instead, here's a useful trick: if you use a negative number to retrieve an element, Python starts counting from the *back* of the array. So, for instance, to retrieve the last element we can also write:

# In[ ]:


names[-1]


# The array above has only three things in it, and their indices are 0, 1, and 2. What happens if we try to access the list at an index that doesn't exist, such as 99?

# In[ ]:


names[99]


# It should also be noted that the same syntax works for retrieving elements from Python lists:

# In[ ]:


lst = ['hi', 'i', 'am', 'a', 'list']
lst[2]


# ## Element-wise operations

# When working with a data set we often want to perform the same operation on all of the data set's elements at once. For example, given an array of temperatures in Fahrenheit, we might want to convert all of them to Celsius. Because of this, Numpy makes writing code that works with 

# In[ ]:


array1 = np.array([1, 2, 3])


# To subtract 3 from all of these numbers, we can simply write:

# In[ ]:


array1 - 3


# To multiply each of the numbers by 2, we would write:

# In[ ]:


array1 * 2


# And so on. In practice this means we could do something like convert an entire array of temperatures measured in Fahrenheit to Celsius by writing a single expression:

# In[ ]:


temperatures_f = np.array([0.5, 32.0, 71.6, 212.0])


# Remember that the formula for converting a measurement in Fahrenheit to Celsius is $C = (F - 32) * (5/9)$. Therefore:

# In[ ]:


temperatures_c = (temperatures_f - 32) * (5 / 9)
temperatures_c


# In the above example, first `(temperatures_f - 32)` is evaluated and produces an array with 32 subtracted from every temperature. Then `(5 / 9)` is evaluated. Then then every element in the new array is multiplied by 5/9, producing the final output array.

# We can also do element-wise operations between pairs of data from two arrays.
# 
# For this to work, both arrays must have the same size. The arrays are then lined up next to eachother, and the operation is performed between every corresponding pair of elements. This is best demonstrated with some examples:

# In[ ]:


array1 = np.array([1, 2, 3])
array2 = np.array([2, 4, 6])


# In[ ]:


array1 * array2


# In[ ]:


array1 - array2


# In[ ]:


array1**array2


# Both paired element-wise operations and standalone element-wise operations can be used in the same expression, since we're always producing another array as a result of each expression.

# In[ ]:


(array1 * 2) - array2


# Watch out for the new errors you might encounter! Let's see what happens if our other array isn't the same size.

# In[ ]:


array_short = np.array([2,4])
array1 * array_short


# The error message is a little cryptic -- what is this about "broadcasting"? Nevertheless, we can kind of understand that there is some issue with the "shape" of the two arrays not being compatible.
# In fact, this error is telling us that the first array has three elements but the other only has two, so the two arrays couldn't be pushed into the same shape.

# ## Ranges

# Often times it's useful to create an array of consecutive numbers, such as:

# In[ ]:


np.array([0, 1, 2, 3, 4, 5, 6, 7])


# Rather than write this array by hand, we can use the `np.arange` function to do it for us:

# In[ ]:


np.arange(8)


# Notice that just like indices, ranges will start at zero by default and exclude the last number. So calling `np.arange(12)`, for instance, will create an array with eleven elements whose first entry is 0 and whose last element is 11.

# While we saw an example of the range function being called with one argument, it can be called with one, two, or three arguments:
# 
# - `np.arange(endpoint)` Consecutive integers from 1 to endpoint (exclusive)
# - `np.arange(start, endpoint)` Consecutive numbers from start to endpoint (exclusive), increasing by 1 each step.
# - `np.arange(start, endpoint, stepsize)` Consecutive numbers from start to endpoint (exclusive), changing by stepsize each step.
# 
# Some example might make this clearer:

# In[ ]:


np.arange(10)


# In[ ]:


np.arange(5.5, 10)


# In[ ]:


np.arange(0, 1, 0.2)


# In[ ]:


np.arange(-1, -4)


# In[ ]:


np.arange(-1, -4, -1)


# The result of `np.arange` is an array like any other, so we can write things like:

# In[ ]:


np.arange(5) + 3


# ```{hiddenanswer}
# ---
# question: |
#     How would you use `np.arange` to create the array containing the first 6 powers of 2: 1, 2, 4, 8, 16, and 32?
# answer: |
#     `2**np.arange(6)`
# ```

# ---
# ## Summary
# 
# - To get multiple pieces of data in one place, we create a **collection**. If the collection is ordered then it is a **sequence**.
# - Each item in a sequence has an **index** -- its position, starting at zero.
# - **Lists** are the most basic sequence, and are created by surrounding a group of items with square brackets and separating each item by commas: `[item, item, ...]`
# - **Arrays** are a sequence type from the NumPy library, and are created by passing a list into the `np.array` function: `np.array([item, item, ...])` `np.array(my_list)`
# - NumPy offers lots of additional functions that can be called on sequences. These can be accessed using `np.function_name(arguments, ...)`.
# - An item can be selected from an array by using brackets with the index of the item: `my_array[index]`
# - Arrays support **element-wise operations**, such as adding or multiplying all elements by a single number.
# - Arrays of the same length support paired element-wise operations between the two arrays, such as adding or multiplying each element in one array with each element in the same position of another array.
# - An array of numbers with constant spacing can be easily constructed using `np.arange`
# - A range will always *exclude* the endpoint -- so `np.arange(3)` will count `0 1 2`.
