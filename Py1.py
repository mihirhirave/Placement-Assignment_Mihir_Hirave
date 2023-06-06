#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Answer_1

from collections import Counter

def find_highest_frequency_word_length(input_string):
    words = input_string.split()

    word_frequency = Counter(words)

    max_frequency = max(word_frequency.values())

    highest_frequency_word_length = max(len(word) for word, freq in word_frequency.items() if freq == max_frequency)

    return highest_frequency_word_length


# Test case 1
input_str1 = "write write write all the number from from from 1 to 100"
result1 = find_highest_frequency_word_length(input_str1)
print("Length of the highest-frequency word in test case 1:", result1)



# Test case 2
input_str1 = "The world world world is going going going to fly fly fly fly"
result1 = find_highest_frequency_word_length(input_str1)
print("Length of the highest-frequency word in test case 1:", result1)



# Test case 3
input_str1 = "I I don't know know how how to float float float"
result1 = find_highest_frequency_word_length(input_str1)
print("Length of the highest-frequency word in test case 1:", result1)




'''

Test case 1:

The input string contains repeated words such as "write" and "from"
The word "write" occurs 3 times, while the word "from" occurs 3 times
The maximum frequency is 3, which corresponds to the word "write"
The length of the highest-frequency word "write" is 5
Therefore, the expected output is 5


Test case 2:

The input string contains repeated words such as "world", "going", "fly"
The word "world" occurs 3 times, the word "going" occurs 3 times, the word "fly" occurs 4 times
The maximum frequency is 4, which corresponds to the word "fly"
The length of the highest-frequency word "fly" is 3
Therefore, the expected output is 3


Test case 3:

The input string contains repeated words such as "I", "know", "how", "float"
The word "I" occurs 2 times, the word "know" occurs 2 times, the word "how" occurs 2 times, the word "float" occurs 3 times
The maximum frequency is 3, which corresponds to the word "float"
The length of the highest-frequency word "float" is 5
Therefore, the expected output is 5

'''

