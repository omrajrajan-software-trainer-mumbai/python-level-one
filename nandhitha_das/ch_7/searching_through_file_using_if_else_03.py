# Searching through files using File Handler, if-else, and open
# Ch-7.7 pg 87

print("\nSearching through files using File Handler, try, except, and open\n")

# variable initialization and declaration
file_name = input('Enter the file name: ')
if len(file_name)< 1:
    exit(0)
else:
    # create file handler using open() and name of file
    file_handler = open(file_name)
    print('File cannot be opened:', file_name)
    
iteration_counter = 0

# create a for loop to traverse through the file_handler object
for current_single_line in file_handler:
    if current_single_line.startswith('Subject:'):
        iteration_counter = iteration_counter + 1
print('There were', iteration_counter, 'subject lines in', file_name)

