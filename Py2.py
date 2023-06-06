#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Answer_2

def is_valid_string(s):
    # Count the frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the frequency of each frequency
    freq_count = {}
    for count in char_count.values():
        freq_count[count] = freq_count.get(count, 0) + 1

    # If there is only one frequency or two frequencies with a difference of one,
    # the string is valid
    if len(freq_count) == 1 or (len(freq_count) == 2 and 1 in freq_count.values()):
        return "YES"
    else:
        return "NO"



## Examples

print(is_valid_string("abc"))  # Output: YES
## All characters have same frequency, so the string is valid


print(is_valid_string("abcc"))  # Output: YES

## Character 'c' appears twice so we can remove 1 occurence to make all characters have the same frequency (1)


## Test case 1:
print(is_valid_string("aaabbbccc"))  # Output: YES

## All characters have the same frequency, so the string is valid


## Test case 2:
print(is_valid_string("aabcc"))  # Output: YES

## Character 'b' appears only once, so we can remove it to make all characters have the same frequency (2)

