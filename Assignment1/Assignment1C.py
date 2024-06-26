# Class: CSE 132L
# Section: W2 Python
# term: Summer 2024
# Instructor: Douglas Malcolm
# Name: Logan White
# Lab: Assignment 1

print("[How far your donation goes]")

S = input("\nHow many cans of soups? ")
R = input("How many bags of rice? ")
V = input("How many cans of vegetables? ")
P = input("How many cans of peanut butter? ")

PFPS = int(S) * 2
PFPR = int(R) * 4
PFPV = int(V) * 3.5
PFPP = int(P) * 7

TPF = float(PFPS) + float(PFPR) + float(PFPV) + float(PFPP)

print("\nYour donation will help feed", float(TPF), "people!")
print(PFPS, "people with the", S, "can(s) of soup")
print(PFPR, "people with the", R, "bag(s) of rice")
print(float(PFPV), "people with the", V, "can(s) of vegetables")
print(PFPP, "people with the", P, "can(s) of peanut butter")
