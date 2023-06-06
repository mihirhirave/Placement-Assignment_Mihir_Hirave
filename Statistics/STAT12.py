#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''


Question 12 :-


A pharmaceutical company develops a new drug and wants to compare its
effectiveness against a standard drug for treating a particular condition. They conduct a
study with two groups: Group A receives the new drug, and Group B receives the standard
drug. The company measures the improvement in a specific symptom for both groups after
a 4-week treatment period.


a. The company collects data from 30 patients in each group and calculates the
mean improvement score and the standard deviation of improvement for each
group. The mean improvement score for Group A is 2.5 with a standard
deviation of 0.8, while the mean improvement score for Group B is 2.2 with a
standard deviation of 0.6. Conduct a t-test to determine if there is a significant
difference in the mean improvement scores between the two groups. Use a
significance level of 0.05.

b. Based on the t-test results, state whether the null hypothesis should be
rejected or not. Provide a conclusion in the context of the study.




Answer 12:-


To determine if there is a significant difference in the mean improvement scores between Group A 
and Group B, we can conduct a t-test. The null hypothesis (H0) assumes that there is no significant 
difference between the two groups, while the alternative hypothesis (H1) assumes that there is a 
significant difference.


Ans-a)
Let's perform the t-test using the given data:

For Group A:
Mean improvement score (x̄1) = 2.5
Standard deviation (s1) = 0.8
Sample size (n1) = 30


For Group B:
Mean improvement score (x̄2) = 2.2
Standard deviation (s2) = 0.6
Sample size (n2) = 30


We can use the two-sample independent t-test formula, which compares the means of two independent groups:

t = (x̄1 - x̄2) / sqrt((s1^2 / n1) + (s2^2 / n2))


Plugging in the values:
t = (2.5 - 2.2) / sqrt((0.8^2 / 30) + (0.6^2 / 30))


Calculating:
t = 0.3 / sqrt(0.02133 + 0.012)
t ≈ 0.3 / sqrt(0.03333)
t ≈ 0.3 / 0.18257
t ≈ 1.642



Ans-b)
Since the p-value is less than 0.05, the null hypothesis is rejected. There is evidence to suggest 
that there is a difference in the mean improvement scores between the two groups. The new drug appears 
to be more effective than the standard drug in treating the condition.


'''

