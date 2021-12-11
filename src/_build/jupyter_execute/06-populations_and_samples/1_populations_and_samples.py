#!/usr/bin/env python
# coding: utf-8

# # Populations and Samples

# In the previous chapter we ended off by talking about the "birthday problem" and used simulation to stumble upon a surprising result. But when we solved the problem we relied on the assumption that *every single birthday is equally likely* in our population. As a data scientist, we might like to check if that assumption is actually valid!
# 
# What if in actuality less people are born over the summer, or perhaps more people are born nine months after Valentines day? In that case, certain birthdays would be more prevalent than others. But how can we actually find out whether or not this is true?
# 
# One way is to ask everyone in the world what their birthday is... good luck with that! As it turns out, it's not feasible to survey billions of people. Fortunately, we can get a pretty good idea of how birthdays are distributed by collecting a *sample* of the population.
# 
# This is precisely the concept we'll introduce in this chapter.
# 
# Many interesting data-driven questions revolve around understanding some aspect of a 'population'. In practice, we usually can't collect data on the entire population, so instead we rely on samples to give us a representative idea of what the population actually looks like, or how it actually behaves.

# ## Populations
# 
# A {dterm}`population` in data science and statistics is an entire group of people, objects, or events on which we're capable of collecting data, in order to answer a specific question. The answers to questions like "do people prefer to watch content A or content B" or "what is a typical price for a house" are dependent on what specific *population* of people or houses they're referring to -- perhaps the populations about could be "all Netflix users", or "all houses in the South of France". Interestingly, a population can also refer to a group of events, such as "all fair dice rolls".

# ### Specifying a population
# 
# When we pose a question, we must narrow in on a corresponding population. There are two steps we follow to do so.
# 1. What group is our question about?
# 
#     Maybe we're only interested in particular group -- like house prices specifically in the South of France. Therefore, our population would be narrowed down from all houses in the world to just houses in the South of France.
#     
# 2. What group can we collect data from?
# 
#     Our data collection is often a limiting factor -- for example, if we're running a survey hosted on our website then we can only collect data on the people who visit our site. Therefore, our population is narrowed down from all users of the internet to just users who visit our site. We must remember that our population during analysis is always limited by the data we collect.
# 
# In the birthday problem above, we're probably interested in the population being the entire world -- are *all* birthdays actually equally likely across the globe? However, we managed to collect [a sample](https://github.com/fivethirtyeight/data/tree/master/births) which only contains births in the United States. Therefore we must narrow our population to only birthdays in the U.S. since that's the population that our data is coming from.

# ### Population distributions
# 
# Recall that knowing the *distribution* of some data is imperative to understanding and gaining insight from the data. The distribution is referred to as the 'shape' of the data, or simply what the data *looks* like.
# 
# The {dterm}`population distribution` is the shape of a feature across the entire specified population. In most settings, it's considered -- unchanging -- for the duration of a study. Notice that even something like the distribution of birthdays in the U.S., which technically changes every time someone is born or dies, is unlikely to change by any substantial amount over the course of a study.

# ### Models
# 
# In reality, unless we fully measure an entire population, we'll never actually *know* what a true population distribution looks like.
# 
# However, in many scenarios we tend to operate under *assumptions* about what populations look like. Statisticians (and marketing folks) love to call a set of these assumptions about the population distribution a "{dterm}`model` for the population".
# 
# For example, we proposed a model for the population of U.S. birthdays, which assumes that every birthday is equally likely and thus the population distribution is *uniform*. (Remember that we're ignoring leap years for simplicity -- sorry!)
# 
# ![](uniform-birthdays.png)

# ```{hiddenanswer}
# ---
# question: |
#     At the time of this writing, the United States populace is approximately $330,221,340$ people. Let's call the population size $N$. Under the assumptions of our model, each of the 365 days in a year is assumed to be equally likely $P(\text{day})=\frac{1}{365}$. 
# 
#     By using a frequentist approach to probability, $P(\text{day})=\frac{\text{# people with this birthday}}{N}$, can you calculate the number of people in the U.S. with a birthday on any given day?
# 
# answer: |
#     $$
#     \begin{aligned}
#     N &= 320,221,340 \\
#     \\
#     P(\text{day}) &= \frac{1}{365} = \frac{\text{# people with this birthday}}{N} \\
#     \\
#     \text{# people with this birthday} &= \frac{365}{N} \\
#     &= 904,716 \\
#     \end{aligned}
#     $$
# ```

