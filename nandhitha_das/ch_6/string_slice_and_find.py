# exercise 6.14 pg 77
# program to Use find and string slicing to extract the portion of the string after the colon

# Use find and string slicing to extract the portion of the string after the colon character
# and then use the float function to convert the extracted string into a floating point number.

print("\nProgram to use find and string slicing to extract the portion of the string after the colon")

data_to_search = 'X-DSPAM-Confidence:0.8475'
index_position_at_colon = data_to_search.find(':')
print('\nThe Index Position of : symbol:', index_position_at_colon)

number_slice = data_to_search[index_position_at_colon + 1 :]
print('\nThe number slice extracted using slicing feature and strip():', number_slice.strip())

print("\nThe type of number slice:", type(number_slice))

new_float_number_slice = float(number_slice)
print("\nThe floating point number extracted from the string:", new_float_number_slice)

print("\nThe type of converted number slice:", type(new_float_number_slice))
