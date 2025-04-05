# n = 0
# while n <= 10:
#     num = int(input('Enter your number = '))
#     n += num
# print(n)


# number = int(input('Enter your number = '))
# sum_digit = 0

# while number > 0:
#     digit = number % 10
#     sum_digit += digit
#     number //= 10

# print(sum_digit)


# l = [1,5,9,2,3,9,4,3,2,4,2,1,2] #create a list
# n = 2 # declare a variable of 2 in n for the removing of the duplicate number

# # Define a while loop for executing the list
# while n in l:
#     l.remove(n)
# print(l)

# fruits = {'apple': 210,
#           'banana':90,
#           'grapes':100}

# done = False
# while not done:
#     fruit = input('Enter your fruits name = ')
#     price = int(input('Enter the price of input fruit =  '))
#     fruits[fruit] = price
#     stop_continue = 'n'.lower()
#     if input('Want to more (y/n) = ')  == stop_continue:
#         done = True
# print(fruits)

# data = [3,5,9,8]
# for item in enumerate(data):
#     print(sorted(item))

# data = [3,5,9,8]
# for item in data:
#     print(item)

# data = [3,5,9,8]
# i = 0
# while i < len(data):
#     print(data[i])
#     i += 1

# string = 'Hello World !'
# message = ''
# for ch in string:
#     message += chr(ord(ch) + 1)
# print(message)

# message = 'Ifmmp!Xpsme!"'
# dmessage = ''
# for ch in message:
#     dmessage += chr(ord(ch) - 1)
# print(dmessage)


# matrix = [[1,4,8,3],
#           [2,5,6,3],
#           [1,9,5,8]]
# row = 3
# column = 4 
# for i in range(row):
#     for j in range(column):
#         print(matrix[i][j],end= ' ')
#     print()

# matrix = [[1,4,8,3],
#           [2,5,6,3],
#           [1,9,5,8]]
# row = int(input('Enter your row = '))
# column = int(input('Enter your column ='))
# for i in range(row):
#     for j in range(column):
#         print(matrix[i][j],end= ' ')
#     print()

# n = 0
# while n <= 6:
#     print(n)
#     n += 1


# vowels = 'aeiou'
# consonents = 'bcdfghjklmnpqrstvwxyz'
# digit = '123456789'
# count = 0
# while count < len(vowels):
#     print(count)
#     count += 1


# vowels = 'aeiou'
# consonents = 'bcdfghjklmnpqrstvwxyz'
# digit = '123456789'


# string  = 'Hello I am anirudh bhattacharya,my age is 45'

# vowels_count = 0
# consonents_count = 0
# digit_count = 0

# for ch in string.lower():
#     if ch in vowels:
#         vowels_count += 1
#     elif ch in consonents:
#         consonents_count += 1
#     elif ch in digit:
#         digit_count += 1
# print(f"Vowels count: {vowels_count}")
# print(f"Consonents count: {consonents_count}")
# print(f"Digit count: {digit_count}")


# list1 = [1,2,3,4,5,6]
# for number in list1:
#     print(f'Calculate the product of all the number in the list = {number*number}')


# list1 = [1, 2, 3, 4, 5, 6]
# product = 1  # Start with 1 because multiplying by 0 will always result in 0

# for number in list1:
#     product *= number  # Multiply the current number to the product

# print(f'The product of all numbers in the list is: {product}')


# string = 'Hello World !!!   '
# dic = {}

# for ch in string:
#     if ch in dic:
#         dic[ch] += 1
#     else:
#         dic[ch] =1

# print(dic)


# string = 'Humpty Dumpty sat on a wall Humpty Dumpty had a great fall'
# dic = {}
# words = string.split()

# for word in words:
#     if word in dic:
#         dic[word] +=1
#     else:
#         dic[word] = 1
# print(dic)


# #Given a string
# string = 'I am anirudh bhattacharya'
# vowels = 'aeiou' #Declare a vowels
# dic = {}

# for frequency in string.lower():
#     if frequency in vowels:
#         if frequency in dic:
#             dic[frequency] += 1
#         else:
#             dic[frequency] = 1
# print(dic)


# n1 = int(input('Enter you first number = '))
# n2 = int(input('Enter your second number = '))

# result = 0
# while n2 > 0:
#     if n2 % 2 == 1:
#         result += n1

#     n1 = n1 * 2
#     n2 = n2 // 2
# print(result)




# s = '''A group of fearless rebels emerged, unafraid to be labelled as crazy or mad.
# others called them mad troublemakers, but their insane ideas held the power to change
# the world. These visionaries proved that it is often the seemingly insane ones who
# hold the key to progress.'''
# L = ['crazy','mad','rebels','lunatic','troublemakers','insane']


