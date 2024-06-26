# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Assignment 1
import math

print("First color")
R1 = input("R: ")
G1 = input("G: ")
B1 = input("B: ")

print("\nSecond color")
R2 = input("R: ")
G2 = input("G: ")
B2 = input("B: ")

RD = float(R2) - float(R1)
GD = float(G2) - float(G1)
BD = float(B2) - float(B1)

RS = RD ** 2
GS = GD ** 2
BS = BD ** 2

CS = RS + GS + BS
CD = math.sqrt(CS)

print("\nColor Distance:" + str(CD))
