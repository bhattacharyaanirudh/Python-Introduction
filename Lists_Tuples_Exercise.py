# #Class type List
# list1 = [1,2,3,4,5,6,7,8,9]
# print(type(list1))
# print(id(list1))

# #Class type tuple
# list1 = (1,2,3,4,5,6,7,8,9)
# print(type(list1))
# print(id(list1))


# #unpacking tuple
# x = 1
# y = 2
# z = 3

# a,b,c = x,y,z
# print(a,b,c)
# print(id(a))
# print(id(b))
# print(id(c))

# x = 1
# y = 2
# z = 3

# a,b,c = x,y,z
# print(a,b,c)
# print(chr(a)*2)
# print(chr(b)*3)
# print(chr(c)*4)


# list1 = [1,2,3,4,5]
# list1[3] = 200
# print(list1)

# list1 = [1,2,3,4,5,6]
# list1[2:len(list1)] = [30,40,50,60,70,80]
# print(list1)

# n = [1,2,3]
# n.extend('pqr')
# print(n)

# number = [1,2,3,4,5,6,7,8]
# number2 = [10,20,30,40,50]
# number.insert(5,50)
# number.insert(5,40)
# number.insert(5,30)
# number.insert(5,20)
# number.insert(5,10)
# print(number)

# number = [1,2,3,4,5,6,7,8]
# number2 = [10,20,30,40,50]
# number[5:5] = number2
# print(number)

# list1 = [1,2,3,4,5,6,7,8]
# del list1[2:6]
# print(list1)

# list = [1,2,3,4,5,6]
# list1 = list.copy()
# print(list1)

# rev = [1,2,3,4,5,6]
# rev.reverse()
# print(rev)

# numbers = [1,2,3,4,5,6]
# rev = numbers[::-1]
# print(numbers)
# print(rev)

# numbers = [1,2,3,4,5,6]
# print(numbers[::-1])

# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.append(100)
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.append(100)
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.insert(0,200)
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# num = [200] + numbers
# print(num)

# numbers = [1,2,3,4,5,6,7,8,9]
# num = numbers + [200]
# print(num)

# numbers = [1,2,3,4,5,6,7,8]
# numbers[3] = 150
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8]
# numbers.insert(3,150)
# print(numbers)

# list = [1,2,3,4,5]
# print(list + [11,12,13,14,15])


# list1 = [1,2,3,4,5,6,7]
# del list1[4]
# print(list1)

# list1 = [1,2,3,4,5,6,7]
# list1.remove(5)
# print(list1)

# list = [1,2,3,4,5,6,7]
# x = list.pop(5)
# print(x)

# list = [1,2,3,4,5,6,7]
# list.pop(0)
# print(list)

# list = [1,2,3,4,5,6,7]
# list.remove(1)
# print(list)

# list = [1,2,3,4,5,6,7]
# del list[0]
# print(list)

# list = [1,2,3,4,5,6,7]
# list.clear()
# print(list)

# list = [1,2,3,4,5,6,7]
# del list[5]
# print(list)


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# del numbers[-3:]
# print(numbers)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# print(55 in numbers)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# num = numbers.index(55)
# print(num)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# num = numbers.index(55,9,len(numbers))
# print(num)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# num = numbers.index(55,4,9)
# print(num)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# num = numbers.index(1,0,len(numbers))
# print(num)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# num = numbers.index(min(numbers))
# print(num)

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# numbers[numbers.index(max(numbers))] = 1000

# print(numbers)


# # My Second Largest Number of code
# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# first_largest_number = max(numbers)
# numbers.remove(max(numbers))
# largest_number = max(numbers)
# print(f'Second largest number is = {largest_number}')
# print()

# # My Third Smallest Number of Code
# numbers.remove(min(numbers))
# del numbers[4]
# smallest_number = min(numbers)
# print(f'Third Smallest Number is = {smallest_number}')



# # My Second Largest Number of code
# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# first_largest_number = max(numbers)
# numbers.remove(first_largest_number)
# largest_number = max(numbers)
# print(f'Second largest number is = {largest_number}')
# print()

# # My Third Smallest Number of Code
# numbers.sort()
# smallest_number = numbers[2]
# print(f'Third Smallest Number is = {smallest_number}')


# # My Second Largest Number of code
# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
# number_cpy = numbers.copy()
# number_cpy.remove(max(number_cpy))
# num = sorted(number_cpy)
# largest_number = num[-1]
# print(f'Second largest number is = {largest_number}')
# print()

# # My Third Smallest Number of Code
# number_cpy.sort()
# smallest_number = number_cpy[2]
# print(f'Third Smallest Number is = {smallest_number}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# num = sorted(numbers_cpy) # sorted of the numbers
# largest_three_numbers = num[-3:]  # Largest three numbers
# print(f'largest three numbers of the list is = {largest_three_numbers}')