# This distribution is purely the result of assumptions from our model!
# 
# Perhaps the distribution of U.S. birthdays actually looks totally different, like a wave ![](wave-birthdays.png), or a U ![](u-birthdays.png), or it could possess gaps where mysteriously no one has a birthday ![](missing-birthdays.png). (Do you actually *know* anyone born on March 19th? Yeah, nor do I.)
# 
# The truth is: we don't know, and we'll never know what the *true* population distribution is for most measurements since it's infeasible to collect data on every individual in the population!

# ```{admonition} A look forward
# What we *can* find out is whether or not the data we eventually collect actually fits our model.
# 
# The samples we're about to learn about are imperative for allowing us to create "hypothesis tests" which can tell is if our model is believable or not!
# ```

# #### Probability distributions
# 
# In many *models*, we basically end up assuming that our distribution matches some known *probability distribution*. This is useful since we know the probability of every outcome in a probability distribution!
# 
# There are also some cases where we *do* know the true population distribution, because we know that the members of the population must follow some probabilistic process.
# 
# For example, when working with the population, "outcomes of all fair six-sided dice rolls", we know *by the nature of 'fair'* that the true population distribution is the uniform probability distribution.
# 
# ![](dice-distribution.png)
# 
# This uniform distribution arises as the true population distribution when all values in that population are equally likely. There are *loads* of other probability distributions that exist, many with their own natural-world counterparts such as the 'bell curve' shape of people's birth weight, or the 'Poisson' shape of the number of supernovae seen per year, or the 'Pareto' distribution of wealth allocation (commonly abbreviated to simply the 80-20 rule)
# 
# ![](probability-distributions.png)
# 
# If we can convince ourselves that measurements from a particular population is the result of a probabilistic process -- such as fair dice rolls, occurrences of cosmological events, mature heights of a specific natural organism, or even combinations of multiple random inputs -- then we know that the true population distribution will match a mathematically-calculatable probability distribution!
# 
# That being said, if we're not entirely sure whether or not a population truly arises from a probabilistic process, we can still *hypothesize* that the population distribution looks similar to a probability distribution -- this is the case when we're comparing the distribution of U.S. birthdays to the uniform distribution.

# ## Samples
# 
# No matter what our hypotheses may be, if we want to get our hands dirty and witness first-hand what our population looks like, we must turn to the power of sampling.
# 
# In contrast to a population, a {dterm}`sample` is a subset of individuals randomly taken from a population. While it's infeasible to collect data from every member of a population, we can easily collect data from *some* of them.
# 
# Here's that sample of U.S. birthdays we mentioned earlier. This subset of the population only includes total births each day between the years 2000 and 2014 (inclusive) and includes $45,538,958$ birthdays (out of the roughly $320,000,000$ birthdays that exist in the country.

# In[1]:


import babypandas as bpd
import matplotlib.pyplot as plt

birthdays = bpd.read_csv('../../data/us_total_births_2000-2014_no_leaps.csv')
birthdays.plot(kind='bar', x='day_of_year', y='births', width=1, legend=False)
plt.xlabel('Day of year')
plt.xticks(range(0, 366, 10), range(0, 366, 10))
plt.ylabel('Frequency')
plt.title('Sample of U.S. Total Births per Day, 2000-2014')


# Hmmm, our sample seems to have a few days where considerably fewer births occur. This maybe just happened by random chance that less people were born on certain days. Maybe not, though, and our sample is a good way to find out. Out of curiosity, let's check which days had the fewest births.

# In[ ]:


# Top 5 lowest number of births
birthdays.sort_values('births').iloc[:5]


# ```{admonition} A look forward
# Notice that our sample doesn't quite match the uniform model we proposed. Is this sample evidence that our uniform model is wrong? Certainly is seems very odd that a truly uniform distribution could produce a random sample with some days (like December 25, January 1, and July 4) with so few births...
# 
# These days don't seem so 'random' either. Chances are the true population of U.S. birthdays is *not* uniform. We'll learn how we can use our sample to make decisions about our model in the Hypothesis Testing chapter.
# ```

