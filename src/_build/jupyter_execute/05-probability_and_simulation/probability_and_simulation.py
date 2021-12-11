#!/usr/bin/env python
# coding: utf-8

# # Probability and simulation

# Congrats, you've made it to the second half of this textbook. Here's a bold claim to start us off: *the study of probability is the key to tackling uncertainty*.
# 
# What exactly does the study of probability entail? And if it's so powerful, how can we use computers to leverage that power?
# 
# Let's dive in.

# ## Probabilities in our daily lives
# 
# Simply, a {dterm}`probability` is a measure of how likely something is to happen.
# 
# We rely on likelihood in our daily lives whenever we're faced with a question that doesn't have a definite answer. These often come in the categories of questions about the future, like "Will it rain today?", or questions that are subject to investigation or debate, like "Is this new medication actually effective?".
# 
# While all of the questions we could possibly ask have some fundamental, universal truth, much like quantum physics the true answer remains unknown until it's been observed! This means, in order to get a 100% certain answer, we need to wait for the future to arrive.
# 
# That's less than ideal. There must be a way to answer the question without waiting.
# 
# Enter: *probabilities*. In real life when we're faced with an uncertain question, we usually provide an uncertain answer. We say things like, "There's a 72% chance of rain -- you should bring an umbrella.", or "The medication was effective for 9 out of 10 tested patients -- there's a pretty good chance it'll work." How we arrive at that measure of '72%', or the reasoning behind 'pretty good chance' all boils down to calculating probabilities.

# ## A semi-formal introduction to probability
# 
# Formally, a probability of an event, written as $P(\text{event})$ is the likelihood that the event will occur expressed as a value between $0$ and $1$. A probability of $0$ means the event will theoretically never happen, $1$ means the event is theoretically certain to happen, and $0.5$ means the event is just as likely to happen or not happen.
# 
# $$
# 0 \leq P(\text{event}) \leq 1
# $$
# 
# For instance, when we flip a fair coin, the probability that it lands showing Heads is $P(\text{Heads}) = \frac{1}{2}$ (or $0.5$ or $50\%$). We know this intuitively, but let's formalize the math a little bit to figure out where that number comes from.

# ```{tip}
# You may notice that probabilities are defined as between 0 and 1, but sometimes we use a percentage. Mathematically they're the same, $100\% = 100 \textit{ per cent} = \frac{100}{100} = 1.$ But while percents can be nice in spoken language, you should stay consistent and always work with probabilities expressed as fractions or decimals between 0 and 1 when performing calculations. This will make your life much easier and prevent you from pulling out your hair due to decimal place errors!
# ```

# Since we're learning about data *science*, let's define the terminology of probability in a scientific manner. This terminology is consistent across most probability and statistics textbooks, too.
# 
# Each time we face an uncertain outcome -- like flipping a fair coin -- we're essentially conducting an *experiment*. An {dterm}`experiment` is a process with a set of distinct possible {dterm}`outcomes`, only one of which can be the true result of a single trial. We can conduct many trials of the experiment, but the each time we are uncertain which specific outcome will be the result. In this example, our experiment is a single coin flip and the possible outcomes are Heads and Tails, often written as a mathematical set, $\{\text{Heads}, \text{Tails}\}$.

# ### All things equal
# 
# In the case of flipping a coin, rolling a die, or any other experiment where all outcomes are equally likely, the probability of any given outcome is one divided by the total number of possible outcomes. So, for flipping a coin the probability of any outcome is $\frac{1}{2}$, for a six-sided die the probability of any outcome is $\frac{1}{6}$.
# 
# $$
# P(\text{equally-likely outcome}) = \frac{1}{\text{# of possible outcomes}}
# $$

# ```{margin}
# If all outcomes of a process are equally likely, we usually call that process 'random'
# ```

# In Python, we'll use NumPy's `random.choice` function to choose one outcome from a list of possible outcomes. The code below essentially conducts an experiment of a single coin flip, then checks whether or not it landed on 'Heads' by using a {dterm}`comparison operator`. If we run the cell a bunch of times, we should expect that it'll return True roughly half of the time.

# In[1]:


import numpy as np

outcome = np.random.choice(['Heads', 'Tails'])

outcome == 'Heads'


# You can also specify a `size=` argument to make multiple random choices, like flipping multiple coins. This time, we tell NumPy to choose randomly between Heads or Tails ten times, and the result is an array of the outcome of each trial.

