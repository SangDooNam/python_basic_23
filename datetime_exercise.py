"""Task 1

Write a Python program that uses the datetime module to display 
the current local time in readable format."""

from datetime import datetime

# now = datetime.now()

# x = now.ctime()

# print(x)

"""Task 2

Write a Python program to create a datetime object of your birthdate
(could be fake!) and display only the day and year of your birthday."""

birthday = datetime(1985, 10, 9, 20, 45)

print(birthday)