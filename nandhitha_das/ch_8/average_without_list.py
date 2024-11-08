# Program to compute an average without a list
# Ch 8 - 8.8

total = 0
count = 0
while (True):
    input_value = input('Enter a number: ')
    if input_value == 'done':
        break
    value = float(input_value)
    total = total + value
    count = count + 1
    
average = total / count
print('Average:', average)