# In[2]:


outcomes = np.random.choice(['Heads', 'Tails'], size=10)
outcomes


# ### Collections of outcomes
# 
# Let's move on to something more exiting than just two outcomes... how about we look at *six* different outcomes instead (oooh).
# 
# If you're playing a game that involves rolling a die, you might be able to win if you roll a one *or* if you roll a two. To calculate the chance that you will win, we find the sum of each individual probability that will lead to winning.
# 
# $$
# P(\mathrm{one}\textit{ or }\mathrm{ two}) = P(\mathrm{one}) + P(\mathrm{two}) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6}
# $$
# 
# What you've just stumbled upon is called an *event*. An {dterm}`event` is a collection of outcomes, and the probability of an event is just the probability of any of those outcomes occurring.
# 
# If we define the event $\text{win}$ as containing both the outcomes $\text{one}$ and $\text{two}$, then the probability of this event uses the exact same calculation as above.
# 
# $$
# P(\text{win}) = P(\mathrm{one}\textit{ or }\mathrm{two})
# $$
# 
# From these two facts, it follows that the probability of any event is always just the sum of the probabilities of each outcome that satisfies the event.
# 
# $$
# P(\text{event}) = \sum_{\text{all outcomes in event}} P(\text{outcome})
# $$
# 
# And yes, and event could contain more or less than two outcomes as well.

# ### Events with equally-likely outcomes
# 
# When we're in the scenario of equally-likely outcomes, it so happens that it doesn't matter *which* outcomes are in our event, merely *how many* outcomes are in our event.
# 
# Notice in our die example above that the numerator of every single outcome probability is $1$, and the denominator is always $6$. We can deduce a simpler way to calculate the probability of an event with these equally-likely outcomes.
# 
# $$
# P(\text{event with equally-likely outcomes}) = \frac{\text{# outcomes in event}}{\text{total # possible outcomes}}
# $$

# ```{margin}
# The realm of equally-likely outcomes is part of the study of 'Classical Probability'. Since the probabilities of outcomes and events are based on counting how many outcomes there are, and how many we're interested in, this study is tackled primarily using combinatorics -- you'll see more of those in DSC 40A and your statistics classes! 
# ```

# #### The `or` and `|` operators
# 
# Just like an event can be broken down into multiple $\text{or}$'s mathematically, we can do the exact same thing in our code by using the `or` operator to string together multiple equality checks. In the code below, we're running an experiment of a single die roll, and checking if the winning event is satisfied by the roll. Based on the math above, we should expect the following cell to return True roughly a third of the times we run it.

# In[3]:


outcome = np.random.choice([1, 2, 3, 4, 5, 6])
outcome


# In[4]:


(outcome == 1) or (outcome == 2)


# Again, NumPy makes it easy make multiple random dice rolls.

# In[5]:


outcomes = np.random.choice(range(1,7), 5)
outcomes


# In order to see which of these rolls satisfy our $\text{win}$ event, we want to use an element-wise version of the 'or' operator (since we're working with an array now). Element-wise 'or'-ing can be performed using the `|` operator.

# In[6]:


(outcomes == 1) | (outcomes == 2)


# ```{tip}
# Whenever you're using `|` or `&` you *must* use parentheses around the things you're comparing -- otherwise you'll get some weird errors or weirder results.
# ```

# ### More events
# 
# Humorously, we can also find the probability of the event containing zero outcomes, $\text{nothing} = \{\}$. Asking for the probability of this empty event is essentially asking for the probability that our experiment produces none of the possible results thus violates all universal laws. If this sounds impossible to you, you're right. The probability of an empty event is zero. Whew, existential crisis avoided.
# 
# On the other end of the spectrum, we could ask for the probability that any of our outcomes happen by specifying the event containing all outcomes -- statisticians have a special word for this event, called the 'sample space' -- $\text{sample space} = \{\text{outcome}_1,\ldots,\text{outcome}_n\}$. Necessarily our experiment must produce one of the possible outcomes, so the probability of observing an outcome sample space is one. Because we also know that the probability of an event is equal to the sum of the probabilities of each outcome it contains, we can equivalently state that the probabilities of all possible outcomes sum to one.
# 
# $$
# P(\mathrm{outcome}_1\textit{ or }\ldots\textit{ or }\mathrm{outcome}_n)
# = \sum_{\text{all outcomes}} P(\text{outcome}) = 1
# $$
# 
# Finally, the probability that some event does *not* happen is one minus the probability that it does. You can think of this as taking the sample space and removing the event that we're interested in *not* happening.
# 
# $$
# P(\textit{not }\mathrm{event}) = 1 - P(\mathrm{event})
# $$