# import heapq

# numbers = [12, 32, 55, 67, 3, 55, 68, 22, 55, 89, 55, 1, 19, 32]

# # Ensure there are at least three numbers
# if len(numbers) >= 3:
#     largest_three_numbers = heapq.nlargest(3, numbers)
#     print(f'Largest three numbers: {largest_three_numbers}')
# else:
#     print("The list does not have enough numbers.")


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# num = sorted(numbers_cpy)
# print(f'The smallest five numbers are = {num[:5]}')


# import heapq

# numbers = [12, 32, 55, 67, 3, 55, 68, 22, 55, 89, 55, 1, 19, 32]
# smallest_five_numbers = heapq.nsmallest(5, numbers)
# print(f'The smallest five numbers are = {smallest_five_numbers}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# num = sorted(numbers_cpy)
# sum_of_numbers = sum(num[:5])
# print(f'The sum of smallest five numbers are = {sum_of_numbers}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# total = sum(numbers_cpy[:7])
# print(f'The Minimum value of the first half of the list are = {total}')

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# min_value = min(numbers_cpy[:5]) # minimum value from the first half of the list
# print(f'The Minimum value of the first half of the list are = {min_value}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# print(numbers_cpy)
# first_half = numbers_cpy[:len(numbers_cpy)//2]
# print(first_half)
# min_value = min(first_half)
# print(f'The Minimum value of the first half of the list is = {min_value}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers_cpy = numbers.copy() # copy of the list of numbers
# average = sum(numbers_cpy)/len(numbers_cpy)
# print(f'Average of all the element of all the list is = {average}')


# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers.sort()
# new_list = numbers.copy()[-5:]
# print(f'Five largest number of the list in new list are = {new_list}')

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers.sort()
# new_list = numbers.copy()[:5]
# print(f'Five smallest number of the list in new list are = {new_list}')

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers.sort(reverse=True)
# new_list = numbers.copy()[-5:]
# print(f'Five smallest number of the list in new list are = {new_list}')

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# numbers.sort(reverse=True)
# print(f'Sort the list in descending order is = {numbers}')

# numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32] # make a lists
# print(numbers)
# new_list = sorted(numbers)
# print(f'the new list all the elements are containing in the ascending order are = {new_list}')

# fruits = ['banana',
#           'flg',
#           'Mango',
#           'pomegranate',
#           'Apple']
# fruits.sort(key = len) 
# print(f'Sorted list of the string based on their length = {fruits}')


# fruits = ['banana',
#           'flg',
#           'Mango',
#           'pomegranate',
#           'Apple']
# fruits.sort(key = str.upper) 
# print(f'Sorted list of the string based on their case sensitive = {fruits}')


# list1 = [None]
# print(f'All the 20 elements are initialized by the none in this list = {list1 * 20}')

# list1 = list(range(1000,0,-100))
# print(f'Create a list using by range = {list1}')

# listD = ['Pluto',
#         'Goofy',
#         'Donald Duck',
#         'Alice']
# print(listD)
# new_list = ','.join(listD)
# print(f'All this strings are joined by comma = {new_list}')


# fruits = ['apple',
#          'banana',
#          'grapes',
#          'guava']
# index1 = list(reversed(fruits))
# print(f'Reversing of the string present at reverse of index 2 is = {index1[2]}')


# fruits = ['apple',
#          'banana',
#          'grapes',
#          'guava']
# index1 = fruits[2][::-1]
# print(f'Reversing of the string present at reverse of index 2 is = {index1}')

# students = ('John',25,[89,90,92])
# students[2].extend([89,90])
# print(students)

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# result = l1 + l2
# print(result)
# l1.extend(l2)
# print(l1)

# list1 = [1,2,3,4,5,6,7,8]
# del list1[4]
# print(list1)

# list1 = [1,2,3,4,5,6,7,8]
# del list1[:]
# print(list1)

# list1 = [1,2,3,4,5,6,7,8]
# list1.clear()
# print(list1)

# list1 = [1,2,3,4,5,6,7,8]
# list1.pop(4)
# print(list1)

# list1 = [1,2,3,4,5,6,7,8]
# list1.remove(5)
# print(list1)

# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# list1[:1] , list1[-1:] = list1[-1:], list1[:1]
# print(list1)


# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# list1[0] , list1[-1] = list1[-1], list1[0]
# print(list1)


# colors_list = []
# colors = input('Enter your color = ').split()
# colors_list.append(colors)
# print(colors)
# sep_colors = '-'.join(colors)
# print(sep_colors)