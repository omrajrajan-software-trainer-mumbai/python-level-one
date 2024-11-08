# Writing files using File Out Handler and write() in Python.
# Ch-7.8 pg 88

print("\nWriting files using File Out Handler and write() in Python\n")

try:
    # create file output handler using open(), name of file and mode
    file_out_handler = open('output.txt', 'w')

except:
    print(file_out_handler)
    exit()
    
line1 = "This here's the wattle,\n"
file_out_handler.write(line1)
line2 = 'the emblem of our land.\n'
file_out_handler.write(line2)
file_out_handler.close()
