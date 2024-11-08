# Reading files using File Handler and open() function in Python
# Ch-7 pg 82

print("\nReading files using File Handler and open() function in Python\n")

# Variable Declaration and Initialization
name_of_file = "renewable_energy.txt"
iteration_counter = 0

#create file handler using open() and name of file
file_handler = open(name_of_file)

#create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    iteration_counter = iteration_counter + 1

print("Line counter:", iteration_counter)
