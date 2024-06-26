import random
scorecounter = 0
incorrectcounter = 0
x = 0
print("[Mathletes Game]")

GM = input("Choose a game mode (0=Easy, 1=Hard): ")

if GM == "0":
    print("Playing on easy mode, huh? Okay!")
    while scorecounter > -1:
        if incorrectcounter == 2:
            print("incorrect!")
            print("Game over...")
            break
        n1 = random.randint(-255, 255)
        n2 = random.randint(-255, 255)
        correct = int(n1) * int(n2)
        x = x + 1
        w = input("Q" + str(x) + ". " + str(n1) + " * " + str(n2) + " = ?\n")
        if int(w) == correct:
            print("Correct!")
            scorecounter = scorecounter + 1
            incorrectcounter = 0
            if scorecounter == 3:
                print("you win")
                break
            continue
        else:
            while incorrectcounter < 2:
                print("incorrect! Try again.")
                incorrectcounter = incorrectcounter + 1
                w = input()
                if int(w) == correct:
                    print("Correct!")
                    scorecounter = scorecounter + 1
                    incorrectcounter = 0
                    if scorecounter == 3:
                        print("you win")
                        exit()
                    break
            continue

if GM == "1":
    print("So, you want a challenge? okay!")
    while scorecounter > -1:
        n1 = random.randint(-255, 255)
        n2 = random.randint(-255, 255)
        correct = int(n1) * int(n2)
        x = x + 1
        w = input("Q" + str(x) + ". " + str(n1) + " * " + str(n2) + " = ?\n")
        if int(w) == correct:
            print("Correct!")
            scorecounter = scorecounter + 1
            if scorecounter == 6:
                print("you win")
                break
            continue
        else:
            print("incorrect!")
            print("Game over...")
        break