# ### Probability of multiple events
# 
# If two events are deemed {dterm}`independent` -- meaning the two events have no effect on each other -- then we can calculate the chance that both of them occur by multiplying their probabilities.
# 
# $$
# P(\mathrm{event}_A\textit{ and }\mathrm{event}_B) = P(\mathrm{event}_A) \times P(\mathrm{event}_B) \\
# \tiny(\text{if independent})
# $$
# 
# This can be extended to work with many events, just so long as they are all independent.
# 
# $$
# P(\mathrm{event}_1 \textit{ and } \ldots \textit{ and } \mathrm{event}_n) = \prod_{i=1}^n P(\mathrm{event}_i) \\
# \tiny(\text{if independent})
# $$
# 
# Independence can be a tricky topic covered in your future probability classes, but for now understand that in most cases where multiple *trials* of an experiment are conducted, the outcomes of each trial are independent from each other.

# ### Probability of at least one success
# 
# If an experiment produces multiple outcomes, such as flipping two coins as opposed to just one, we may wish to find the probability that *any* of the outcomes successfully satisfies some condition.
# 
# In this setting, we may be interested the probability that at least one of our coins lands on Heads. Drawing out all possible outcomes makes answering this probability trivial -- but drawing out all possible outcomes becomes really painful when working with more and more complex experiments.
# 
# Fortunately, we can utilize some cleverness to rearrange our question. Consider that 'at least one success' is the same thing, logically, as 'not none of the outcomes are successful'...
# 
# $$
# P(\text{at least one success}) = P(\textit{not}\text{ no successes})
# $$
# 
# Often times, calculating the probability of 'no successes' is easier than trying to define every possible outcome. In the n-coin flip setting, we know that there's only outcome where none of our coins land on Heads -- no matter how many coins we use.

# ## A general way to find probabilities
# 
# In the example above, we already knew the probability of each outcome (and therefore each event).
# 
# What if we wanted to *find* those probabilities in real life? Let's look at the rain example.
# 
# When you look outside and see dark clouds, you want to estimate the probability that it will rain so you can know whether or not to stay indoors. Whenever you see dark clouds you start keeping track of whether or not it rained that day. Of the 20 days with dark clouds you've seen so far, 16 of them have also rained. Seems like dark clouds indicate an $\frac{16}{20} = 80\%$ chance of rain, huh?
# 
# Humans have a very natural intuition for what statisticians call the {dterm}`frequentist` approach towards probabilities. This approach doesn't need any pre-existing assumptions about our outcomes -- we only need to count the number of times some event did or didn't happen. When we divide the number of times it did happen by the total number of observations we made, we get a pretty good approximation of the underlying true probability. This approximation only gets better as the number of our observations increases.
# 
# $$P(\text{event}) \approx \frac{\text{# times event observed}}{\text{total # observations}}$$
# 
# If you remember our introduction to {dterm}`proportions` in Exploring Data, you'll notice that the calculation of an experimental probability is the exact same as the calculation of a proportion! In the same way we utilize computers to crunch numbers and spit out proportions, we'll learn to leverage computers to simulate events and calculate probabilities.

# ### The number of observations is important
# 
# Our approximation of the experimental probability will get closer and closer to the true underlying probability as we make more observations.
# 
# Theoretically, the equality only holds once you've made infinite observations... in practice it can be pretty challenging to make infinite observations!
# 
# Truthfully, we expect our experimental probability to be a little bit incorrect, simply due to randomness. You wouldn't expect to get exactly five Heads *every* time you flip ten coins. Sometimes you'll get more, sometimes less... it's possible that you might even see no Heads (though extremely rare)!
# 
# We should always strive to make more observations, since with fewer observations slight deviations are exaggerated. For example, if you flip ten coins, then getting one more or less Heads will change your experimental probability by an entire $0.1$. Whereas if you make one-hundred observations a single deviation only chances our probability by $0.01$.
# 
# Because it's never possible to make infinite observations, we must accept the use of a smaller number of observations, but remain cognizant that we lose both accuracy and precision as the number of observations decreases -- we'll talk about how to deal with this more when we discuss sampling.

