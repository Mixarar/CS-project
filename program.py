# Task 1
global HighScore
HighScore = [["",0] for i in range(10)]
# Task 2
def ReadHighScores():
    f = open("HighScore.txt", "r")
    for i in range(0,10):
        HighScore[i][0]=f.readline()[:-1]
        HighScore[i][1]=f.readline()[:-1]

# Task 3
def OutputHighScores():
    for i in range(len(HighScore)):
        print(HighScore[i])

# Task 4

#ReadHighScores()
#OutputHighScores()

# Task 5
while True:
    playername = input("Please input the player name:")
    if len(playername) != 3:
        print("The inputted player name is longer than 3, please try again..")
        continue
    score = int(input("Please input the player score:"))
    if score > 100000:
        print("The inputted score is too high! Please try again..")
        continue
    break

# Task 6
def calculate_top():
    if score > int(HighScore[len(HighScore)-1][1]):
        NewHighScore=HighScore
        NewHighScore.append([playername,score])
        for i in range(len(HighScore)-2,-1,-1):
            if score > int(NewHighScore[i][1]):
                temp = NewHighScore[i]
                NewHighScore[i]=NewHighScore[i+1]
                NewHighScore[i+1]=temp
            else:
                NewHighScore.pop()
                break
        return NewHighScore
    else:
        return False

# Task 7
ReadHighScores()
OutputHighScores()
NewHighScore = calculate_top()
print(NewHighScore)


# Task 8 Final