# ### Sampling schemes
# 
# The process of choosing individuals from a population is called *sampling*, and while there are many different ways you can sample from a population, some approaches are better than others!
# 
# For example, if we were tasked with collecting a sample of people in the U.S., in an attempt to answer the birthday assumption, we might be tempted to just ask the people around us -- you might choose to ask your classmates, or simply the first hundred people you encounter on campus. This is called a *convenience sample* because, well, it's convenient. Unfortunately it's a bad practice.
# 
# Poor sampling schemes, like convenience sampling, produce samples that don't accurately represent the population. Remember that our population is determined in part by the data we're able to collect -- so when conducting convenience sampling we're essentially limiting our population to individuals in our geographical area at best.

# ```{margin}
# Did you know that the birthdays on sports teams are usually more common earlier in the year than later? So, if you were about to only ask your teammates on the local hockey team -- well, don't, that would probably be a skewed sample!
# 
# https://en.wikipedia.org/wiki/Relative_age_effect
# 
# https://www.wired.com/2013/03/nhl-selection-bias/
# ```

# A much better sampling scheme should produce samples that are *representative* of the population -- therefore diverse and random in nature.
# 
# By far the most common, simple, and yet extremely powerful method of sampling is called the "*simple random sample*". NumPy has a name for it too: `np.random.choice`.
# 
# As you might already suspect, this representative sampling scheme boils down to one simple step: *pick individuals from the total population, completely at random*.

# ### Collecting a random sample
# 
# NumPy's `random.choice` function should at least sound familiar to us by now, since we used it to simulate coin flips. In general, the function works by randomly picking elements from a sequence, like a list or an array -- in this case, randomly picking elements from a population.
# 
# In the case of simulating probabilities, we're essentially sampling from a probability distribution. But, in order get some experimental data samples, we need some population data to sample from!
# 
# How about we look at some fish? Each year in August the London Zoo measures the weight of its nearly 20,000 animal inhabitants, 7072 of which were fish as of 2019. Weight is a very powerful indicator of general health, but measuring the entire population of fish at the London Zoo is, obviously, quite an arduous process.
# 
# At other points in the year we still want to track the population distribution of fish weights, but we don't want to measure all seven-thousand fish again -- nor do we need to! As long as we collect a representative sample we can avoid a lot of work and still understand roughly what distribution of weights looks like.

# In[ ]:


import numpy as np


# In[ ]:


# Load in an array of fish weights in kilograms
fish = np.loadtxt('../../data/fish_kg.csv')
fish


# Above, the 'true' population of fish weights in kilograms has been loaded into a table -- but we won't look at it just yet. Let's work on sampling first.
# 
# By calling `np.random.choice` we can don our wetsuits, pull out a single random fish from anywhere in the entire zoo, measure it and then put the fish back in its tank.

# In[ ]:


np.random.choice(fish)


# #### Sample size and replacement
# 
# If you remember from the last chapter, `random.choice` also accepts a `size=` argument. The name of the argument, 'size', may have seemed strange in the context of simulating coin flips, but in the context of collecting a sample it fits right in. We can set the `size=` argument to our desired sampled size!
# 
# Careful though. By default, the `random.choice` function *puts the fish back* each time it samples an individual, which poses a problem if we try to sample multiple individuals. If we're unlucky, we might measure a fish, put it back, and then swim around and accidentally grab the same fish again! In a large population, this chance is really slim so it doesn't matter if we replace or don't replace the fish, but it's good to be cognizant of when dealing with smaller populations.
# 
# If we want to take our sample all at the same time, *without* replacing the individual after each pull. Therefore, we must remember to specify `replace=False`.
# 
# Let's try it now by filling up our scuba tank and randomly pulling aside fifty fish.

# In[ ]:


np.random.choice(fish, size=50, replace=False)


# We now have the power to sample representatively with whatever sample size we want. One fish, two fish, ~~red fish, blue fish~~, one-hundred, two-thousand...
# 
# You may have heard before that bigger sample sizes are better, so how about we go large and sample ten-thousand fish from our zoo?

# In[ ]:


np.random.choice(fish, size=10_000, replace=False)


# We can't.
# 
# The error message spells out the issue nicely -- we cannot take a sample that is larger than the population if we're sampling without replacement!
# 
# In most cases it is true that larger sample sizes are better -- we'll learn more about this in the next chapter -- but we have some notable limits. In real life, factors like cost or data availability might also limit our sample size.

