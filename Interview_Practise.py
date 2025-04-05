# # Define a class
# class Car:
#     # Constructor (initializer method)
#     def __init__(self, brand, model, year):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute
#         self.year = year    # Attribute
    
#     # Method to display car details
#     def display_details(self):
#         return f"{self.year} {self.brand} {self.model}"
    
#     # Method to start the car
#     def start(self):
#         return f"The {self.model} is starting!"

# # Create objects (instances of the Car class)
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Tesla", "Model S", 2022)

# # Access attributes
# print(car1.brand)  # Output: Toyota
# print(car2.year)   # Output: 2022

# # Call methods
# print(car1.display_details())  # Output: 2020 Toyota Corolla
# print(car2.start())            # Output: The Model S is starting!


# # Parent Class
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         return f"{self.brand} {self.model} is starting."

#     def stop(self):
#         return f"{self.brand} {self.model} is stopping."

# # Child Class 1
# class Car(Vehicle):
#     def __init__(self, brand, model, doors):
#         super().__init__(brand, model)  # Call the parent class's constructor
#         self.doors = doors

#     def open_trunk(self):
#         return f"The trunk of the {self.brand} {self.model} is now open."

# # Child Class 2
# class Bike(Vehicle):
#     def __init__(self, brand, model, type_of_bike):
#         super().__init__(brand, model)  # Call the parent class's constructor
#         self.type_of_bike = type_of_bike

#     def kick_start(self):
#         return f"{self.brand} {self.model} is kick-started."

# # Creating objects
# car = Car("Toyota", "Camry", 4)
# bike = Bike("Harley-Davidson:", "Street 750:", "Cruiser:")

# # Using parent and child methods
# print()
# print(car.start(),'\n','*'*25)        # Output: Toyota Camry is starting.
# print(car.open_trunk().upper(),'\n','*'*41)   # Output: The trunk of the Toyota Camry is now open.
# print(bike.start(),'\n','*'*40)       # Output: Harley-Davidson Street 750 is starting.
# print(bike.kick_start(),'\n','*'*45)  # Output: Harley-Davidson Street 750 is kick-started.


# # Parent class
# class Animal:
#     def speak(self):
#         return "The animal makes a sound."

# # Child classes
# class Dog(Animal):
#     def speak(self):
#         return "The dog barks."

# class Cat(Animal):
#     def speak(self):
#         return "The cat meows."

# # Polymorphic behavior
# def make_animal_speak(animal):
#     print(animal.speak())

# # Using different types of objects
# dog = Dog()
# cat = Cat()

# make_animal_speak(dog)  # Output: The dog barks.
# make_animal_speak(cat)  # Output: The cat meows.


# from abc import ABC, abstractmethod

# # Abstract base class
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# # Concrete implementations
# class Dog(Animal):
#     def speak(self):
#         return "The dog barks."

# class Cat(Animal):
#     def speak(self):
#         return "The cat meows."

# # Polymorphism in action
# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())
# # Output:
# # The dog barks.
# # The cat meows.


# class Person:
#     species = "Homo sapiens"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def introduce(self):
#         return f"Hello, I am {self.name} and I am {self.age} years old."

#     # Class method
#     @classmethod
#     def set_species(cls, new_species):
#         cls.species = new_species

#     # Static method
#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# # Create an instance
# person = Person("Alice", 25)

# # Instance method
# print(person.introduce())  # Output: Hello, I am Alice and I am 25 years old.

# # Class method
# Person.set_species("Homo neanderthalensis")
# print(Person.species)  # Output: Homo neanderthalensis

# # Static method
# print(Person.is_adult(25))  # Output: True


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b  # Move to the next number

# fib = fibonacci()
# print(next(fib))  # Output: 0
# print(next(fib))  # Output: 1
# print(next(fib))  # Output: 1
# print(next(fib))  # Output: 2
# print(next(fib))  # Output: 3

# import matplotlib
# print(dir(matplotlib))


# import matplotlib.pyplot as plt

# # Data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# # Create the plot
# plt.plot(x, y, marker="o", linestyle="-", color="b", label="Line 1")

# # Labels and Title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Basic Line Plot")

# # Show Legend
# plt.legend()

