Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sentence = spam-spam-spam
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sentence = spam-spam-spam
NameError: name 'spam' is not defined
sentence = 'spam-spam-spam'
delimiter = '-'
sentence.split(delimiter)
['spam', 'spam', 'spam']
>>> sentence = 'spam$spam$spam'
>>> delimiter = '$'
>>> sentence.split(delimiter)
['spam', 'spam', 'spam']
>>> new_line = [pining, for, the, fjords]
SyntaxError: invalid syntax
>>> new_line = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(new_line)
'pining for the fjords'
>>> fhand = open(mbox-short.txt)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fhand = open(mbox-short.txt)
NameError: name 'mbox' is not defined
>>> fhand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fhand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand = open('renewable_energy.txt')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fhand = open('renewable_energy.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'renewable_energy.txt'
>>> 
===== RESTART: C:/Users/HP/Documents/Python Class/ch_8/parsing_lines.py =====
Traceback (most recent call last):
  File "C:/Users/HP/Documents/Python Class/ch_8/parsing_lines.py", line 1, in <module>
    fhand = open(mbox-short.txt)
NameError: name 'mbox' is not defined
>>> 
===== RESTART: C:/Users/HP/Documents/Python Class/ch_8/parsing_lines.py =====
Traceback (most recent call last):
  File "C:/Users/HP/Documents/Python Class/ch_8/parsing_lines.py", line 1, in <module>
    fhand = open(text_01.txt)
NameError: name 'text_01' is not defined
