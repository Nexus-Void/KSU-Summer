text = input("enter a sentence ")
y = int(input("enter a offset "))
w = ""
for i in range(len(text.upper())):
    ch = text.upper()[i]

    if ch == ' ':
        w += ' '
        continue

    else:
        w += chr((ord(ch) + y - 65) % 26 + 65)
        continue

print(w)
