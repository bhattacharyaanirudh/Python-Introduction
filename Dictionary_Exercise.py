# dic = {'Apple':250,
#        'Banana':100,
#        'Grapes':90,
#        'Guava':140}
# print(dic)

# dic = {'Apple':250,
#        'Banana':100,
#        'Grapes':90,
#        'Guava':140}
# print(id(dic))

# dic = {'Apple':250,
#        'Banana':100,
#        'Grapes':90,
#        'Guava':140}
# print(type(dic))

# dic = {'Apple':250,
#        'Banana':100,
#        'Grapes':90,
#        'Guava':140}
# print(dic)
# print(dic.keys())
# print(dic.items())
# print(dic.values())


# dic = {'Apple':250,
#        'Banana':100,
#        'Grapes':90,
#        'Guava':140}
# print(dic)
# print()
# print(dic.keys())
# print()
# print(dic.items())
# print()
# print(dic.values())
# print()

# dic['Apple'] = 300
# print(dic.values())

# dic['Apple'] = 'Fly'
# print(dic.keys())
# print(dic.values())

# currency = {}
# print(currency)
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Australia'] = 'Euro'
# currency['Bangladesh'] = 'Takka'
# print(currency)


# students = {}
# students['Anirudh'] = 49
# students['Abhishek'] = 32
# students['Arobinda'] = 23
# students['Ranjana'] = 1

# print(students)


# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'

# print(currency)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# del currency['UK']
# print(currency)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# del_currency = currency.pop('UK')
# print(del_currency)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# del currency['UK']
# print(currency)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# C = currency.pop('Japan')
# print(C)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# currency['Switzerland'] = 'Swiss Franc'
# print(currency)


# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# currency['India'] = 'Indian Rupee'
# print(currency)



# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# currency['India'] = 'Indian Rupee'
# print(currency)

# c = currency.popitem()
# print(c)

# currency = {}
# currency['India'] = 'Rupee'
# currency['UK'] = 'Pound'
# currency['Japan'] = 'Yen'
# currency['Austria'] = 'Euro'
# currency['Bangladesh'] = 'Taka'
# print(currency)

# print(f'Get the keys of currency = {currency.keys()}')
# print()
# print(f'Get the Values of currency = {currency.values()}')
# print()
# print(f'Get the keys-Values pair of currency = {currency.items()}')


# fruits = {'apple':100,
#           'banana':75,
#           'mango':80}

# fruits['apple'] = 0
# fruits['grapes'] = 0
# print(fruits.items())


# fruits = {'apple':100,
#           'banana':75,
#           'mango':80}

# fruits['apple'] = 0
# fruits.setdefault('apple',0)
# fruits.setdefault('grapes',0)
# print(fruits.items())

# names = ['John','Sam','Marie','Anne']
# login = dict.fromkeys(names,None)
# print(login)

# designation = ['Programer','Manager','accountant']
# salary = [4000,5000,3000]
# result = dict(zip(designation,salary))
# print(result)

# import pandas as pd

# designation = ['Programmer', 'Manager', 'Accountant']
# salary = [4000, 5000, 3000]

# # Create a dictionary using pandas DataFrame
# df = pd.DataFrame(list(zip(designation, salary)), columns=['Designation', 'Salary'])
# exp = dict(zip(df['Designation'], df['Salary']))

# print(exp)



# python_books = ['Learn Python','Programming in Python','Python for Beginners']
# cplusplus_books = ['C++ in depth','C++ programming']
# java_books = ['Java Programming','Learn Java']

# books = {}  #Declare a empty dictionary

# #define all the books dictionary variable with books keys
# books['python'] = python_books
# books['C++'] = cplusplus_books
# books['java'] = java_books

# # Declare a new list variables for define the Dictionary values
# print(books['python'])
# print()

# print(books['C++'])
# print()

# print(books['java'])
# print()

