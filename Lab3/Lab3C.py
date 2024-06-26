# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 3

S = input("Enter the number of small sandwiches: ")
M = input("Enter the number of medium sandwiches: ")
L = input("Enter the number of large sandwiches: ")
XL = input("Enter the number of extra-large sandwiches: ")

print("\nYou've entered " + S + " small sandwiches.")
print("You've entered " + M + " medium sandwiches.")
print("You've entered " + L + " large sandwiches.")
print("You've entered " + XL + " extra-large sandwiches.\n")

TCT = (int(S) * 0.5) + (int(M) * 1.0) + (int(L) * 1.25) + (int(XL) * 2.25)
MIN = int(TCT)
SEC = (TCT - MIN) * 60

print("Total cooking time is", MIN, "minutes and", int(SEC), "seconds.")