# # Display the plot
# plt.show()

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()


# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 25, 15]
# plt.scatter(x, y, color="red")
# plt.show()

# import matplotlib.pyplot as plt
# import random 
# import numpy as np

# fig, axs = plt.subplots(2, 2)  # 2 rows, 2 columns

# axs[0, 0].plot([1, 2, 3], [4, 5, 6])
# axs[0, 1].bar(["A", "B", "C"], [5, 7, 3])
# axs[1, 0].scatter([1, 2, 3], [4, 5, 6])
# axs[1, 1].hist(np.random.randn(100), bins=10)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# # Create a 2x2 subplot grid
# fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# # Line Plot
# axs[0, 0].plot([1, 2, 3], [4, 5, 6], color="blue")
# axs[0, 0].set_title("Line Plot")

# # Bar Chart
# axs[0, 1].bar(["A", "B", "C"], [5, 7, 3], color="green")
# axs[0, 1].set_title("Bar Chart")

# # Scatter Plot
# axs[1, 0].scatter([1, 2, 3], [4, 5, 6], color="red")
# axs[1, 0].set_title("Scatter Plot")

# # Histogram (your original code)
# axs[1, 1].hist(np.random.randn(100), bins=10, color="purple", edgecolor="black")
# axs[1, 1].set_title("Histogram")

# # Adjust layout for better spacing
# plt.tight_layout()

# # Show the plots
# plt.show()




# import threading
# import time

# # Define a function that will be executed by each thread
# def print_numbers():
#     for i in range(5):
#         time.sleep(1)  # Simulate a delay
#         print(i,end=' ')

# def print_letters():
#     for letter in ['A', 'B', 'C', 'D', 'E']:
#         time.sleep(1)  # Simulate a delay
#         print(letter)

# # Create threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for both threads to complete
# thread1.join()
# thread2.join()

# print("Both threads are finished.")

# import threading
# import time

# def task():
#     time.sleep(1)
#     print("Task completed")

# # Create multiple threads
# threads = [threading.Thread(target=task) for _ in range(5)]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()


# import asyncio

# # Define an asynchronous function
# async def greet(name):
#     print(f"Hello, {name}!")
#     await asyncio.sleep(4)  # Simulates an I/O-bound operation (e.g., waiting for something)
#     print(f"Goodbye, {name}!")

# # Define another asynchronous function
# async def main():
#     # Start both greet tasks concurrently
#     task1 = asyncio.create_task(greet("Alice"))
#     task2 = asyncio.create_task(greet("Bob"))
    
#     # Wait for both tasks to complete
#     await task1
#     await task2

# # Run the event loop to execute the tasks
# asyncio.run(main())


# # Regular function
# def add(a, b):
#     return a + b

# # Lambda function that does the same thing
# add_lambda = lambda a, b: a + b

# # Using both functions
# print(add(2, 3))         # Outputs: 5
# print(add_lambda(2, 3))  # Outputs: 5


# # This is the function we're testing
# def add(a, b):
#     return a + b


# import unittest

# # Unit test class that inherits from unittest.TestCase
# class TestAddFunction(unittest.TestCase):
    
#     # Test case to check if the add function returns the correct result
#     def test_add_positive_numbers(self):
#         result = add(2, 3)
#         self.assertEqual(result, 5)  # Assert that the result is 5
    
#     # Test case to check if the add function handles negative numbers correctly
#     def test_add_negative_numbers(self):
#         result = add(-1, -4)
#         self.assertEqual(result, -5)  # Assert that the result is -5
    
#     # Test case to check if adding zero gives the correct result
#     def test_add_with_zero(self):
#         result = add(0, 5)
#         self.assertEqual(result, 5)  # Assert that the result is 5
    
#     # Test case to check if the function handles large numbers
#     def test_add_large_numbers(self):
#         result = add(1000000, 1000000)
#         self.assertEqual(result, 2000000)  # Assert that the result is 2000000

# # This allows us to run the tests if this script is executed directly
# if __name__ == '__main__':
    # unittest.main()


# #Fisrt option of exception
# class intersection_number():
#     def __init__(self):
#         self.list1 = [1,2,3,4,5,6,7,8,9]
#         self.list2 = [1,4,5,6,8,10,12,14]

