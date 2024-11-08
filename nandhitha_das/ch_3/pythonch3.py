Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5==5
True
5==6
False
type(True)
<class 'bool'>
type(False)
<class 'bool'>
17 and True
True
if x > 0 :
    print('x is positive')

    
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    if x > 0 :
NameError: name 'x' is not defined
x=10
if x > 0 :
    print('x is positive')

    
x is positive
if x < 0 :
    pass


x = 3
if x < 10:
    print('Small')

    
Small
 print('Done')
 
SyntaxError: unexpected indent
print('Done')
Done
if x%2 == 0 :
print('x is even')
SyntaxError: expected an indented block after 'if' statement on line 1
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
    
x is odd
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
    
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    if x < y:
NameError: name 'y' is not defined
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
x=1
y=2
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
...         
x is less than y
>>> if 0 < x:
...     if x < 10:
...         print('x is a positive single-digit number.')
...         
x is a positive single-digit number.
>>> if 0 < x and x < 10:
...     print('x is a positive single-digit number.')
...     
x is a positive single-digit number.
>>> inp = input('Enter Fahrenheit Temperature: ')
Enter Fahrenheit Temperature: 55
>>> fahr = float(inp)
>>> cel = (fahr - 32.0) * 5.0 / 9.0
>>> print(cel)
12.777777777777779
>>> inp = input('Enter Fahrenheit Temperature:')
... try:
...     fahr = float(inp)
...     cel = (fahr - 32.0) * 5.0 / 9.0
...     print(cel)
... except:
...     print('Please enter a number')
...     
SyntaxError: multiple statements found while compiling a single statement
>>> inp = input('Enter Fahrenheit Temperature:')
... try:
...     fahr = float(inp)
...     cel = (fahr - 32.0) * 5.0 / 9.0
...     print(cel)
... except:
...     print('Please enter a number')
...     
SyntaxError: multiple statements found while compiling a single statement
>>>  x >= 2 and (x/y) > 2 and y != 0
...  
SyntaxError: unexpected indent
>>> x >= 2 and (x/y) > 2 and y != 0
False
