# #create a pyramid of star

# for i in range(0,5):
#     print('*'*i)



# str = 'A'
# for i in range(1,5):
#     print(str * i)


# for i in range(0,5):
#     print(chr(65 + i) * (i + 1))

# for i in range(0,6):
#     print(chr(i) * (i - 1))

# for i in range(0,5):
#     print(chr(65 + i)*(i + 1))

# for i in range(0,4):
#     print(chr(49 + i)* (i + 1))

# n = 5
# for i in range(0,n):
#     print(' ' * (n - i) + '*' * i)

# n = 4
# for i in range(0,n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# n = 4
# for ch in range(n):
#     print((ord('A') + ch - 1) * ch)

# for i in range(0,1):
#     for j in range(0,4):
#         print(chr(49 + j) * (j + 1))


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(str(j),end=' ')
#     print()


# n = 14
# for i in range(10,n):
#     for j in range(10,i+1):
#         print(str(j),end=' ')
#     print()

# n = 10
# for i in range(1,5):
#     for j in range(i):
#         print(n,end=' ')
#         n += 1
#     print()

# n = 65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(n),end=' ')
#         n += 1
#     print()
# print()


# n = 65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(n + j),end=' ')
#     print()
# print()


# n = 65
# for i in range(0,1):
#     for j in range(0,4):
#         print(chr(n + j) * (j + 1))
#     print()



# for i in range(0,4):
#     for j in range(0,8):
#         print(('*'),end=' ')
#     print()

# for k in range(4):
#     print('*')


# l = [1,2,3,4]
# l1 = reversed(l)
# print(list(reversed(l)))

# l = [23,34,56,78,12,34,56,2]
# l1 = sorted(l)
# if len(l1) < 5:
#     print(list(reversed(l1)))


# from random import randint

# list1 = []
# for numbers in range(10):
#     numbers = randint(1,50)
#     list1.append(numbers)

# print(list(sorted(list1)))

# from random import randint

# def my_list():
#     list1 = []
#     for numbers in range(10):
#         numbers = randint(1,50)
#         list1.append(numbers)
#     print(list(sorted(list1)))

# my_list()


# from random import randint
# class MyList():
#     def __init__(self):
#         self.list1 = []

#     def display(self):
#         for numbers in range(10):
#             numbers = randint(1,50)
#             self.list1.append(numbers)
#         print(list(sorted(self.list1)))

# l1 = MyList()
# l1.display()

# from random import randint
# class MyList():
#     def __init__(self):
#         self.list1 = []

#     def display(self):
#         for numbers in range(10):
#             numbers = randint(1,50)
#             self.list1.append(numbers)
#         print(list(sorted(self.list1)))

# l1 = MyList()
# l1.display()


# from random import randint

# # Create a class for the list of random numbers
# class MyList():
#     def __init__(self):
#         self.list1 = []

#     def display(self):

#         # declare the clear() function for clear the old list of numbers
#         self.list1.clear() 

#         for numbers in range(10): # Range is use to create the size of list 10
#             numbers = randint(1,50) # Randint is use for contains a random numbers from 1 to 50 in the list
#             self.list1.append(numbers) # append always use for the list if you want to add any number or list of numbers
#         print(f'Random numbers of list is\n{list(sorted(self.list1))}')

# #Execute the random numbers of list
# l1 = MyList()
# l1.display()

# n = 0
# while n == 0:
#     for i in range(4):
#         print('*' * i)
#     n += 1

# n = 0
# while n == 0:
#     for i in range(0,5):
#         for j in range(0,10):
#             print(chr(65 + j),end='')
#         print()
#     for k in range(4):
#         print(chr(65 + k))
#     n += 1

# n = 0
# while n == 0:
#     for i in range(0,1):
#         for j in range(0,5):
#             print(chr(65 + j) * (j + 1))
#     n += 1

# n = 0
# ab = 65
# while n == 0:
#     for i in range(0,5):
#         for j in range(i):
#             print(chr(ab),end=' ')
#             ab += 2
#         print()
#     n += 1


# def is_multiple(m,n):
#     for i in range(n):
#         if n == m * i:
#             return True
#         return False
# print(is_multiple(5,4))


# def is_even(k):
#     if k == 2:
#         return True
#     return False

# print(f'K is even = {is_even(2)}')
# print(f'K is even = {is_even(3)}')

# print(9//2)

# i = 0
# while i < 3:
#     print(i)
#     i += 1
#     print(i+1)

# s = print
# s('hello')

# print(type(type(int)))

# L = ['a','b','c','d']
# print("".join(L))

# print(chr(ord('A')))

