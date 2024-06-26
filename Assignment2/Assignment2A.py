# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: assignment 2

print("[Image Encoding Checker]")
W = input("What is the image width? ")
H = input("What is the image height? ")
B = input("What is the file size (in bytes)? ")

A = int(W) * int(H)
TB = int(B) / int(A)
BPC = int(TB) * 2

if BPC == 8 or BPC == 16 or BPC == 32:
    print("\nThe RGBA image is encoded with", BPC, "bits per channel.")

else:
    print("\nThis information is invalid - please re-enter it.")
