# ---- Importing libraries ----
import randint from random
# ---- Setting up variables ----
name = "NoName"
time = 0
useless_minutes = 0
codes = []
priceHome = 0
priceStart = 0
priceEnd = 0
priceTotal = 0
accounts = []
bookid = 0
accid = 0
# ---- Getting the correct name ----
def create_account():
    print("Please input your name...")
    while True:
        try:
            input_name = input()
            if len(input_name) <= 2 or len(input_name) >=16:
                raise TypeError
            else:
                name = input_name
                break
        except:
            print("The name should be longer than 2 characters and shorter than 16.")
    print("Your name is:",name)
    accid = randint(1,999999)
    print("Your account is now created:",name,"ID:",accid)
# ---- Booking a journey ----
def book_journey():
    # ---- Getting the correct hour ----
    print("Please input the hour of your journey in a 24 hour format.")
    while True:
        try:
            input_time = int(input())
            if input_time > 23:
                raise TypeError
            else:
                time = input_time
                break
        except:
            print("Please make sure the hour you inputed is correct.")
    print("The hour of your journey is:",time)
    # ---- Getting the useless minutes ----
    while True:
        try:
            uselesss_minutes = int(input())
            if useless_minutes > 59:
                raise TypeError
            else:
                break
        except:
            print("Please make sure the minutes you inputed is correct.")
    print("The minute of your journey is:",useless_minutes)
    # ---- Inputing the codes of the journey ----
    for i in range(0,2):
        while True:
            try:
                part_journey = ""
                if i == 1:
                    part_journey = "Home to start station"
                elif i == 2:
                    part_journey = "Start station to end station"
                elif i == 3:
                    part_journey = "End station to destination"
                print("Please input the code for the",part_journey)
                input_code = int(input())
                if input_code > 5:
                    raise TypeError
                else:
                    codes.insert(input_code-1,i)
                    break
            except:
                print("Please make sure the code you inputed is correct.")
    print("The codes you inputed are: "+"C"+str(codes[0])+"-->"+"M"+str(codes[1])+"-->"+"F"+str(codes[2]))
    bookid = randint(1,999999)
    print("Your booking ID: "+str(bookid))
# ----Def function to save data into file Account.txt----
def SaveAccountData():
# Try to find Account.txt and append user's name into file
    try:
        UserData = "Account.txt"
        AccountFile = open(UserData,"a")
        AccountFile.write(name)
        AccountFile.write(bookid)
        AccountFile.write(accid)
        AccountFile.close()
# If file not found print error    
    except:
        print("{} not found".format(UserData))
        
# ----Def function to save bookings data into files Bookings.txt----
def BookingsData():
# Try to find Bookings.txt and append booking codes into file
    try:
        BookingData = "Booking.txt"
        BookingFile = open(BookingData,"a")
        BookingFile.write(input_code)
        BookingFile.close()
    except:
        print("{} not found".format(BookingData))

def menu()
    print("1. Create account")
    print("2. Log in account")
    print("3. Book journey (Must be logged in)")
    print("4. Find booked journeys")
    choice = int(input())
    if choice.isdigit():
        if choice >= 1 and choice <=4:
            if choice == 1:
                print("Selected 1")
            elif choice == 2:
                print("Selected 2")
            elif choice == 3:
                print("Selected 3")
            else:
                print("Selected 4")
    else:
        print("Wrong input, please try again.")
        menu()
# ----Define the subroutine to calculate prices and totalprice----
def priceHome():
    if codes[0] >= 1 and codes[0] <= 5:
        if codes[0] == 1:
            priceHome = 1.50
            print("The price of start journey is" + str(priceHome) + "$")
        elif codes[0] == 2:
            priceHome = 3
            print("The price of start journey is" + str(priceHome) + "$")
        elif codes[0] == 3:
            priceHome = 4.50
            print("The price of start journey is" + str(priceHome))
        elif codes[0] == 4:
            priceHome = 6
            print("The price of start journey is" + str(priceHome))
        elif codes[0] == 5:
            priceHome = 8
            print("The price of start journey is" + str(priceHome))
    else:
        print("Input cannot be processed, please try again")
        priceHome()

def priceStart():
    if codes[1] >= 1 and codes[1] <= 5:
        if codes[1] == 1:
            priceStart = 5.75
            print("The price of start journey is" + str(priceStart) + "$")
        elif codes[1] == 2:
            priceStart = 12.5
            print("The price of start journey is" + str(priceStart) + "$")
        elif codes[1] == 3:
            priceStart = 22.25
            print("The price of start journey is" + str(priceStart) + "$")
        elif codes[1] == 4:
            priceStart = 34.5
            print("The price of start journey is" + str(priceStart) + "$")
        elif codes[1] == 5:
            priceStart = 45
            print("The price of start journey is" + str(priceStart) + "$")
    else:
        print("Input cannot be processed, please try again")
        priceStart()

def priceEnd():
    if codes[2] >= 1 and codes[2] <= 5:
        if codes[2] == 1:
            priceEnd = 1.5
            print("The price of start journey is" + str(priceEnd) + "$")
        elif codes[2] == 2:
            priceEnd = 3
            print("The price of start journey is" + str(priceEnd) + "$")
        elif codes[2] == 3:
            priceEnd = 4.5
            print("The price of start journey is" + str(priceEnd) + "$")
        elif codes[2] == 4:
            priceEnd = 6
            print("The price of start journey is" + str(priceEnd) + "$")
        elif codes[2] == 5:
            priceEnd = 8
            print("The price of start journey is" + str(priceEnd) + "$")
    else:
        print("Input cannot be processed, please try again")
        priceEnd()

def priceTotal():
    if time = 10 and minutes = 0:
        PriceTotal = (priceHome + priceStart + priceEnd) * 0.4
        print("The total price of your journey is:" + str(priceTotal) + "$")
    else:
        PriceTotal = (priceHome + priceStart + priceEnd)
        print("The total price of your journey is:" + str(priceTotal) + "$")

# Main program thingy code whatever
menu()
