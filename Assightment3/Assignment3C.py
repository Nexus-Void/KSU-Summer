def invalid_size(x):
    if x < 1:
        print("Invalid input!")


def invalid_color(x):
    if x > 1 or x < 0:
        print("Invalid input!")


SS = 0
SB = 0
CS = -1
CB = -1
while SS < 1:
    SS = int(input("Enter the size of the square: "))
    invalid_size(SS)
    continue
while SB < 1:
    SB = int(input("Enter the size of the border: "))
    invalid_size(SB)
    continue
while CS > 1 or CS < 0:
    CS = int(input("Enter the color of the square: "))
    invalid_color(CS)
    continue
while CB > 1 or CB < 0:
    CB = int(input("Enter the color of the border: "))
    invalid_color(CB)
    continue
print("PBM File contents: ")
print("P1")
dimensions = SS + SB + SB
print(dimensions, "", dimensions)

for i in range(dimensions):
    for j in range(dimensions):
        if i < SB or i >= SB + SS or j < SB or j >= SB + SS:
            print(CB, end="  ")
        else:
            print(CS, end="  ")
    print()
