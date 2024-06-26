# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 3

H1 = input("Course 1 hours: ")
G1 = input("Grade for course 1: ")
H2 = input("Course 2 hours: ")
G2 = input("Grade for course 2: ")
H3 = input("Course 3 hours: ")
G3 = input("Grade for course 3: ")
H4 = input("Course 4 hours: ")
G4 = input("Grade for course 4: ")

TH = int(H1) + int(H2) + int(H3) + int(H4)
print("Total hours:", TH)

TQP = (int(H1) * int(G1)) + (int(H2) * int(G2)) + (int(H3) * int(G3)) + (int(H4) * int(G4))
print("Total quality points:", TQP)

GPA = TQP / TH
print("Your GPA for this semester is", round(GPA, 2))
