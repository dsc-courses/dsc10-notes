#!/usr/bin/env python
# coding: utf-8

# # Parameters and statistics

# In the last section we learned about populations, samples, and their respective distributions. But there's really a *lot* happening in a histogram, and you can't really *tell* someone the exact distribution of a population or sample. In life, people like to summarize complicating things with simple numbers. In your career, you'll be asked to generate metrics -- single numbers which summarize important characteristics of a distribution.
# 
# The total size, average, minimum, maximum, spread, and so on are all important characteristics of distributions, and each can be expressed with a metric. There are many more metrics that exist, and we can even invent our own!

# ## Population parameter
# 
# The {dterm}`population parameter` refers to a desired metric of a population, and just like the population distribution a parameter this is usually considered *fixed*.
# 
# Remember that the *p*opulation has a *p*arameter since they both start with *p*.
# 
# Using our population of fish weights, we could ask about parameters such as the mean or maximum weight, or about average variability of fish weights. For all of these potential parameters, the population produces a single value.

# In[1]:


import babypandas as bpd
import numpy as np

population = bpd.read_csv('../../data/fish_kg_cm.csv')
population.plot(kind='hist', y='WEIGHT')


# In[ ]:


print('Population Mean:    ', population.get('WEIGHT').mean())
print('Population Max:     ', population.get('WEIGHT').max())
print('Population Variance:', np.var(population.get('WEIGHT')))


# If we're feeling zany (or have a specific purpose in mind, like checking the well-being of our fish), we can even define our own metric of interest. Maybe we're interested in just the proportion of fish below a certain weight. That's certainly a metric, too!

# In[ ]:


print(
    'Population Proportion of small fry:', (population.get('WEIGHT') < 1).mean()
)


# But, we've already realized that we can't expect to measure entire populations in the real world, so we'll need work with samples instead.

# ## Sample statistic
# 
# When the metric used to calculate a population parameter is used on a sample, we call it the {dterm}`sample statistic`. Just like sample distributions, a sample statistic is subject to random chance depending on what group of individuals we sample!
# 
# Remember that the *s*ample produces a *s*tatistic since they both start with *s*.
# 
# Just like parameters, we could calculate statistics such as the mean, max, or variance, and we'll receive a single value. But, we should expect these values to differ each time we conduct a new sample -- even when the sample remains the same size.

# In[ ]:


sample = population.sample(100)

print('Sample Mean:    ', sample.get('WEIGHT').mean())
print('Sample Max:     ', sample.get('WEIGHT').max())
print('Sample Variance:', np.var(sample.get('WEIGHT')))
print('Sample Prop of small fry:', (sample.get('WEIGHT') < 1).mean())


# Ideally, we'd like to be able to use a sample statistic to provide us with an educated guess for the true population parameter. Unfortunately, it seems like the sample statistic doesn't seem to always match the parameter...

# In[ ]:


pop_mean = population.get('WEIGHT').mean().round(2)
pop_max  = population.get('WEIGHT').max().round(2)
pop_var  = np.var(population.get('WEIGHT')).round(2)
pop_prop_small = (population.get('WEIGHT') < 1).mean().round(2)

# Collect a handful of samples keep track of various sample statistics for each

sample_means = []
sample_maxes = []
sample_vars  = []
sample_prop_smalls = []

for i in range(5):
    
    sample = population.sample(100)
    sample_weights = sample.get('WEIGHT')
    
    sample_means.append(sample_weights.mean().round(2))
    sample_maxes.append(sample_weights.max().round(2))
    sample_vars.append(np.var(sample_weights).round(2))
    sample_prop_smalls.append((sample_weights < 1).mean().round(2))
    
print('Pop Mean:         ', pop_mean)
print('Sample Means:     ', sample_means)
print('Pop Max:          ', pop_max)
print('Sample Maxes:     ', sample_maxes)
print('Pop Variance:     ', pop_var)
print('Sample Variances :', sample_vars)
print('Pop Prop small   :', pop_prop_small)
print('Sample Prop small:', sample_prop_smalls)


