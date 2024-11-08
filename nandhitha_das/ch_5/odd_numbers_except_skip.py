# program to print odd numbers except one number
# 5.4 pg59

# starting value
initial_value = 1
# ending value
ending_value = 10
# increment/ decrement value
increment_value = 2
# store the value to skip
skip_value = int(input("Enter a value to skip: "))

# setting initial value for the loop
counter = initial_value

# creating a while loop using condition
while counter < ending_value:
    # check if the current value is the skip value
    if counter == skip_value:
        counter = counter + increment_value
        continue
    else:
        print("Current value of the loop: ", counter)
        counter = counter + increment_value
