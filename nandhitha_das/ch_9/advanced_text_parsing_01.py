# Program to count number of occurances of a letter in a word using dict in Python
# Chapter - 9.4 pg 115

import string

file_name = input("Enter the file name: ")

try:
    file_handler = open(file_name)
except:
    print("File not found:", file_name)
    exit(0)

word_count_dictionary = dict()

for current_line in file_handler:
    current_line = current_line.rstrip()
    current_line = current_line.translate(current_line.maketrans('','', string.punctuation))
    current_line = current_line.lower()
    list_of_words = current_line.split()
    for current_word in list_of_words:
        if current_word not in word_count_dictionary:
            word_count_dictionary[current_word] = 1
        else:
            word_count_dictionary[current_word] += 1

print(word_count_dictionary)
