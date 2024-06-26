# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: assignment 4
def message_input(x, y):
    if any(digit.isdigit() for digit in x):
        print("\nSorry we can only process messages with letters and spaces, and the offset")
        print("must be between 0 and 26.")
        return False

    if y < 0 or y > 26:
        print("\nSorry we can only process messages with letters and spaces, and the offset")
        print("must be between 0 and 26.")
        return False

    return True


def message_encryption(x, y):
    w = ""
    for i in range(len(x.upper())):
        ch = x.upper()[i]

        if ch == ' ':
            w += ' '
            continue

        else:
            w += chr((ord(ch) + y - 65) % 26 + 65)
            continue
    return w


A = "Y"

while A == "Y" or A == "y":
    message = str(input("Enter your message:\n"))
    offset_value = int(input("Enter the offset value: "))
    mi = message_input(message, offset_value)

    if mi is False:
        A = input("\nDo you want to encrypt another message?: ")
        if A == "N" or A == "n":
            print("\nClosing out...")

    else:
        me = str(message_encryption(message, offset_value))
        print("\nYour secret message is...")
        print(me)
        A = input("Do you want to encrypt another message?: ")
        if A == "N" or A == "n":
            print("\nClosing out...")
