#datetime
 
import datetime
current_time = datetime.datetime.now()
print("Current date and time: ", current_time)

#python version

import sys
python_version = sys.version
print("Python version: ", python_version)

#Compute n + nn + nnn

n = int(input("Enter a number: "))
result = n + n*11 + n*111
print("Result of n + nn+ nnn is :" , result)

# Read and Print Various Types of Variables

name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
student = input("Are you a student? (yes/no):").strip().lower()
print("\n Variable values:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", student)
print("\n Variable types:")
print("Name type:", type(name))
print("Age type:", type(age))
print("Height type:", type(height)) 
print("Student type:", type(student))

# Print the Calendar of a Given Month and Year

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year, month))