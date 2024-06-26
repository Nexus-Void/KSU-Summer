# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 1

# Program Lab1C.py
# Demonstrate the use of the input function to read numeric data.
# Calculate fuel efficiency based on values entered by the user.

miles = input("Enter the number of miles: ")
gallons = input("Enter the gallons of fuel used: ")

mpg = int(miles) / float(gallons)
print("miles Per Gallon: " + str(mpg))
