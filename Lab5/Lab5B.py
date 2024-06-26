size = input("Please enter a value for the size: ")

sxs = size + "x" + size

print("This is the requested " + sxs + " box:")
for i in range(int(size)):
    for j in range(int(size)):
        print("*", end="")
    print()

print("This is the right-facing " + sxs + " right-triangle:")
for i in range(int(size)):
    for j in range(i + 1):
        print("*", end="")
    print()

print("This is the left-facing " + sxs + " right-triangle:")
for i in range(int(size)):
    for j in range(int(size) - i - 1):
        print(" ", end="")
    for x in range(i + 1):
        print("*", end="")
    print()