# ## Complex experiments and simulation
# 
# The real world can throw some pretty challenging events at us.
# 
# How would you calculate probabilities in experiment which involve two dice? What if you had three dice? One hundred dice followed by thirty coin flips and a slot machine? We *could* learn about combinatorics in order to calculate the probabilities of events in these experiments, but we'll save that for your math courses!
# 
# Fortunately, we can rely on the frequentist approach and use computers to simulate a bunch of experiments, allowing us to approximate the true probability of any specified event -- just so long as we know (or can estimate) the probabilities of the individual component outcomes.

# ### The Birthday Problem
# 
# Suppose you look around your classroom and count a total of 23 students (including yourself). Assuming it's equally likely for someone's birthday to be on any day of the year (ignoring February 29th, sorry!), would you expect that at least two people in your class share the same birthday?
# 
# To answer this uncertain question, we'll need to come up with the probabilities that two people do or don't share a birthday, then side in favor of whichever probability is greater.
# 
# Using our intuitive frequentist approach, we're going to need to repeat the experiment many times. That means we could physically go out into the world, gather 23 people from the global population and see if any of them share a birthday, then do it again, like a lot of times... good luck with that! You'll be hard pressed to find the time, willingness, or funding necessary to conduct such a study.
# 
# Because we have an assumption about the probability of each birthday occurring, we can rely on a computer simulation instead!

# ### Conducting a probability simulation
# 
# Every time we conduct a simulation to estimate a probability, we follow the same four general steps:
# 
# 1. Frame your experiment, outcomes, and event of interest
# 2. Write the code to simulate a single outcome
# 3. Call that code lots of times and keep track of the outcomes
# 4. Calculate the experimental probability of your event
# 
# #### Step 1. Frame the experiment
# 
# Starting with step one of simulation, let's frame the experiment, outcomes, and event of interest an attempt to get a better grasp of this unintuitive Birthday Problem.
# 
# - Experiment: Select 23 birthdays at random from 1 to 365 (inclusive) and see whether or not there are any shared birthdays  
# - Outcomes: $\{\text{True}, \text{False}\}$  
# - Event: $\{\text{True}\}$
# 
# 
# #### Step 2. Simulate a single trial
# 
# Moving on to step two, we translate the description of our experiment into Python code. We can use NumPy to easily generate 23 random birthdays.

# In[7]:


classmate_birthdays = np.random.choice(range(1, 365+1), 23)
classmate_birthdays


# In order to see if any of the birthdays are shared, we can check if the number of unique elements in our array of birthdays is smaller than the total number of randomly selected birthdays.

# In[8]:


unique_birthdays = np.unique(classmate_birthdays)

any_shared = len(unique_birthdays) < len(classmate_birthdays)
any_shared


# Now that we have working code to simulate a single trial of the experiment, we want to wrap it all into a function so that we can easily call it in the future. (Remember to write a docstring or some comments to help *future you* remember what your code does!)

# In[9]:


def run_birthday_experiment():
    """
    Performs a single trial of the Birthday Problem experiment.
    
    - Selects 23 birthdays at random (1 to 365)
    - Returns whether or not any birthdays are shared by multiple people
    """
    
    classmate_birthdays = np.random.choice(range(1, 365+1), 23)
    
    unique_birthdays = np.unique(classmate_birthdays)
    
    any_shared = len(unique_birthdays) < len(classmate_birthdays)
    
    return any_shared

run_birthday_experiment()


# #### Step 3. Use a `for` loop to perform multiple trials
# 
# Arriving at step three, we need a way to run this custom function multiple times -- how do we do this? In programming the concept of repeatedly executing code is called 'iteration', and it is commonly carried out in Python using a **`for` loop**.
# 
# The syntax for running something many times is as follows. Just like with functions, the code you want repeated must be indented.
# 
# ```html
# for i in range(<number_of_repetitions>):
#     # Indented lines will be run each iteration of the loop
#     <code_that_you_want_run_multiple_times>
# 
# # Once outdented, the following code only runs after the loop is complete
# <code_that_will_run_after_the_loop>
# ```
# 
# Let's see what happens if we double a number three times using a for loop, then get that variable as an output.

