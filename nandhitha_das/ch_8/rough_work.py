Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
print(cheeses[0])
Cheddar
numbers[1] = 5
print(numbers)
[17, 5]
'Edam' in cheeses
True
'Brie' in cheeses
False
for cheese in cheeses:
... print(cheese)
SyntaxError: expected an indented block after 'for' statement on line 1
>>> for cheese in cheeses:
...     print(cheese)
... 
...     
Cheddar
Edam
Gouda
>>> for i in range(len(numbers)):
...     numbers[i] = numbers[i] * 2
...     
>>> 
>>> for i in range(len(numbers)):
...     numbers[i] = numbers[i] * 2
... 
...     
>>> 5
5
>>>  a = [1, 2, 3]
...  
SyntaxError: unexpected indent
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> a[1:2]
[2]
>>> a.append('d')
>>> print(a)
[1, 2, 3, 'd']
>>> a.extend(b)
>>> print(a)
[1, 2, 3, 'd', 4, 5, 6]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
