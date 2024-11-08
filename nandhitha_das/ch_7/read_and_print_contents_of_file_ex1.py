# Program to read through a file and print the contents of the file in upper case
# Ex-7.11 pg 89

print("\nProgram to read through a file and print the contents of the file (line by line) all in upper case\n")

# taking user input using input() and storing in file_name variable
name_of_file = input('Enter the file name: ')

# Variable declaration and initialization
start_string = 'From'

#create file handler using open() and name of file
file_handler = open(name_of_file)

#create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    current_single_line = current_single_line.rstrip()
    # Skips uninteresting lines
    if not current_single_line.startswith(start_string):
        continue
    uppercase_current_single_line = current_single_line.upper()
    print(uppercase_current_single_line)
