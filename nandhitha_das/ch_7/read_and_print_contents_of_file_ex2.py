# Program to extract values and calculate average spam condidence in python
# Ex-7.11 pg 90

print("\nProgram to extract values and calculate average spam condidence in python\n")

# taking user input using input() and storing in file_name variable
name_of_file = input('Enter the file name: ')

# Variable declaration and initialization
start_string = 'X-DSPAM-Confidence:'
confidence_counter = 0
total_spam_confidence = 0
average_spam_confidence = 0

#create file handler using open() and name of file
file_handler = open(name_of_file)

#create a for loop to traverse through the file_handler object (collection)
for current_single_line in file_handler:
    current_single_line = current_single_line.rstrip()
    # Skips uninteresting lines
    if not current_single_line.startswith(start_string):
        continue
    # storing the floating-point number using the reverse slice feature
    current_float_point_number = float(current_single_line[-6:])
    confidence_counter = confidence_counter + 1
    total_spam_confidence = total_spam_confidence + current_float_point_number

average_spam_confidence = total_spam_confidence / confidence_counter
print("Average spam confidence:", average_spam_confidence)
