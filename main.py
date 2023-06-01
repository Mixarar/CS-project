# ---- Importing libraries ----
import ranint from random
# ---- Setting up variables ----
name = "NoName"
time = 0
useless_minutes = 0
codes = []
price = 0
accounts = []
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
    accid = ranint(1,999999)
    print("Your account is now created:",name,"ID:",accid)
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
            print("Please make sure your input is correct.")
    print("The hour of your journey is:",hour)
    # ---- Getting the useless minutes ----
    while True:
        try:
            uselesss_minutes = int(input())
            if useless_minutes > 59:
                raise TypeError
            else:
                break
        except:
            print("Please make sure your input is correct.")
    print("The minute of your journey is:",useless_minutes)
    # ---- Inputing the codes of the journey ----
    for i in range(1,3):
        while True:
            try:
                input_code = int(input())
                if input_code > 5:
                    raise TypeError
                else:
                    
                    break

