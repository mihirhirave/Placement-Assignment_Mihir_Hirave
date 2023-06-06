#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''

Question 10 :-

A factory produces light bulbs, and the probability of a bulb being defective is 0.05.
The factory produces a large batch of 500 light bulbs.

a. What is the probability that exactly 20 bulbs are defective?
b. What is the probability that at least 10 bulbs are defective?
c. What is the probability that at max 15 bulbs are defective?
d. On average, how many defective bulbs would you expect in a batch of 500?





Answer 10:-


To solve these problems, we can use the binomial distribution, which models the probability of a certain 
number of successes (defective bulbs) in a fixed number of independent trials (total bulbs produced).

The binomial distribution is defined by two parameters: the number of trials (n) and the probability of 
success (p).


Ans-a)
The probability that exactly 20 bulbs are defective can be calculated using the binomial distribution formula:

P(X = k) = (n C k) * p^k * (1 - p)^(n - k)

where:
- n is the number of trials (500 bulbs)
- k is the number of successes (20 defective bulbs)
- p is the probability of success (0.05, probability of a bulb being defective)
- (n C k) is the number of combinations of n items taken k at a time

Using this formula, we can calculate:

P(X = 20) = (500 C 20) * (0.05^20) * (1 - 0.05)^(500 - 20) is Approx. 0.0355



Ans-b) 
The probability that at least 10 bulbs are defective can be calculated by summing the probabilities 
of having 10, 11, 12, ..., up to 500 defective bulbs. We can subtract the probability of having fewer 
than 10 defective bulbs from 1:

P(X >= 10) = 1 - P(X < 10)

To calculate P(X < 10), we sum the probabilities of having 0, 1, 2, ..., up to 9 defective bulbs.




Ans-c) 
The probability that at most 15 bulbs are defective can be calculated by summing the probabilities of 
having 0, 1, 2, ..., up to 15 defective bulbs:

P(X <= 15) = P(X = 0) + P(X = 1) + P(X = 2) + ... + P(X = 15) is Approx. 0.9999




Ans-d)  
The average number of defective bulbs can be calculated using the formula for the mean of a binomial 
distribution:

mean = n * p

Substituting the values:
mean = 500 * 0.05 = 25


'''

