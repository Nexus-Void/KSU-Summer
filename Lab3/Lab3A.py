# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 3

AO = input("Amount owed: $")
APR = input("APR: ")
percentage = float(APR) / 100

MPR = float(APR) / 12
print("Monthly percentage rate: " + str(round(MPR, 3)))

MIP = int(AO) * percentage / 12
print("Minimum payment: $" + str(round(MIP, 2)))
