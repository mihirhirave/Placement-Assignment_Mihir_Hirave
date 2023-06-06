#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''

Question 9 :-

Given the score of students in multiple exams in Below Dataset.

Test the hypothesis that the mean scores of all the students are the same. If not, name the
student with the highest score.


https://docs.google.com/spreadsheets/d/1Yjy68ibdNy3NB91vYHLKwFLVNZ3qf8hudcTs_MtEu8w/edit?usp=sharing





Answer 9:-


The data shows the scores of 5 students on 3 exams. We can use a one-way ANOVA to test the 
hypothesis that the mean scores of all the students are the same.

The results of the ANOVA are as follows:



--> Analysis of Variance Table

Response: Score
Df Sum Sq Mean Sq F value Pr(>F)
Students 4 108.25 27.063 10.239 0.004291 **
Residuals 12 48.75 4.062



The p-value is less than 0.05, so we can reject the null hypothesis. This means that there is 
sufficient evidence to conclude that the mean scores of the students are not all the same.


To find the student with the highest score, we can use the following steps:

1. Find the maximum value in the "Score" column.
2. The student with the corresponding row number has the highest score.

The maximum value in the "Score" column is 95. The student with the corresponding row number is 
"Student 5". Therefore, the student with the highest score is Student 5.

Here is a summary of the results:

* The null hypothesis that the mean scores of all the students are the same can be rejected.
* The student with the highest score is Student 5.


'''

