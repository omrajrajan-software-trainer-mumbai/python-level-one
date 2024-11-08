# Program to create function to find the largest value in a list or sequence

# defining the function largest_value to return largest number from the collection
def largest_value(list_numbers_array):
    largest_number = None
    
    for current_number in list_numbers_array:
        if largest_number is None or current_number > largest_number:
            largest_number = current_number
   
    return largest_number

list_numbers = [3, 141, 12, 119, 74, 15]

largest_number = largest_value(list_numbers)
print("largest number in the list is = ", largest_number)
