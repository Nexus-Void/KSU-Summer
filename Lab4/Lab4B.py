# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 4

print("Welcome!")
NUM = input("Please input a number: ")

print("\nWhat would you like to do to this number: ")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
x = input()
if x == "0":
    print("\nThe additive inverse of", float(NUM), "is", float(NUM) * -1)

elif x == "1":
    if NUM == "0":
        print("\nCannot divide by 0!")
    elif NUM > "0" or NUM < "0":
        print("\nThe reciprocal of", float(NUM), "is", float(NUM) ** -1)


elif x == "2":
    print("\nThe square of", float(NUM), "is", float(NUM) ** 2)

elif x == "3":
    print("\nThe cube of", float(NUM), "is", float(NUM) ** 3)

elif x == "4":
    print("\nThank you, goodbye!")

elif x > "4" or x < "0":
    print("\nInvalid input, please try again!")
