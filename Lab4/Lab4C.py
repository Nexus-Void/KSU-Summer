# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Lab 4

print("Welcome!")
print("You have $1000 in your account.")
IV = 1000

M = "Y"

while M == "Y" or M == "y":
    print("\nMenu")
    print("0  – Make a deposit")
    print("1  – Make a withdrawal")
    print("2  – Display account value")

    x = input("\nPlease make a selection: ")

    if x == "0":
        D = input("How much would you like to deposit?: ")
        IV = (IV + float(D))
        print("Your current balance is $" + str(IV))

    if x == "1":
        W = input("How much would you like to withdraw?: ")
        if IV > float(W):
            IV = IV - float(W)
            print("Your current balance is $" + str(IV))
        else:
            print("Not enough balance. Withdrawal cancelled.")

    if x == "2":
        print("Your current balance is $" + str(IV))

    if x > "2" or x < "0":
        print("Invalid entry, please try again.")

    M = input("Would you like to return to the main menu (Y/N)?: ")

    if M == "N" or M == "n":
        print("\nThank you for banking with us!")
        break
