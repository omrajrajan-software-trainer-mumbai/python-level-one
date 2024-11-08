# Program which repeatedly reads numbers until the user enters “done” using list
# ex 2 of 5.9 pg 66
    
#initialization
list_of_numbers = []

# creating a controlled infinite loop with while
while True:

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
    maximum_number = max() > current_number
    minimum_number = min() < current_number
    
# calling the function 
print("The maximum of these numbers are:", maximum_number)
print("The minimum of these numbers are:", minimum_number)