# y = 8
# z = lambda x : x * y
# print(z(6))

# x = 'A'
# print(id(x))
# print(type(id))

# list1 = [3,4,5,20,5,25,1,3]
# l = list1.pop(1)
# print(l)


# s = "Welcome"
# print(s[0:5:2])

# def minmax(data):
#     data = [23,34,12,45,26,17,89]
#     if data < 20 and data > 70:
#         return (data)


# def minmax(data):
    
#     smallest = data[0]
#     largest = data[0]
    
#     for num in data[1:]:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
    
#     return (smallest, largest)
# data = [23, 34, 12, 45, 26, 17, 89]
# result = minmax(data)
# print(result)  # Output: (12, 89)


# class person:
#     def __init__(self):
#         print(self)
#     def display(self):
#         print('Hello')
# p1 =person()
# p1.display()


# class person:
#     def display(self):
#         n = 0
#         list1 = []
#         while n == 0:
#             list2 = [11,22,334,124,512,61]
#             list2[2] = 89
#             list1.append(list2)
#             n += 1
#             print(sorted(list2[:5:2]))
#             print(list2[::-1])
#             print(list1)
#             print(n)
#             print((n + 1)*list2)
#         screen = print
#         print('Hello')
# p1 = person()
# p1.display()



# l = []
# while True:
#     n = input('Enter your number (or press Enter to stop) = ')
#     if n == '0':  # Stop if input is empty
#         break
#     l.append(n)
# print(l)


# l = []
# while True:
#     number = input('Enter your number = ')
#     if number == '0':
#         break
#     l.append(int(number))
# l.sort(reverse=True)
# print(l)


# l = [34,23,45,67,12,23,45,56,67,78,34]
# l.sort(reverse=False)
# print(list(l))

# l = []
# while True:
#     number = input('Enter your number = ')
#     if number == '0':
#         break
#     l.append(int(number))
# l.sort()
# print(l)

# class List1:
#     def __init__(self):
#         self.l = []

#     def display(self):
#         while True:
#             number = input('Enter the list of numbers = ')
#             if number == '0':
#                 break
#             self.l.append(int(number))
#         self.l.sort()
#         print(set(self.l))
#         print(set(self.l[0:5]))
# l1 = List1()
# l1.display()

# l = open('test.txt','w')
# l.write('Hi I am Anirudh')
# l.close()
# print(l)


# class Level:
#     def __init__(self):
#         self.list1 = []


    
#     def display(self):
#         print('_________Enter you number in List_______'.center(30).upper())
#         print()
#         while True:
#             self.number = input('Enter your number = ')
#             if self.number == '0':
#                 break
#             self.list1.append(int(self.number))
        
#         if self.list1:
#             self.largest = self.list1[0]
#             self.smallest = self.list1[0]

#         for num in self.list1:
#             if num > self.largest:
#                 self.largest = num
#             if num < self.smallest:
#                 self.smallest = num
#         print(f"Largest number: {self.largest}")
#         print(f"Smallest number: {self.smallest}")
            
# l = Level()
# l.display()

# def sum_of_even_squares(n):
#     return sum(i**2 for i in range(2, n, 2))

# # Example usage
# n = int(input("Enter a positive integer: "))
# print(f"The sum of the squares of all even positive integers smaller than {n} is: {sum_of_even_squares(n)}")


# temperature = float(input("Enter in celsius = "))
# fahrenheit = (temperature * 1.8) + 32
# print(f'Temperature in fahrenheit = {fahrenheit:3f}')


# from math import pi
# radius_of_circle = float(input('Enter the radius = '))
# area = (pi * radius_of_circle) * radius_of_circle
# circum = (2 * pi) * radius_of_circle
# print('Area of the circle is = {0:2f} and Circumference of the circle is = {1:3f}'.format(area,circum))



# phone_number = input('Enter your phone number = ')
# print(phone_number[7:])
# print()


# from math import gcd
# n1 = int(input('Enter your number = '))
# n2 = int(input('Enter your another number = '))
# result = gcd(n1,n2)
# print(f'The GCD of {n1} and {n2} is {result}')

# from random import randrange
# n1 = int(input('Enter your number = '))
# n2 = int(input('Enter your another number = '))
# random_number = randrange(n1,n2)
# print(f'The random number between {n1} and {n2} is {random_number}')

# list1 = [ 1112,2,3,44]
# print(min(list1))
# print(max(list1))

# string = 'Hello World'
# slice1 = string[1:-1]
# print('d'+slice1+'h')

# string = 'Anirudh'
# s = reversed(string)
# print(list(s),'\n')

# string = 'anirudh'
# print('dh'+string[0:-4]+'dh')