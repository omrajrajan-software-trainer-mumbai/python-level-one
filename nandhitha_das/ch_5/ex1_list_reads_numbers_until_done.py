# Program which repeatedly reads numbers until the user enters “done” using list
# ex 1 of 5.9 pg 65
    
# declaration and initialization
list_of_numbers = []
count = 0
average = 1

# creating a controlled infinite loop with while
while True:

    # taking input from user using the built-in input() function
    current_number = input("Enter a number: ")

    if current_number[0]=="#":
        continue
    if current_number =="done":
        break
    
    # using exception handling with try and except
    try:
        current_number = int(current_number)
    except:
        print("Error: Invalid Input")
        continue
    list_of_numbers.append(current_number)

# calculating the average of the list of numbers
# using list functions sum() and len()
average = sum(list_of_numbers)/ len(list_of_numbers)

# printing the final results
print("The total of numbers are:", sum(list_of_numbers))
print("The count of numbers are:", len(list_of_numbers))
print("The average of numbers are:", average)

