# Parsing String
# program to look in to a string and find a substring
# 6.10 pg 74

print('\nChapter 6 - 6.10 - Parsing Strings - 01 \n')
print('Program to extract substring from a given text\n')

print('Using the built-in find() in Strings datatype to find positions of given characters / symbols')
data_to_search = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
index_position_at_attherate = data_to_search.find('@')
print('The Index Position of @ symbol:', index_position_at_attherate)

index_position_at_space = data_to_search.find(' ', index_position_at_attherate)
print('The Index Position of first space character after the @ symbol:', index_position_at_space)

host_address = data_to_search[index_position_at_attherate + 1 : index_position_at_space]
print('\nThe host address extracted using slicing feature and strip():', host_address.strip())

