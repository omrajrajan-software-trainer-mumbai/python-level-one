# Skipping the line based on string passed to find()
# Ch-7.5 pg 85

print("\nSkipping the line based on string passed to find()\n")

# Variable Declaration and Initialization
name_of_file = "renewable_energy.txt"

#create file handler using open() and name of file
file_handler = open(name_of_file)

#create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    current_single_line = current_single_line.rstrip()
    if current_single_line.find('Adani') == -1:
        continue
    print(current_single_line)