# In[10]:


double_me = 1

for i in range(3):
    
    double_me = double_me * 2


# The code inside our loop has been run three times. Loops don't spit out return values, they simply execute instructions multiple times. Their effects are persistent, though! So, if we add a print statement outside of the loop (after it completes) we'll see that indeed the value of `double_me` has been doubled three times!

# In[11]:


double_me = 1

for i in range(3):
    
    double_me = double_me * 2
    
print(double_me)


# When running a simulation, we'd like to keep track of the outcome of each trial, not just the final outcome. Since we know that we can modify variables within a for loop, we can keep track of our outcomes by creating an empty list and then adding each trial to it within the loop. This is accomplished by using the `.append` list method with the outcome as an argument.

# In[12]:


outcomes = []

outcomes.append(True)

outcomes


# Putting this all together, let's finally run out Birthday Problem experiment a handful of times. Start by creating the empty list which will contain our outcomes and defining how many trials we will conduct.
# 
# Recall from our introduction to frequentist probability that as the number of observations increases our probability approximation will be better. Before you try to run an infinite number of trials, remember that the more iterations we simulate, the longer our code will take to run. But since this simulation doesn't take too much processing power, let's start with $10,000$ trials. Make sure to keep track of this number, since we'll need it to calculate the experimental probability. Then, within our loop append the outcome of a single experiment run to our list.

# In[13]:


trials = 10_000
outcomes = []

for i in range(trials):
    
    any_shared = run_birthday_experiment()
    outcomes.append(any_shared)


# #### Step 4. Calculate the experimental probability
# 
# For the final step four, we just need to use the formula for experimental probability to calculate an approximate probability for the chance that at least one pair of our 23 classmates will share a birthday. Recall this formula is $P = \frac{\text{# times event observed}}{\text{total # of trials}}$.
# 
# Back outside of the loop, let's turn our list into a NumPy array in order to unlock the extra capabilities that NumPy provides like element-wise comparisons. To count how many times our outcomes satisfied our event, we can use a comparison operator on our outcome array, then take the sum. Finally, we divide by the number of trials to arrive at our approximate probability.

# In[14]:


outcomes = np.array(outcomes)
sum(outcomes == True) / trials


# No way, really? According to our simulation, there's over a $50\%$ chance that at least one of the 23 students will share their birthday with someone else in the class.

# ## Simulations are approximate
# 
# Simulation isn't a perfect substitute for theoretical math -- but the approximations made by our simulations can be pretty close!
# 
# As the number of trials increases, we expect that our approximation gets better and better, but of course there is still some random chance involved that can throw things off.
# 
# Let's calculate the theoretical probability of the birthday problem to see how close we really got.
# 
# By relying on what we learned about `for` loops and our handy $P(\text{at least one}) = 1 - P(\text{none})$ rule, we can actually solve this problem with relative ease. Even though we're starting to doing math here, the math isn't that scary when we can rely on Python as an incredible calculator.
# 
# First, let's rearrange our probabilities. Our key event which we consider a success is two students having the same birthday. Therefore, no success would correspond to every birthday being different:
# 
# $$
# P(\text{at least one pair has the same birthday}) = 1 - P(\text{all 23 birthdays different})
# $$
# 
# We'll figure out how to calculate this probability by imagining our process: we ask each student, one at a time, when they're birthday is.
# 
# Since the birthday of any given student doesn't depend on the birthday of another student -- they are independent -- we can calculate the probability that all birthdays are different by multiplying the probability that the second student's birthday is different than the first, then the probability that the third is different from the first and second, and so on. This uses our $\it{and}$ rule.
# 
# When we ask the first student, they have a 100% chance of having a unique birthday so far. When we ask the second student, there's now a 364/365 probability that they're birthday is different from the first. Then we move to the third and now two birthdays are taken up, so there is a 363/365 probability that the third student's birthday is unique. Each time, the probability of a unique birthday decreases by one in the numerator (since one less possibility is considered unique) and remains the same on the denominator (since there are still 365 possibilities).
# 
# Let's chuck that into Python using a loop.

# In[15]:


num_students = 23

prob = 1 # Starting value -- we need something to multiply with
for position in range(num_students):
    
    prob = prob * (365 - position) / 365
    
prob_at_least_one_shared = 1 - prob
prob_at_least_one_shared


# Hey, our simulation was pretty close!
