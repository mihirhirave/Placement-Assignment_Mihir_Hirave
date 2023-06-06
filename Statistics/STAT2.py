#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''


Question 2:-

Consider a dataset containing the heights (in centimeters) of 1000 individuals. The
mean height is 170 cm with a standard deviation of 10 cm. The dataset is approximately
normally distributed, and its skewness is approximately zero. Based on this information,
answer the following questions:

a. What percentage of individuals in the dataset have heights between 160 cm
and 180 cm?

b. If we randomly select 100 individuals from the dataset, what is the probability
that their average height is greater than 175 cm?

c. Assuming the dataset follows a normal distribution, what is the z-score
corresponding to a height of 185 cm?

d. We know that 5% of the dataset has heights below a certain value. What is
the approximate height corresponding to this threshold?

e. Calculate the coefficient of variation (CV) for the dataset.

f. Calculate the skewness of the dataset and interpret the result.


'''






'''
Answer 2:-


Ans-a) To find the percentage of individuals with heights between 160 cm and 180 cm,
we need to calculate the z-scores for these heights and find the corresponding areas
under the normal distribution curve.

The z-score formula is given by: z = (x - μ) / σ

For 160 cm:
z1 = (160 - 170) / 10 = -1

For 180 cm:
z2 = (180 - 170) / 10 = 1

Using a standard normal distribution table or a calculator, we can find the area between -1 and 1, 
which represents the percentage of individuals with heights between 160 cm and 180 cm. 
This area is approximately 68%.

Therefore, approximately 68% of individuals in the dataset have heights between 160 cm and 180 cm.



Ans-b) If we randomly select 100 individuals from the dataset, the sample mean height will still
follow a normal distribution with the same mean as the population but with a standard deviation 
equal to the population standard deviation divided by the square root of the sample size.

Standard deviation of the sample mean = σ / sqrt(n)
= 10 / sqrt(100)
= 10 / 10
= 1

To find the probability that the average height of the sample is greater than 175 cm, we need to
calculate the z-score for 175 cm, assuming a mean of 170 cm and a standard deviation of 1 cm.

z = (x - μ) / σ
= (175 - 170) / 1
= 5

Using a standard normal distribution table or a calculator, we can find the area to the right of z = 5.
This represents the probability that a randomly selected sample of 100 individuals has an average height 
greater than 175 cm.

Since the z-score of 5 is extremely large, the area under the curve is essentially 0. Therefore, the 
probability is almost 0.



Ans-c) To find the z-score corresponding to a height of 185 cm, we can use the same formula:

z = (x - μ) / σ
= (185 - 170) / 10
= 15 / 10
= 1.5

The z-score corresponding to a height of 185 cm is 1.5.



Ans-d)  We know that 5% of the dataset has heights below a certain value. This value corresponds 
to the z-score that has an area of 5% to its left in the standard normal distribution.

Using a standard normal distribution table or a calculator, we can find the z-score that has an 
area of 5% to its left. This z-score is approximately -1.645.

Now, we can find the corresponding height using the z-score formula:

z = (x - μ) / σ
-1.645 = (x - 170) / 10

Solving for x:

-1.645 * 10 = x - 170
-16.45 = x - 170
x ≈ 170 - 16.45
x ≈ 153.55

Therefore, the approximate height corresponding to the threshold below which 5% of the dataset 
falls is approximately 153.55 cm.




Ans-e)  The coefficient of variation (CV) is a measure of relative variability and is calculated 
by dividing the standard deviation by the mean and multiplying by 100% to express it as a percentage.

CV = (σ / μ) * 100
= (10 / 170) * 100
≈ 5.88%

Therefore, the coefficient of variation for the dataset is approximately 5.88%.



Ans-f)  The skewness of a dataset measures the asymmetry of its distribution. Since the dataset 
is approximately normally distributed and its skewness is approximately zero, it indicates that 
the dataset is symmetric. This means that the distribution is balanced and there is no significant 
skew to the left or right.


'''

