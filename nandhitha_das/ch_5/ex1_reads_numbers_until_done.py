# Program which repeatedly reads numbers until the user enters “done”
# ex 5.9 pg 65
    
# Defining a function that takes a random  number
def read_numbers(current_number):
    total = sum(current_number)
    count = count(current_number)
    average = mean(current_number)
    return read_numbers

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
        print("Error: Please enter a valid number only.\nRestart the program to try again")
        exit(0)
        
    # calling the function read_numbers()
    new_random_number = read_numbers(current_number)
    print("new random number:", new_random_number)




