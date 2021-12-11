#!/usr/bin/env python
# coding: utf-8

# # Parameter Estimation and Bootstrap

# In the past handful of pages, we've been doing a lot of work around testing if samples fit some existing assumptions we have about their populations. But what if we want to start *making new assumptions* about the population -- i.e. we want to estimate a population parameter using our sample.

# ## The issue with just guessing the statistic

# It seems very convenient to just guess a value for the parameter based on the statistic -- after all, representative samples should exhibit statistics similar to the parameter.
# 
# Alas, a cautionary tale awaits you.
# 
# You, a famed data magician, are tasked with demonstrating your powers by predicting the proportion of students at your school who prefer apples over oranges. You survey a bunch of students and proclaim that the proportion is $0.7$, because that's what you saw in your sample. Soon, the school performs its annual "Apples vs Oranges" census, and it turns out the true proportion is only $0.6$... you were wrong. Your powers have been denounced and now you sit in shambles wondering how you could have prevented this from happening.
# 
# Unfortunately, samples are affected by random chance. Our *best guess* for the population parameter *is* an equation involving the statistic, but each time we take a sample that statistic is going to look a bit different, so our best guess estimate is going to be different, too!
# 
# Data science is not data magic. Data science is all about recognizing and embracing uncertainty. So when we make predictions we don't just give one number, we give two:
# 1. What is our best guess for the parameter
# 2. How different could our guess have been

# ## Our best guess for the parameter

# In your statistics classes you'll learn about 'maximum likelihood estimates'. These are basically just estimates for the population parameter that result in the highest probability of observing your sample statistic. They're usually a pretty good way to come up with a best guess, or {dterm}`point estimate` for a parameter.
# 
# A couple common point estimates are:
# - Mean: We estimate that the population mean $\mu$ is equal to the sample mean $\bar x$
# - Variance: We estimate that the population variance is equal to $\frac{1}{n}\sum(x_i - \bar x)^2$
# 
# When guessing something like the population maximum, the sample maximum is probably *not* a good choice because if our sample doesn't contain the population max then we're going to be totally wrong! We might choose to come up our own formula for guessing the max, like two times the mean $2\bar x$, or something else.
# 
# In all of these cases, our point estimate is going to look different every time our sample statistic looks different, and our sample statistic will look different pretty much every time we take a new sample. If we want to measure how 'good' a point estimate is, we should think about the question "*how different could my estimate have been if I saw a different sample?*"

# ## How different could our statistic have been

# When we collect samples from a population distribution, each sample will resemble the population distribution in shape. Due to the randomness of sampling, though, there will be a bit of variability in the sample, and thus in the statistic as well.

# ### The empirical sampling distribution
# 
# We can see this directly by loading in a population distribution, then taking a bunch of samples and plotting the empirical {dterm}`sampling distribution` (distribution of sample statistics). Let's look at the salary dataset again. Because it's a very skewed population, we'll be computing the median salary and overlay this true population proportion on each of our plots. We'll use samples of size 100 for simplicity.

# In[1]:


import babypandas as bpd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


population = bpd.read_csv('../../data/salaries.csv', names=['Salary'])
pop_median = population.get('Salary').median()
print('Population median:', pop_median)
population.plot(kind='hist', density=True)
plt.title('Population distribution')
plt.xlabel('Salary')
plt.ylabel('Density')

plt.axvline(pop_median, c='k', linestyle='dashed', label='Population Median')
plt.legend();


# In[ ]:


trials = 10_000

sample_medians = []

for i in range(trials):
    sample = population.sample(100)
    median = sample.get('Salary').median()
    sample_medians.append(median)
    
plt.hist(sample_medians, density=True)
plt.title('Empirical distribution of sample medians, n=100')
plt.xlabel('Sample median')
plt.ylabel('Density')


# With this distribution of the sample statistic computed it's very easy to see how different any one observed statistic could have been. There are a whole range of values that we could have randomly seen. Relatively often we could randomly find a sample with a statistic in the middle -- pretty close to the true population median of $100,000$. But not all the time.
# 
# ### A range of likely estimates
# 
# If we were to take a random sample and make a point estimate for the population median, it seems like most of the time we might estimate anywhere between $90,000$ and $110,000$ -- a solid *ten thousand dollars* below or above the true median. Very rarely we would get super unlucky with our sample and estimate outside of that range.
# 
# We could feel a lot more confident about our estimate if we gave a range of values that might capture the population median, instead of just our point estimate. E.g. if we got a sample median of $95,000$ it might be nice to say:  
# "Based on the sampling distribution I know that I could have gotten values both above and below this, so I'll guess that the population median is *somewhere within* ten thousand dollars of $95,000$."

# ## The bootstrap

# So, when we set out to estimate a parameter, we'd like to use the distribution of our point estimate in order to come up with a *range* of estimates that probably capture the true population value.
# 
# Only issue: we can't go out get all of the brand new samples needed to make an empirical sampling distribution. In the real world we can't just take thousands of samples due to a lack of funding and patience. Instead, we'll usually need to make due with only one sample, and that's all.

# In[ ]:


sample = population.sample(100)
sample.plot(kind='hist', density=True)
plt.title('Sample, n=100')
plt.xlabel('Salary')
plt.ylabel('Density')


