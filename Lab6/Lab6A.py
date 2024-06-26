def isValid(x, y):
    s = x + y
    return s > 30


def area(x, y):
    a = x * y
    return a


def perimeter(x, y):
    p = 2 * x + 2 * y
    return p


X = "Y"
while X == "Y":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if isValid(width, height):
        print("This is a valid rectangle.")
        print("The area is:", area(width, height))
        print("The perimeter is:", perimeter(width, height))
        X = input("\nDo you want to enter another width and height (Y/N)?: ")
    else:
        print("This is an invalid rectangle.")
        X = input("\nDo you want to enter another width and height (Y/N)?: ")
    if X == "N":
        print("Program Ends")
        break