# Based on what we've seen so far, it seems unlikely that a metric like the sample max will be the same as the population max, but something like the sample mean does appear consistently close to the population mean.
# 
# How close is our statistic to the parameter, really? How consistent is it? With what probability will the statistic equal the population parameter (within some margin-of-error, like +/- 1 gram)?
# 
# With an understanding of formal mathematics and probability theory we can answer these questions! In the mean time, we can use the some approach from our introduction to probabilities: just run a simulation!

# ## Sampling distribution
# 
# Using the same general steps for simulation as we learned before, we can run an experiment to select a random sample of n=100 from the population and see what the resulting sample statistic is.

# In[ ]:


# Write the code for a single trial
def sample_mean(n):
    return population.sample(n).get('WEIGHT').mean()

sample_mean(100)


# In[ ]:


# Call the trial function a lot of times and keep track of the results
sample_means = []

for i in range(5000):
    sample_means.append(sample_mean(100))


# We can now calculate a specific experimental probability, like the probability that the sample mean is within ±0.01 of the population mean. Or, better yet, we can enable ourselves to answer lots of questions about the sample statistic by plotting the *sampling distribution*.
# 
# The {dterm}`sampling distribution` is the distribution of all possible sample statistics with a fixed population and metric, and given sample size. For example, as a result of the experiment above we can plot the sampling distribution of mean fish weights at the London Zoo when the sample size is 100.
# 
# Because we're running an experiment instead of calculating the theoretical probabilities, this distribution is considered *empirical*. On top of this histogram we can overlay a line at the true population parameter to see how close we got.

# In[ ]:


sample_means_series = bpd.Series(data=sample_means)
ax = sample_means_series.plot(kind='hist', density=True,
                         title="Empirical sampling distribution of mean fish weight, n=100")
# Add a vertical line at the population mean, with a red color
ax.axvline(x=population.get('WEIGHT').mean(), c='r')


# Based on this sampling distribution, we've empirically shown that the sample mean seems to be centered around the population mean. So, on average our sample mean should be pretty close to the true population mean.
# 
# We can find sampling distributions for any and every possible metric we want by using this simulation approach! Remember that the sampling distribution depends strongly on the sample size, however. For example, let's look at the sampling distribution in regards to maximum weight.

# In[ ]:


def sample_max(n):
    return population.sample(n).get('WEIGHT').max()

def sample_max_distribution(sample_size, ax=None):
    
    sample_maxes = []
    
    for i in range(1000):
        sample_maxes.append(sample_max(sample_size))
        
    sample_maxes_series = bpd.Series(data=sample_maxes)
    
    ax = sample_maxes_series.plot(kind='hist', density=True, ax=ax)
    ax.axvline(x=population.get('WEIGHT').max(), c='r')
    
    return ax


# ```{note}
# It's worth mentioning that the number of trials of our experiment (in this case 1000) won't affect the overall shape of the resulting sampling distribution -- only the granularity of it. Too small and we'll start losing detail, but any relatively large number of trials is okay.
# 
# Sample size, however, has a profound effect on the sampling distribution!
# ```

# In[ ]:


sample_max_distribution(500)


# ```{hiddenanswer}
# ---
# question: Want to convince yourself that the number of trials really doesn't change our sampling distribution? See if you can modify the function above to add a `number_of_trials` argument and check it over a handful of values!
# answer: (No answer, try it in a notebook!)
# ```

# It so happens that the sample size *does* have a pretty profound effect on most sampling distributions. Let's see what happens when we increase the sample size.

# In[ ]:


# You don't need to understand this plotting code, but congrats if you do :)
import matplotlib.pyplot as plt

def plot_three_sampling_distributions(sample_sizes):
    """
    Simulates the sampling distribution of sample max for three different sample
    sizes, then plots them side-by-side.
    """

    # Create a figure to hold three charts on the same row
    fig, axes = plt.subplots(1, 3, sharey=True,
                             constrained_layout=True, figsize=(10, 3))
    fig.suptitle('Sample Distributions of Max Weight')

    # Simulate the sampling distribution for each sample size
    for i in range(len(sample_sizes)):
        
        sample_max_distribution(sample_sizes[i], ax=axes[i])
        axes[i].set_title('n='+str(sample_sizes[i]))


# In[ ]:


plot_three_sampling_distributions([50, 150, 300])


# As sample size increases, the sampling distribution changes significantly -- this is the case for practically any metric we choose to study. Once again, with a larger sample size, our result is better (in this case, more consistent).
