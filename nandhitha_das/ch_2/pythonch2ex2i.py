Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name= int(input("Enter your name: ")
          print(name)
          
SyntaxError: '(' was never closed
name= int(input("Enter your name: "))
          print(name)
          
SyntaxError: multiple statements found while compiling a single statement

=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chuck
Traceback (most recent call last):
  File "C:/Users/HP/Downloads/pythonch2ex2.py", line 1, in <module>
    name= int(input("Enter your name: "))
ValueError: invalid literal for int() with base 10: 'chuck'
>>> name= input("Enter your name: ")
...           
Enter your name: 
=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chuck
chuck
>>> 
=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chuck
hellochuck
>>> 
=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chuck
hellochuck
Enter hours: 35
Enter rate: 2.75
Traceback (most recent call last):
  File "C:/Users/HP/Downloads/pythonch2ex2.py", line 6, in <module>
    Rate= int(input("Enter rate: "))
ValueError: invalid literal for int() with base 10: '2.75'
>>> 
=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chucko
hellochucko
Enter hours: 
Traceback (most recent call last):
  File "C:/Users/HP/Downloads/pythonch2ex2.py", line 5, in <module>
    Hours= int(input("Enter hours: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
=============== RESTART: C:/Users/HP/Downloads/pythonch2ex2.py ==============
Enter your name: chucko
hello chucko
Enter hours: 35
Enter rate: 2.75
Pay: 96.25
