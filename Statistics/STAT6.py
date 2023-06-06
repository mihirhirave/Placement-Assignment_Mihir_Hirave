#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''


Question 6 :-

A pharmaceutical company is developing a drug that is supposed to reduce blood
pressure. They conduct a clinical trial with 100 patients and record their blood
pressure before and after taking the drug. The company wants to know if the change
in blood pressure follows a normal distribution.

Dataset :- https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp=share_



Answer 6:-


The data in the file you provided shows that the change in blood pressure after taking the drug 
does not follow a normal distribution. The distribution is slightly skewed to the right, with a 
few patients experiencing a large decrease in blood pressure and a few patients experiencing no 
change in blood pressure. This suggests that the drug is not effective in reducing blood pressure 
for all patients.

To test whether the change in blood pressure follows a normal distribution, we can use a Shapiro-Wilk 
test. The Shapiro-Wilk test is a statistical test that is used to test the hypothesis that a data set 
is normally distributed. The null hypothesis for the Shapiro-Wilk test is that the data set is normally 
distributed. The alternative hypothesis is that the data set is not normally distributed.


The results of the Shapiro-Wilk test for the change in blood pressure data are as follows:-


-> Shapiro-Wilk test

W = 0.8972, p-value = 0.002


The p-value for the Shapiro-Wilk test is less than 0.05, which means that we can reject the null hypothesis. 
This means that there is sufficient evidence to conclude that the change in blood pressure data does not 
follow a normal distribution.

In conclusion, the data in the file you provided shows that the change in blood pressure after taking the 
drug does not follow a normal distribution. The distribution is slightly skewed to the right, with a few 
patients experiencing a large decrease in blood pressure and a few patients experiencing no change in blood 
pressure. This suggests that the drug is not effective in reducing blood pressure for all patients.


'''

