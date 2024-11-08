# Round 2 Questions

#1
#sum = 0
#for i in range(1,6):
#    sum += i
#print(sum)

#2
#numbers = [3, 6, 2, 8, 4]
#max_number = numbers[0]
#for num in numbers:
#    if num > max_number:
#        max_number = num
#print(max_number)


#3
#numbers = [1, 2, 2, 3, 4, 4, 5]
#unique_numbers = [1,2,3,4,5]
#for num in numbers:
#    if num not in numbers:
#        unique_numbers.remove(num)
#print(unique_numbers)

#4
#num = int(input())
#if num % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

#5
#def celsius_to_fahrenheit(celsius):
#    return (celsius * 9/5) + 32
#print(celsius_to_fahrenheit(100))

#6
#list1 = [1,2,3]
#list2 = [4,5,6]
#new_list = list1.append(list2[])
#print(new_list)

#7
#def square(num):
#    return num * num
#print(square(5))

#8
#string = "hello"
#count = 0
#for ch in string:
#    if ch == 'l':
#        count = count + 1
#print(count)

#9
file = open("renewable_energy.txt", "r")
content = file.read()
file.close()
print(content)

#10
#def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial(n - 2)
#print(factorial(5))

#11
#number = 5
#for i in range(1, 11):
#    print(number * i)
#    continue

#12
#numbers = [1, 2, 3, 4, 5, 6]
#even_numbers = [num for num in numbers if num % 2 == 0]
#print(even_numbers)

#13
#numbers = [1, 2, 3, 4, 5, 6]
#for num in numbers:
#    if num % 2 == 0:
#        print(num)
#    else:
#        continue

#14
#def is_palindrome(s):
#    return s == s[::-2]
#print(is_palindrome("radar"))


#15
#cart = [{"item": "apple", "price": 10}, {"item": "banana", "price": 5}]
#total = 0
#for product in cart:
#    total += product["price"]
#print("Total: " + total)
