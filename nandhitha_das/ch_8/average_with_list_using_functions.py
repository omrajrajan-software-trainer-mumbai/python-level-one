# Program to compute an average with a list and using functions()
# Ch 8 - 8.8

numlist = list()
while (True):
    input_value = input('Enter a number: ')
    if input_value == 'done':
        break
    value = float(input_value)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average:', average)