# for word in L: # for is use to looping the list 
#     if word in s:
#        s =  s.replace(word,'*' * len(word))
# print(s)
# print(str.__doc__)




# total = 0
# while total <= 10:
#     number = int(input('Enter your number = '))
#     total += number
# print(total)



# s = '''A group of fearless rebels emerged, unafraid to be labelled as crazy or mad.
# others called them mad troublemakers, but their insane ideas held the power to change
# the world. These visionaries proved that it is often the seemingly insane ones who
# hold the key to progress.'''
# L = ['crazy','mad','rebels','lunatic','troublemakers','insane']

# for word in L:
#     if word in s:
#         s = s.replace(word[1:],'*' * len(word))
# print(s)
# print(str.__doc__)



# string = 'Hello world !!!   '
# dic = {}

# for char in string:
#     if char in dic:
#         dic[char] += 1
#     else:
#         dic[char] = 1
# print(dic)


# string = 'Hello world !!!   '
# dic = {}

# words = string.split()

# for word in words:
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1

# print(dic)


# age = int(input('Enter your age = '))

# for i in range(10,100):
#     print(f'{i} = {age}')
# print()

# age = input('Enter your age = ')
# for i in range(10,100):
#     if str(i) in age:
#         print(f"The digit {i} is found in age, its Unicode value is {ord(str(i)[0])}")
# print(age)



# age = int(input('Enter your age in non numeric = '))

# if 10 <= age <= 100:
#     for i in range(10,100):
#         print(f'{i}  =  {age}')

# else:
#     print('Do Something')
# print(age)


# names = {'_num','var','product','_add','_sub','square'}
# underscore_names = {}

# for name in names:
#     if name.startswith('_'):
#         underscore_names[name] = name
# print(underscore_names)
     

# names = {'_num','var','product','_add','_sub','square'}
# underscore_names = set()

# for name in names:
#     if name.startswith('_'):
#         underscore_names.add(name)
# print(underscore_names)


# D = {'apple': 100,
#      'grapes': 55,
#      'banana': 200,
#      'guava' : 60}

# for fruit,price in D.items():
#     if price < 100:
#         D[fruit] += 10
#     elif price >= 100:
#         D[fruit] -= 10
# print(D)

# L = [['John',[88,89,78]],
#      ['Sam', [89,76,99]],
#      ['Dev', [85,67,89]]]

# for name,grades in L:
#     total = sum(grades)
#     print(name,total)


# D = {}
# for number in range(1,6):
#     if number in D:
#         D[number] = number
#     else:
#         D[number] = number * number
# print(D)

# d = {}
# for number in range(1,6):
#     d[number] = number * number
# print(d)

# L1 = ['China','Brazil','India','Iran','Russia']
# L2 = ['Italy','Japan','China','Russia','Nepal','France']

# L3 = []

# for common in L1:
#     if common in L2:
#         L3.append(common)
# print(L3)


# D = {'pen':10,
#      'pencil':5,
#      'eraser':8,
#      'marker':15,
#      'ruler':19}

# for chart in D:
#     print(f'{chart:8}',end=' ')
#     for i in range(D[chart]):
#         print('-',end=' ')
#     print()


# from random import randint

# L = []
# for number in range(0,10):
#     L.append(randint(1,50))
# print(L)




# Dir = ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
#        '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', 
#        '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#          '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
#          '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
#          'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
#            'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
#            'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
#            'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
#            'swapcase', 'title', 'translate', 'upper', 'zfill'] 

# is_list = set()

# for string in Dir:
#     if string.startswith('is'):
#         is_list.add(string)
# print(is_list)


# Dir = ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
#        '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', 
#        '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#          '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
#          '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
#          'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
#            'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
#            'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
#            'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
#            'swapcase', 'title', 'translate', 'upper', 'zfill'] 

# is_list = set()

# for string in Dir:
#     if string.startswith('__'):
#         is_list.add(string)
# print(is_list)


# row = 4
# for i in range(1, row + 1):
#     print('*' * i)

# row = 4
# for i in range(1,row+1):
#     print(str(i) * i)

# row = 5
# for i in range(1,row+1):
#     print(chr(64 + i)* i)

# row = 4
# for i in range(1, row + 1):
#     print(' ' * (row - i) + '*' * i)

# row = 4
# for i in range(1, row+1):
#     print(' ' * (row - i) + '*' * (2 * i - 1))