# So, we only have one sample; we don't have access to the population; we want to create a sampling distribution so we can be confident in a range of possible values to estimate. Our question becomes:  
# *How can we create a sampling distribution when we don't have a population to sample from?*
# 
# True, we don't have access to the population distribution to take new samples from. However, if we could get access to a distribution that looks *similar* to the population... well then maybe we can get away with taking new samples from that similar distribution instead.
# 
# As it turns out, we *do* have a distribution that looks similar to the population -- our sample itself!

# ### The bootstrapped sampling distribution
# 
# To generate a sampling distribution from our single sample, simply pretend that our sample *is* the population, and take {dterm}`resamples` from that 'population'.
# 
# This process is called {dterm}`bootstrapping`. The term originates from a 19th century saying of "to pull yourself up by your bootstraps" -- essentially performing an impossible feat with no external help (like if a single lone sample were able to produce an entire sampling distribution with no external samples).
# 
# Just like with our normal sampling distribution process, the sample size should be fixed to a value we're interested in -- in this case **the resample size should be the same size of our original sample**. And finally, it's worth noting that **we must take resamples with replacement** -- can you imagine what would happen if we didn't?
# 
# Let's try it out.

# In[ ]:


# This is our one and only sample
# s = np.random.randint(10000)
# print(s)
#714,7698,4582,3493,7318,759,683,8441
# np.random.seed(s)
np.random.seed(8441)
sample = population.sample(100)
sample_median = sample.get('Salary').median()
sample.plot(kind='hist', density=True)
plt.axvline(sample_median, c='lightblue', linestyle='dashed', label='Sample Median')
plt.legend()
print('Sample median:', sample_median)


# In[ ]:


# This time, all references to `population` have been replaced with `sample`,
# and all `sample` have been replaced with `resample`.
#
# Other than that, this code looks pretty similar to previous sampling distrs!

trials = 10_000

resample_medians = []

for i in range(trials):
    
    # Remember that we need to sample with replacement
    resample = sample.sample(100, replace=True)
    median = resample.get('Salary').median()
    resample_medians.append(median)
    
plt.hist(resample_medians, density=True)
plt.title('Distribution of resample medians, n=100')
plt.xlabel('Bootstrapped median')
plt.ylabel('Density')


# Somehow (through the powers of probabilities and statistics) we managed to squeeze an entire sampling distribution out of a single sample. This 'bootstrapped' sampling distribution or resample medians doesn't look exactly the same as our empirical sampling distribution of sample medians -- but let's look at the *range* that it produces.
# 
# Based on this one sample, we conducted bootstrapping and determined that most resample medians fall somewhere between about $98,000$ and $120,000$, and very rarely outside of this range. Knowing that our sample median might not be the exact right answer, we can use this range of possibilities to estimate with a good amount of confidence that the true population median is *captured somewhere within* the interval between $98,000$ and $120,000$.
# 
# That way, if it turns out that our point estimate isn't perfect (it usually won't be) we don't need to be ashamed and ridiculed -- we can *plan* on our single-sample estimate being approximate, and simply provide the interval that our estimate covers.
# 
# It so happens that our range estimates from this example does successfully capture the true population median of $100,000$, nice!

# In[ ]:


plt.hist(resample_medians, density=True)
plt.title('Distribution of resample medians, n=100')
plt.xlabel('Bootstrapped median')
plt.ylabel('Density')

# Let's overlay our point estimate and the true median
# plt.axvline(sample_median, c='lightblue', label='Sample Estimate')
plt.axvline(pop_median, c='k', linestyle='dashed', label='Population Median')

# Finally, overlay our eyeballed range of typical bootstrapped estimates
plt.plot([98_000, 120_000], [0, 0], c='gold', lw=8, label='Typical estimates')

plt.legend(loc='upper right');


# Using this general process, we can actually be pretty confident that *most* of times that we pull a random sample and generate a bootstrapped distribution of estimates the range *will* capture the true population parameter -- we'll find out more about this on the next page.

# ## The bootstrap isn't magical

# As a final point, it's worth noting that the bootstrap -- much like us -- does not work by magic.
# 
# Before using the bootstrap, it's worth understanding a few key limitations. First of which: the quality of a bootstrap is bounded by the quality of the original sample it comes from.
# 
# ```{margin}
# This is parallel to a very common saying in machine learning, regarding the quality of training data and the performance of a model: "garbage in, garbage out".
# ```
# 
# In order to produce a useful bootstrapped distribution, our original sample should employ proper sampling techniques and be large enough to resemble the population it comes from. Remember that the reason we allow ourselves to take resamples from the original sample is because we've convinced ourselves that the original sample resembles the population.

# ## FAQ: Bootstrapping versus Permuting
# 
# Every quarter, a common question that arises is: "when do we resample versus when do we shuffle?" Both are a way of squeezing information out of samples so this question is understandable. Ultimately, they have different setup and different goals.
# 
# - Bootstrapping involves taking **resamples** (sampling the entire size of your data *with* replacement). We do this when we have a **single sample** and want to use it to generate a **sampling distribution** for a statistic (and a confidence interval, as we'll soon see).
# 
# - Permuting involves **shuffling** (sampling the entire size of your data *without* replacement) the labels between two groups, so that a data point in one group may get randomly moved over to the other group and vice versa. We do this when we have **two samples** and want to conduct a **hypothesis test for a shared population**.
