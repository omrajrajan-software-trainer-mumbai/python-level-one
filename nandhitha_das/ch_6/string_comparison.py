Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> if word == 'banana':
...     print('All right, bananas.')
... 
...     
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined. Did you mean: 'ord'?
>>> if word == 'banana':
... print('All right, bananas.')
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if word < 'banana':
... print('Your word,' + word + ', comes before banana.')
... elif word > 'banana':
... print('Your word,' + word + ', comes after banana.')
... else:
... print('All right, bananas.')
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if word < 'banana':
...     print('Your word,' + word + ', comes before banana.')
... elif word > 'banana':
...     print('Your word,' + word + ', comes after banana.')
... else:
...     print('All right, bananas.')
... 
...     
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    if word < 'banana':
NameError: name 'word' is not defined. Did you mean: 'ord'?
