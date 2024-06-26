l1 = ["1) Yes", "2) No"]
l2 = ["1) That's awful!", "2) What can I do?"]
l3 = ["1) Okay", "2) No"]

print("[Epic Quest Simulator!]")
print("Hello stranger! Do you have time to hear my tale?")
print(*l1, sep="\n")
S1 = input()
while S1 == "2":
    print("Ah, then goodbye")
    break
else:
    print("Thank you! I come from the land of Pax Bisonica. Our country has been")
    print("taken over by a cruel tyrant!")
    print(*l2, sep="\n")
    S2 = input()
    if S2 == "1":
        print("Alas, it is truly terrible...")
        print("Please, you must journey to Pax Bisonica and free our country!")
        print(*l3, sep="\n")
        S3 = input()
        if S3 == "1":
            print("Hooray!")
    else:
        print("Please, you must journey to Pax Bisonica and free our country!")
        print(*l3, sep="\n")
        S3 = input()
        if S3 == "2":
            print("Then all is lost...")
            