# row = 4

# for i in range(1,row + 1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# row = 4

# for i in range(1,row + 1):
#     for j in range(1,i + 1):
#         print(i, end=' ')
#     print()


# row = 4

# for i in range(1,row + 1):
#     for j in range(10,10 + i):
#         print(j, end=' ')
#     print()


# start = 10
# row = 4

# for i in range(1, row + 1):
#     for j in range(start, start + i):
#         print(j, end=' ')
#     start += i  
#     print()  


# for i in range(1,5):
#     for j in range(1,i + 1):
#         print(chr(64 + i),end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,i + 1):
#         print(chr(64 + j),end=' ')
#     print()



# start_char = 65  

# for i in range(1, 5):
#     for j in range(i):
#         print(chr(start_char), end=' ')  
#         start_char += 1  
#     print()  

# people = [('John', 25), ('Alice', 30), ('Bob', 20)]
# sorted_people = sorted(people, key=lambda person: person[1])

# print(sorted_people)  # Output: [('Bob', 20), ('John', 25), ('Alice', 30)]


# list1 = [1,2,3,4,5,6,7,8]
# list2 = list(reversed(list1))
# print(list2)


# list1 = [1,2,3,4,5,6,7,8]
# list1.sort(reverse=True)
# print(list1)

# class rev():
#     def __init__(self):
#         self.list1 = [1,2,3,4,5,6,7,8]
        
    
#     def display(self):
#         self.list1.sort(reverse=True)
#         return self.list1

# r1 = rev()
# print(r1.display())


# class rev():
#     def __init__(self):
#         self.list1 = set()


#     def display(self):
#         for self.number in range(1,10):
#             self.list1.add(self.number)
#             print(self.number,end=' ')
#         return self.list1
        
# add_list = rev()
# add_list.display()


# class rev():
#     def __init__(self):
#         self.list1 = {}


#     def display(self):
#         for number in range(1,10):
#             self.list1[number] = number * number
#         return self.list1
        
# add_list = rev()
# result = add_list.display()
# print(result)


# from random import randint
# class rev():
#     def __init__(self):
#         self.list1 = {}
    
#     def display(self):
#         try:
#             for random_number in range(1,10):
#                 random_number = randint(1,50)
#                 if random_number % 2 == 0:
#                     self.list1[random_number] = random_number
#             return self.list1
#         except Exception as error:
#             print(f'Error = {error}')
#             raise ValueError('Invalid')
# add_list = rev()
# result = add_list.display()
# print(result)


# from random import randint
# class rev():
#     def __init__(self):
#         self.list1 = {}
    
#     def display(self):
#         try:
#             for key_number in range(1,10):
#                 if key_number in self.list1:
#                     self.list1[key_number] += key_number
#                 else:
#                     self.list1[key_number] = key_number
#             for random_number in range(1,key_number):
#                 random_number = randint(1,50)
#                 if random_number % 2 == 0:
#                     if random_number in self.list1.values():
#                         self.list1[random_number] += random_number
#                     else:
#                         self.list1[random_number] = random_number
#             return self.list1
#         except Exception as error:
#             print(f'Error = {error}')
#             raise ValueError('Invalid')
# add_list = rev()
# result = add_list.display()
# print(result)




# from random import randint
# from copy import deepcopy
# class rev():
#     def __init__(self):
#         self.list1 = {}
    
#     def display(self):
#         try:
#             for key_number in range(1,10):
#                 self.list1[key_number] = self.list1.get(key_number,0) + key_number

#             for _ in range(1,10):
#                 random_number = randint(1,50)
#                 if random_number % 2 == 0:
#                     self.list1[random_number] = self.list1.get(random_number, 0) + random_number
#             return deepcopy(self.list1)
#         except Exception as error:
#             print(f'Error = {error}')
#             raise ValueError('Invalid')
# add_list = rev()
# result = add_list.display()
# print(result)


# list1 = []
# for number in range(1,5):
#     number = int(input('Enter your number = '))
#     list1.append(number)
# print(list1)

# list1 = []
# for string in range(1,5):
#     string = input('Enter your first name = ')
#     list1.append(string)
# print(list1)

# list1 = set()
# for string in range(1,5):
#     string = input('Enter your first name = ')
#     list1.add(string)
# print(list1)

# list1 = {}
# for string in range(1,5):
#     string = input('Enter your first name = ')
#     if string in list1:
#         list1[string] += 1
#     else:
#         list1[string] = 1
# print(list1)

