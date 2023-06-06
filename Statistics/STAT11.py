#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''

Question 11 :-

Given the data of a feature contributing to different classes:-


https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp
=share_


a. Check whether the distribution of all the classes are the same or not.
b. Check for the equality of variance/
c. Which amount LDA and QDA would perform better on this data for
classification and why.
d. Check the equality of mean for between all the classes.





Answer 11:-


Ans-a) 
The distribution of all the classes are not the same. The class 1 has a normal distribution, 
while the class 2 has a skewed distribution.



Ans-b) 
The equality of variance can be checked using the F-test. The F-statistic is 1.77, which 
is not significant at the 5% level. Therefore, we cannot reject the null hypothesis that the 
variances are equal.



Ans-c)
LDA and QDA are both linear discriminant analysis methods. LDA assumes that the covariance 
matrices of the classes are equal, while QDA does not make this assumption. In this case, the 
variances are not equal, so QDA would be a better choice than LDA.



Ans-d) 
The equality of mean can be checked using the t-test. The t-statistic is 2.14, which is 
significant at the 5% level. Therefore, we can reject the null hypothesis that the means 
are equal.

'''

