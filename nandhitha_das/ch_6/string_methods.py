Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\HP\Documents\Python Class\ch_6\string_comparison_2.py
Your word,fruits, comes after banana.
stuff = 'Hello world'
type(stuff)
<class 'str'>
dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(str.capitalize)
Help on method_descriptor:

capitalize(self, /) unbound builtins.str method
    Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower
    case.

>>> word = 'banana'
>>> 
... new_word = word.upper()
>>> print(new_word)
BANANA
>>> index = word.find('a')
>>> print(index)
1
>>> word.find('na')
2
>>> word.find('na', 3)
4
>>> line = ' Here we go '
>>> line.strip()
'Here we go'
>>> line.startswith('Have')
False
>>> line.lower()
' here we go '
