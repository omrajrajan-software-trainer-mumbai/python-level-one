# Taking the filename from the user
# Ch-7.6 pg 85

print("\n Taking the filename from the user\n")

# variable initialization and declaration
iteration_counter = 0
search_topic = 'Adani'

# taking user input using input() and storing in file_name variable
file_name = input('Enter the file name: ')

# create file handler using open() and name of file
file_handler = open(file_name)

# create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    if current_single_line.startswith(search_topic):
        iteration_counter = iteration_counter + 1
        
print('There were', iteration_counter, 'related to the subject', search_topic, 'in', file_name)
