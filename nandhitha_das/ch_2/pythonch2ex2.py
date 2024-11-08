#program to prompt a user for their name and then welcomes them.
name= input("Enter your name: ")
print("hello " + name)

#program to prompt the user for hours and rate per hour to compute gross pay. 
Hours= int(input("Enter hours: "))
Rate= float(input("Enter rate: "))
Pay= Hours * Rate
print("Pay:", Pay)
