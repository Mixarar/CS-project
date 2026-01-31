# ---- Importing libraries ----
from random import randint
import os

# ---- Setting up variables ----
name = "NoName"
time = 0
useless_minutes = 0
codes = []
priceHome_val = 0
priceStart_val = 0
priceEnd_val = 0
priceTotal_val = 0
accounts = []
bookid = 0
accid = 0

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- Getting the correct name ----
def create_account():
    global name, accid
    print("Please input your name...")
    while True:
        try:
            input_name = input()
            if len(input_name) <= 2 or len(input_name) >= 16:
                raise ValueError
            else:
                name = input_name
                break
        except ValueError:
            print("The name should be longer than 2 characters and shorter than 16.")
    print("Your name is:", name)
    accid = randint(1, 999999)
    print("Your account is now created:", name, "ID:", accid)

# ---- Booking a journey ----
def book_journey():
    global time, useless_minutes, codes, bookid
    # ---- Getting the correct hour ----
    print("Please input the hour of your journey in a 24 hour format.")
    while True:
        try:
            input_time = int(input())
            if input_time > 23 or input_time < 0:
                raise ValueError
            else:
                time = input_time
                break
        except ValueError:
            print("Please make sure the hour you inputed is correct.")
    print("The hour of your journey is:", time)

    # ---- Getting the useless minutes ----
    print("Please input the minutes of your journey.")
    while True:
        try:
            input_minutes = int(input())
            if input_minutes > 59 or input_minutes < 0:
                raise ValueError
            else:
                useless_minutes = input_minutes
                break
        except ValueError:
            print("Please make sure the minutes you inputed is correct.")
    print("The minute of your journey is:", useless_minutes)

    # ---- Inputing the codes of the journey ----
    codes = []
    for i in range(1, 4):
        while True:
            try:
                part_journey = ""
                if i == 1:
                    part_journey = "Home to start station"
                elif i == 2:
                    part_journey = "Start station to end station"
                elif i == 3:
                    part_journey = "End station to destination"
                print(f"Please input the code (1-5) for the {part_journey}")
                input_code = int(input())
                if input_code < 1 or input_code > 5:
                    raise ValueError
                else:
                    codes.append(input_code)
                    break
            except ValueError:
                print("Please make sure the code you inputed is correct (1-5).")

    print(f"The codes you inputed are: C{codes[0]} --> M{codes[1]} --> F{codes[2]}")
    bookid = randint(1, 999999)
    print("Your booking ID: " + str(bookid))

# ----Def function to save data into file Account.txt----
def SaveAccountData():
    try:
        UserData = os.path.join(BASE_DIR, "Account.txt")
        with open(UserData, "a") as AccountFile:
            AccountFile.write(f"{name}\n")
            AccountFile.write(f"{bookid}\n")
            AccountFile.write(f"{accid}\n")
    except Exception as e:
        print(f"Error saving account data: {e}")

# ----Def function to save bookings data into files Bookings.txt----
def BookingsData():
    try:
        BookingData = os.path.join(BASE_DIR, "Bookings.txt")
        with open(BookingData, "a") as BookingFile:
            BookingFile.write(f"C{codes[0]} M{codes[1]} F{codes[2]}\n")
            BookingFile.write("--------------------Day Separation\n")
    except Exception as e:
        print(f"Error saving bookings data: {e}")

# ----Define the subroutine to calculate prices and totalprice----
def calculate_priceHome():
    global priceHome_val
    code = codes[0]
    prices = {1: 1.50, 2: 3.0, 3: 4.50, 4: 6.0, 5: 8.0}
    priceHome_val = prices.get(code, 0)
    print(f"The price of start journey is {priceHome_val}$")

def calculate_priceStart():
    global priceStart_val
    code = codes[1]
    prices = {1: 5.75, 2: 12.5, 3: 22.25, 4: 34.5, 5: 45.0}
    priceStart_val = prices.get(code, 0)
    print(f"The price of middle journey is {priceStart_val}$")

def calculate_priceEnd():
    global priceEnd_val
    code = codes[2]
    prices = {1: 1.5, 2: 3.0, 3: 4.5, 4: 6.0, 5: 8.0}
    priceEnd_val = prices.get(code, 0)
    print(f"The price of end journey is {priceEnd_val}$")

def calculate_priceTotal():
    global priceTotal_val
    total = priceHome_val + priceStart_val + priceEnd_val
    if time == 10 and useless_minutes == 0:
        priceTotal_val = total * 0.4
    else:
        priceTotal_val = total
    print(f"The total price of your journey is: {priceTotal_val}$")

# ----Defining subroutine to store prices and total prices of each journey----
def PricesFile():
    try:
        PricesData = os.path.join(BASE_DIR, "JourneyPrices.txt")
        with open(PricesData, "a") as f:
            f.write(f"Home: {priceHome_val}\n")
            f.write(f"Start: {priceStart_val}\n")
            f.write(f"End: {priceEnd_val}\n")
            f.write(f"Total: {priceTotal_val}\n")
            f.write("-------------------- Day Separation\n")
    except Exception as e:
        print(f"Error saving prices data: {e}")

def run_booking_system():
    print("--- Transport Booking System ---")
    create_account()
    book_journey()
    calculate_priceHome()
    calculate_priceStart()
    calculate_priceEnd()
    calculate_priceTotal()
    SaveAccountData()
    BookingsData()
    PricesFile()
    print("Booking complete and data saved.")

if __name__ == "__main__":
    run_booking_system()
