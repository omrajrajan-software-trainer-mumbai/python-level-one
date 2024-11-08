# Searching through files using File Handler, open() and startswith() function in Python
# Ch-7.5 pg 83

print("\nSearching through files using File Handler, open() and startswith() function in Python\n")

# Variable Declaration and Initialization
name_of_file = "renewable_energy.txt"

#create file handler using open() and name of file
file_handler = open(name_of_file)

#create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    if current_single_line.startswith('In'):
        print(current_single_line)
