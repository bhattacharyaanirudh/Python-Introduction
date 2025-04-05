# string = "'Nurses run'  'Was it a rat I saw'"
# s = 'Nurses'
# string_case = s.lower()
# if string_case == string_case[::-1]:
#     print(f'{string_case} is a palindrome')
# else:
#     print(f'{string_case} is not a palindrome')
# print(string_case)

# days = {0:'Sunday',
#         1:'Monday',
#         2:'Tuesday',
#         3:'Wednesday',
#         4:'Thursday',
#         5:'Friday',
#         6:'Saturday'}

# choice = int(input('Enter your choice = '))
# if choice == 0:
#     key = days[choice]
#     print(key)

# elif choice == 1:
#     key = days[choice]
#     print(key)

# elif choice == 2:
#     key = days[choice]
#     print(key)

# elif choice == 3:
#     key = days[choice]
#     print(key)

# elif choice == 4:
#     key = days[choice]
#     print(key)

# elif choice == 5:
#     key = days[choice]
#     print(key)

# elif choice == 6:
#     key = days[choice]
#     print(key)

# else:
#     print('Invalid Input')



# days = {0:'Sunday',
#         1:'Monday',
#         2:'Tuesday',
#         3:'Wednesday',
#         4:'Thursday',
#         5:'Friday',
#         6:'Saturday'}

# choice = int(input('Enter your choice (0-6) = '))
# if 0 <= choice <= 6:
#     key = days[choice]
#     print(key)
# else:
#     print('Invalid input')

# print(True + 4)
# print(False - 3)


# D = {'a': 23, 'b': 34, 'c': 56}

# number = 23
# # Check if the number exists as a value in the dictionary
# if number in D.values():
#     # Find the key corresponding to the value
#     key = [k for k, v in D.items() if v == number][0]
#     print(key)
# else:
#     print('Do Something')

# L = [1,2,3,5,6,7,8,9]

# number = int(input('Enter your number = '))
# if number in L:
#     result = sum(L)/len(L)
#     print(f'I am using Ternary operator = {result}')
# else:
#     print('Invalid')


# L = [1,2,3,5,6,7,8,9]

# try:
#     number = int(input('Enter your number = '))
#     average = sum(L)/len(L) if number in L  else 'Invalid !!!!!!'
#     print(f'Code is created by Ternary Operator = {average}')

# except ValueError:
#     print('Invalid input! Please enter a valid integer.')


# bill_amount = int(input('Enter your bill amount = '))

# if bill_amount > 2000:
#     free_home_delivery = 'Available'
#     print(free_home_delivery)

# else:
#     free_home_delivery = 'Not Available'
#     print(free_home_delivery)


# bill_amount = int(input('Enter your bill amount = '))

# free_home_delivery = "Available" if bill_amount > 2000 else "Not Available"
# print(f'Your home Delivery is = {free_home_delivery}')


# marks = int(input('Enter Marks = '))

# if marks >= 70:
#     grade = 'A'

# else:
#     if marks >= 60:
#         grade = 'B'
#     elif marks >= 50:
#         grade = 'C'
#     else:
#         if marks >= 40:
#             grade = 'D'
#         else:
#             grade = 'E'
# print(grade)


# year = int(input('Enter your year = '))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     leap_year = 'Is a Leap Year'

# else:
#     leap_year = 'Not Leap Year'
# print(leap_year)


# year = int(input('Enter your year = '))
# if year % 400 == 0:
#     leap_year = f'{year} is a Leap Year'
# elif year % 4 == 0 and year % 100 != 0:
#     leap_year = f'{year} is a Leap Year'
# else:
#     leap_year = f'{year} is not a Leap Year'

# print(leap_year)



# weight = int(input('Enter your proper weight = '))
# height = float(input('Enter your proper height = '))

# height_in_meter = height/100
# bmi = weight/(height_in_meter**2)

# if bmi >= 30:
#     weight_result = 'Obese'
# elif 25 < bmi < 29.9:
#     weight_result = 'Overweight'
# elif 18.5 < bmi < 24.9:
#     weight_result = 'Normal weight'
# elif bmi < 18.5:
#     weight_result = 'Underweight'
# else:
#     weight_result = 'None of theses'

# print(weight_result)



# # Declare a weight and height in input
# weight_in_pound = int(input('Enter your proper weight = '))
# height_in_inch = float(input('Enter your proper height = '))

# #Calculate weight in pound and height in kg
# weight_in_kg = weight_in_pound * 0.4535924
# height_in_cm = height_in_inch * 2.54

# #Print out the weight in pound and and height in kg
# print()
# print('*'*37)
# print('WEIGHT and HEIGHT are mentioned below'.upper())
# print('*'*37)
# print(f'Your weight is = {weight_in_kg} kg')
# print(f'Your height is = {height_in_inch} cm')
# print()
# print('Execution of the result is calculate according to the condition'.upper())
# print('-'*64)
# #Code block or intendant of weight and height 
# if weight_in_kg >= 30:
#     weight_state = 'obese_weight'
#     weight_result = f'Calculated Your {weight_in_kg:.3f} kg weight and {height_in_cm:.2f} cm height are =  {weight_state.upper()}'
# elif 25 < weight_in_kg < 29.9:
#     weight_state = 'Over_Weight'
#     weight_result = f'Calculated Your {weight_in_kg:.3f} kg weight and {height_in_cm:.2f} cm height are =  {weight_state.upper()}'
# elif 18.5 < weight_in_kg < 24.9:
#     weight_state = 'Normal_Weight'
#     weight_result = f'Calculated Your {weight_in_kg:.3f} kg weight and {height_in_cm:.2f} cm height are =  {weight_state.upper()}'
# elif weight_in_kg < 18.5:
#     weight_state = 'Under_Weight'
#     weight_result = f'Calculated Your {weight_in_kg:.3f} kg weight and {height_in_cm:.2f} cm height are =  {weight_state.upper()}' 
# else:
#     weight_result = 'Do Proper Exercise'
# print(weight_result)
# print()

