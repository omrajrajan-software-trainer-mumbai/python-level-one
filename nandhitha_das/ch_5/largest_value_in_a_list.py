# Program to find the largest value in a list or sequence

list_numbers = [3, 41, 12, 119, 74, 15]
largest_number = None

# creating a for each loop to loop through each item in the list
for current_number in list_numbers:
    if largest_number is None or current_number > largest_number:
        largest_number = current_number
        
    # print("Loop: ", current_item, largest_number)
    
print("largest number in the list is = ", largest_number)

