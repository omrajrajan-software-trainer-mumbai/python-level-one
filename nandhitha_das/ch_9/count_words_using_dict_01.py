# Program to count number of occurances of a letter in a word using dict in Python
# Chapter - 9.3 pg 113

file_name = input("Enter the file name: ")

try:
    file_handler = open(file_name)
except:
    print("File not found:", file_name)
    exit(0)

word_count_dictionary = dict()

#nested for loop
for current_line in file_handler:
    word_list = current_line.split()

    for current_word in word_list:
        if current_word not in word_count_dictionary:
            word_count_dictionary[current_word] = 1
        else:
            word_count_dictionary[current_word] += 1
            
print(word_count_dictionary)
