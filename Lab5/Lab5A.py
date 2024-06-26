print("Please enter 10 numbers and this program will display the largest.")
Largest = -10000000
for i in range(10):
    C = i + 1
    Q = input("Please enter number " + str(C) + ": ")
    if int(Q) > Largest:
        Largest = int(Q)

print("\nThe largest number was " + str(Largest))