# #### Sampling from tables
# 
# Sampling is the act of picking *individuals* from a population. Those individuals might possess multiple measurements, and it's important we keep those measurements together in case we want to compare those measurements in the future, like for measuring correlation.
# 
# When we're sampling individuals from a table, we need to create a sample of *rows*. For this, we use the DataFrame `.sample` method. It works exactly like the random choice function, but samples with `replace=False` as the default.

# In[ ]:


import babypandas as bpd


# In[ ]:


# Load a table of fish weights and fish lengths!
fish_frame = bpd.read_csv('../../data/fish_kg_cm.csv')


# To sample a single row of our table, the `.sample` method can be called with no arguments.

# In[ ]:


fish_frame.sample()


# And if we want to specify a sample size, we can just pass in the size as the first argument without needing any keywords. Remember that `replace=False` is the default behavior for sampling from tables.

# In[ ]:


# Randomly sample 50 rows without replacement
fish_frame.sample(50)


# ### Sample distributions
# 
# Just like populations, the distribution of a feature in our sample is called the {dterm}`sample distribution`. We can quickly use a visualization such as a bar chart or histogram to see what it looks like.

# In[ ]:


sample = fish_frame.sample(50)

sample.plot(kind='hist', y='WEIGHT', density=True)


# Each time we take a sample, we'll mostly end up collecting a different group of fish. As such, each time we collect an empirical sample distribution, it'll look a bit different.
# 
# Let's take a look at a handful of sample distributions -- all coming from the same population and the same sample size.

# In[ ]:


# You don't need to understand this plotting code, but congrats if you do :)
import matplotlib.pyplot as plt

def draw_five_samples(sample_size):
    """
    Collects five random samples with a specified sample size, then plots the
    corresponding sample distributions side-by-side.
    """

    # Create a figure to hold five charts on the same row
    fig, axes = plt.subplots(1, 5, sharey=True, figsize=(10, 2))
    fig.suptitle('Sample Distributions of Weight, n=' + str(sample_size))

    # Draw a sample and histogram for each chart position
    for ax in axes:
        fish_frame.sample(sample_size).plot(kind='hist', y='WEIGHT', density=True,
                                            ax=ax, legend=False)


# In[ ]:


draw_five_samples(50)


# #### Sample distributions converge to the population distribution
# 
# It's finally time to look at the true population distribution. This whole experiment was to find out if we truly can collect just a sample of fish weights and still determine what the population looks like. So how close did we get?

# In[ ]:


fish_frame.plot(kind='hist', y='WEIGHT', density=True)


# We may have gotten close, we may have been quite wrong, depending on *which sample we pulled*. Notice that there is a lot of disparity between each sample distribution, and a varying amount of disparity between the population distribution and each sample distribution.
# 
# Here's where sample size starts to matter. Let's increase the number of fish we measure from fifty to one-hundred.

# In[ ]:


draw_five_samples(100)


# Quite a bit better, right? And it's still tremendously less work than measuring the entire population of fish.
# 
# As we increase sample size, sample distributions will increasingly resemble the population distribution they come from.

# In[ ]:


draw_five_samples(500)


# #### Why do sample distributions resemble their population?
# 
# When we take a representative sample, we are picking individuals at random from the population. Recall that when more individuals share a similar value of a feature, the population distribution is considered 'denser' at that value.
# 
# ![](population-distribution.png)
# 
# When we randomly pick an individual, we're more likely to pick individuals from denser regions (higher bars) since there are physically more individuals in our population that exist in that range of values. The opposite can be said for regions of low density (lower bars) -- if there's a low density, we're less likely to pick an individual there.
# 
# ![](population-samples.png)
# 
# Therefore, once we've taken our full sample and plot out the sample distribution, we the sample will also exhibit more individuals from the same dense regions, and fewer individuals from the same low density regions.
# 
# ![](sample-distribution.png)
# 
# Invariably, there is random chance involved during sampling, so in most cases we won't produce a sample distribution that is exactly the same as the population. Each sample looks a bit different from the population and from each other, but greater disparities have rarer probabilities. It's downright statistically *unlikely* that we could produce a large sample distribution that looks super different from our population distribution.
