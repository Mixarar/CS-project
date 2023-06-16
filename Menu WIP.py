print("1.Create Account","\n"+"2.Log into Account","\n"+"3.Book a Journey","\n"+"4.Previous Journeys for Account")
print("Choose an option by typing the number in front")
nuhuh = True
while nuhuh:
    choice = input()
    try:
        int(choice)
    except ValueError:
        nuhuh = True
    if nuhuh:
        print("It's not an interger. Try again.")
    else:
        break
checkchoice = int(choice)
if checkchoice>4 or checkchoice<1:
    print("Unacceptable input. Try again.")
Û