# #Declare a 2 Dictionary with items
# book_prices = {'Learn ABC': 150,
#                'Learn 123' : 200,
#                'Rhymes': 300,
#                'Cursive Writing': 250}
# print(book_prices)
# new_stock = {'Stories':350,
#              'Poems':290,
#              'Spellings':200}
# print(new_stock)

# #Add my new_stock Dictionary into the book_prices
# book_prices.update(new_stock)
# print(dict(book_prices))


# print(dict.fromkeys(range(1000,10000,1000)))


# student = {'name':{'first':'John',
#                    'last':'Mark'},
#             'marks': 98,
#             'age':20}
# last_name = student['name']['last']
# print(f'The last name of student is = {last_name}')

# d = {2:300,8:900,7:800,1:100}
# print(sorted(dict(d)))

# d = {2:300,8:900,7:800,1:100}
# sort_value = sorted(d.items())
# print(dict(sort_value))


# marks = {2234:[99,23,56],
#          2135:[67,56,68],
#          2199:[78,89,66]}

# total = sum(marks[2135])
# print(f'Total marks of the student with student id 2135 = {total}')



# t1 = [(1,(0,0,0,0,0,4)),
#       (2,(0,0,0,8,0,0)),
#       (3,(0,0,0,0,0,0)),
#       (4,(0,0,0,0,6,0)),
#       (5,(0,0,0,0,0,0)),
#       (6,(0,0,3,0,0,0))]
# matrix = dict(t1)
# print(matrix)


# list1 = {}
# s1 = input('Enter your first string = ')
# s2 = input('Enter your second string = ')
# list1[s1] = s2

# s1 = input('Enter your first string = ')
# s2 = input('Enter your second string = ')
# list1[s1] = s2

# s1 = input('Enter your first string = ')
# s2 = input('Enter your second string = ')
# list1[s1] = s2

# s1 = input('Enter your first string = ')
# s2 = input('Enter your second string = ')
# list1[s1] = s2


# print(dict(list1))



# s1 = input('Enter your first string = ')
# s2 = input('Enter your second string = ')

# common_char = list(set(s1) & set(s2))
# print(common_char)


# string1 = 'Life has no remote, get up and change it yourself'
# string2 = 'Life has no ctrl+z'

# common_char = set(string1.split(' ')) & set(string2.split(' '))
# print(common_char)


# string1 = 'Life has no remote, get up and change it yourself'
# string2 = 'Life has no ctrl+z'


# common_char = len(set(string1.split(' '))) - len(set(string2.split(' ')))

# print(common_char)


# L = [12,44,46,32,12,43,55,86,43]
# new_list = set(L)
# filter(L,new_list)
# print(new_list)

# L = [12,44,46,32,12,43,55,86,43]
# list_cpy = L.copy()

# new_list = set(list_cpy)
# print(sorted(new_list))

# l1 = [1,2,3,4]
# l2 = [2,3,1,4]
# print(set(l1) == set(l2))

# L1 = [1,2,3,7]
# L2 = [2,3,4,5]
# print(set(L1) - set(L2))


# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# remove_id = toppers.remove('id11')
# print(remove_id)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# new_id1 = champions.add('id46')
# new_id2 = champions.add('id20')
# print(champions)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# not_champions = toppers - champions
# print(not_champions)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# not_toppers = champions - toppers
# print(not_toppers)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# both_toppers_champions = champions & toppers
# print(both_toppers_champions)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# either_toppers_champions = champions | toppers
# print(either_toppers_champions)


# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}

# string = {'id19', 'id23', 'id45', 'id56', 'id11'}
# s1,s2,s3 = toppers,champions,string

# common_char = set(s1) & set(s2) & set(s3)
# print(common_char)

# toppers = {'id11','id23','id34','id45','id77','id12','id89','id56','id55','id19'}
# champions = {'id19','id23','id78','id99','id79','id13','id56','id45','id80'}
# print(toppers)
# print()
# print(champions)
# print()
# string = set(toppers) | set(champions)
# print(string)
# print()
# s1,s2,s3 = toppers,champions,string
# common_char = set(s1) & set(s2) & set(s3)
# print(sorted(common_char))