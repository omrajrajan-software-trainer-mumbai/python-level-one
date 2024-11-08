# Program to count number of occurances of a letter in a word using dict in Python
# Chapter - 9.1 pg 111

word = 'malayalam'
letter_count_dictionary = dict()

for current_letter in word:
    if current_letter not in letter_count_dictionary:
        letter_count_dictionary[current_letter] = 1
    else:
        letter_count_dictionary[current_letter] = letter_count_dictionary[current_letter] + 1
        
print(letter_count_dictionary)