#     def display(self):
#         try:
#             return set(self.list1).intersection(set(self.list2))
#         except Exception as error:
#             print(f'Error = {error}')
#             raise ValueError('Invalid Number !!!!!!!')

# r1 = intersection_number()
# result = r1.display()
# print(result)

# import numpy as np

# a = np.zeros([2, 2], dtype = int)
# print("\nMatrix a : \n", a)

# b = np.zeros(2, dtype = int)
# print("Matrix b : \n", b)
  
# c = np.zeros([3, 3])
# print("\nMatrix c : \n", c)


# import numpy as np

# a = np.zeros([3,2],dtype=float)
# print("\n matrix a : \n",a)


# s = "GeeksForGeeks"
# print(s[0])


# This will raise an IndentationError because it is not indented correctly.

#User function Template for python3

# def welcomeAboard(name):
#     print ("Welcome John")

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import re ##import re module to use regex

# } Driver Code Ends
#User function Template for python3


# def numberMatcher(str):
#     pat=  ("asdasd123asmdasdk34234kfdsd34sdfk5")##write the pattern here
#     match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
#     if(match): 
#         for i in match:
#             print(i, end=" ")
#     else:
#         print(-1,end="")


# #{ 
#  # Driver Code Starts.

# def main():
#     testcases = int(input()) #testcases
#     while(testcases > 0):
#         str = input()
#         numberMatcher(str)
#         print()
#         testcases -= 1
        


#         print("~")
# if __name__=='__main__':
#     main()
# # } Driver Code Ends

# x = 4
# print(x)
# x = "GFG"
# x+="Hello"
# print(x)

# x = 10
# print(type(x))
# x ="GFG"
# print(type(x))


# list1 = [10,20,30]
# list2 = [30,10,20]

# print("list1 + list2 = ",list1 +list2)
# print("list1 * 2 = : ",list1 *2)

# l = [1,12,3,4,5]
# print(l.remove(2))

# t1 = (1,2,4,3)
# t2 = (1,2,3,4)

# print(t1 < t2)

# set1 = {1,2,3}
# set2 = {4,5,6}
# print(len(set1 + set2))


# arr = tuple(map(int, input().split()))
# x = int(input())

# ########### Write your code below ###############
# # Print the index of x in arr
# arr.index(x)

# for num in range(4):
#     print('*' * 4)

# temperature = 25.25
# kelvin = 273 + temperature
# print(f'Celsius-{temperature}')
# print(f'Kelvin-{kelvin}')

# # cook your dish here
# temperature = 25.5
# print(f'Celsius-{temperature}')
# print(f'Kelvin-{temperature + 273}')

# # cook your dish here
# side_length = 4.5
# print("Area of a Square =",(side_length*side_length))
# print("Perimeter =",side_length*4)

# p = "Programming"
# result = p[:3]+'n'+p[4:]
# print(result)


# one = "Coding"
# two = "Chaf"
# two = two[:2] + 'e' + two[3:] 
# print(one + " " + two)


# # cook your dish here
# one = "Coding"
# two = "on"
# three = "CodeChef"
# four = one + " " + two + " " + three
# print(one + " - " + str(len(one)))
# print(two + " - " + str(len(two)))
# print(three + " - " + str(len(three)))
# print(four + " - " + str(len(four)))


# # cook your dish here
# s = "I Love Python"
# b = s[::-1]
# print(b)

# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# # Create a simple line plot
# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Plot')
# plt.show()

# import mysql.connector # type: ignore
# from mysql.connector import Error # type: ignore

# try:
#     # Establishing the connection to the database
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="J12345%",
#         database="test"
#     )

#     # Create a cursor object to interact with the database
#     my_cursor = my_db.cursor()

#     # Execute the query to show databases
#     my_cursor.execute("SHOW DATABASES")

#     # Loop through the result and print each database
#     print("Databases:")
#     for x in my_cursor:
#         print(x)

# except Error as e:
#     print(f"Error: {e}")

# finally:
#     # Ensure the connection is closed even if there's an error
#     if my_db.is_connected():
#         my_cursor.close()
#         my_db.close()
#         print("Connection closed.")
