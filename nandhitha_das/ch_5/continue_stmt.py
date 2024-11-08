#Program to demonstrate use of continue statement
#5.4 - page no 60
while True:
    current_line = input(">")
    if current_line[0]=="#":
        continue
#if the first char is #, ignore the line and skip the current iteration
    if current_line =="done":
#        print("line number 9")
        break
#        print("line number 11")
#if user types done, then exit the current loop using break statement
    print(current_line)
#    print("line number 14")
# print("line number 15")
# done. we are here because of break out of the loop and next statement is run