# n = []
# while len(n) < 5:
#     number = int(input('Enter your number = '))
#     n.append(number) 
# odd_number = [num for num in n if num % 2 == 1]  
# print(f'Odd number is = {odd_number}')


# n = []
# for _ in range(4):
#     number = int(input('Enter your number = '))
#     n.append(number)
# print(n)


# n = []
# while len(n) < 5:
#     number = int(input('Enter your number = '))
#     n.append(number) 
# n = [num for num in n if num % 2 == 0]  
# print(f'Even number is = {n}')


# class largest_element():
#     def __init__(self):
#         self.list1 = [12,1,34,56,23,14,89,56,78,90]

#     def display(self):
#         largest_number = max(self.list1)
#         return largest_number
# p1 = largest_element()
# result = p1.display()
# print(f'Largest number in the list is = {result}') 


# class largest_element():
#     def __init__(self):
#         self.list1 = [12,1,34,56,23,14,90,56,78,89]

#     def display(self):
#         sorted_number = sorted(self.list1)
#         largest_number = sorted_number[-1]
#         return largest_number
# p1 = largest_element()
# result = p1.display()
# print(f'Largest number in the list is = {result}') 


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage:
# arr = [12, 1, 34, 56, 23, 14, 90, 56, 78, 89]
# sorted_arr = quick_sort(arr)
# print("Sorted list:", sorted_arr)


# def merge_sort(arr):
#     # Base case: If the list has 1 or 0 elements, it's already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Split the list in half
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
    
#     # Merge the sorted halves
#     return merge(left, right)

# def merge(left, right):
#     sorted_arr = []
#     while left and right:
#         if left[0] < right[0]:
#             sorted_arr.append(left.pop(0))
#         else:
#             sorted_arr.append(right.pop(0))
    
#     # If one half has leftovers, append them
#     sorted_arr.extend(left)
#     sorted_arr.extend(right)
    
#     return sorted_arr

# # Example usage:
# arr = [12, 1, 34, 56, 23, 14, 90, 56, 78, 89]
# sorted_arr = merge_sort(arr)
# print("Sorted list:", sorted_arr)



# class Timer:
#     def __enter__(self):
#         self.start = time.time()  # Start timing
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = time.time()  # End timing
#         self.duration = self.end - self.start
#         print(f"Operation took {self.duration:.4f} seconds")

# # Using the custom context manager
# import time
# with Timer() as t:
#     # Simulate a time-consuming operation
#     time.sleep(2)
#     print(type(time))


# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)  # Adds an item to the end of the list

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()  # Removes and returns the last item from the list
#         else:
#             return "Stack is empty"

#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]  # Returns the last item without removing it
#         else:
#             return "Stack is empty"

#     def is_empty(self):
#         return len(self.stack) == 0  # Returns True if the stack is empty

#     def size(self):
#         return len(self.stack)  # Returns the number of items in the stack

# # Example usage
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)

# print(s.pop())  # Output: 30
# print(s.peek())  # Output: 20
# print(s.is_empty())  # Output: False
# print(s.size())  # Output: 2


# # First type of code for intersection
# L1 = [1,3,5,7,9,2,4]
# L2 = [1,4,6,9,10]

# L3 = set(L1).intersection(set(L2))
# print(L3)


# # Second type of code for intersection
# L1 = [1,3,5,7,9,2,4]
# L2 = [1,4,6,9,10]

# L3 = set(L1) & set(L2)
# print(L3)


# #Third type of code for intersection
# class intersect():
#     def __init__(self):
#         self.L1 = [1,3,5,7,9,2,4]
#         self.L2 = [1,4,6,9,10]

#     def display(self):
#         L3 = []
#         for number in self.L1:
#             if number in self.L2:
#                 L3.append(number)
#         return set(L3) 
# ret = intersect() 
# result = ret.display()
# print(result)

# #Wrong Code
# #Fourth type of code for intersection
# class intersect():
#     def __init__(self):
#         self.L1 = [1,3,5,7,9,2,4]
#         self.L2 = [1,4,6,9,10]

#     def display(self):
#         for number in self.L1:
#             if number in self.L2:
#                 number = set(L1) & set(L2)
#         return set(number) 
# ret = intersect() 
# result = ret.display()
# print(result)


# #Fifth type of code for intersection
# class intersect():
#     def __init__(self):
#         self.L1 = [1,3,5,7,9,2,4]
#         self.L2 = [1,4,6,9,10]

#     def display(self):
#         L3 = set()
#         for number in self.L1:
#             if number in self.L2:
#                 L3.add(number)
#         return set(L3)
# ret = intersect() 
# result = ret.display()
# print(result)
