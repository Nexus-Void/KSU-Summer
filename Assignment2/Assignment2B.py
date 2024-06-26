# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: assignment 2

C = input("Enter a character to use: ")
W = 0
while W < 3:
    W = int(input("Enter the diamond's width: "))

    if W < 3:
        print("Please enter a width of at least 3.")


if W % 2 == 0:
    W = W + 1
    print("To make a diamond, we'll use", W, "as the width instead.")

row = ""
counter = 0
for i in range(W):
    if i < (W + 1) / 2:
        counter = 2 * i + 1
    else:
        counter = counter - 2
    spaces = (W - counter) / 2
    for j in range(W):
        if j < spaces:
            row = row + " "
            continue
        if j < spaces + counter:
            row = row + C
    print(row)
    row = ""
