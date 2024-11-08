#5.3
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#5.4
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
