import os

# Task 1
HighScore = [["", 0] for i in range(10)]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "HighScore.txt")

# Task 2
def ReadHighScores():
    global HighScore
    if not os.path.exists(FILE_PATH):
        return
    try:
        with open(FILE_PATH, "r") as f:
            for i in range(0, 10):
                name = f.readline().strip()
                score = f.readline().strip()
                if name and score:
                    HighScore[i][0] = name
                    HighScore[i][1] = int(score)
    except Exception as e:
        print(f"Error reading high scores: {e}")

# Task 3
def OutputHighScores():
    print("\n--- High Scores ---")
    for i in range(len(HighScore)):
        if HighScore[i][0]:
            print(f"{i+1}. {HighScore[i][0]}: {HighScore[i][1]}")
        else:
            print(f"{i+1}. <Empty>")

# Task 5
def GetPlayerInput():
    while True:
        playername = input("Please input the player name (3 characters): ")
        if len(playername) != 3:
            print("The inputted player name must be exactly 3 characters, please try again.")
            continue
        try:
            score = int(input("Please input the player score: "))
            if score > 100000:
                print("The inputted score is too high! Please try again.")
                continue
            return playername, score
        except ValueError:
            print("Invalid score. Please enter a number.")

# Task 6
def calculate_top(playername, score):
    global HighScore
    # Add new score to the list
    HighScore.append([playername, score])
    # Sort the list by score descending
    HighScore.sort(key=lambda x: int(x[1]), reverse=True)
    # Keep only top 10
    HighScore = HighScore[:10]

    # Check if the new player made it to top 10
    found = False
    for entry in HighScore:
        if entry[0] == playername and entry[1] == score:
            found = True
            break
    return found

def SaveHighScores():
    try:
        with open(FILE_PATH, "w") as f:
            for name, score in HighScore:
                f.write(f"{name}\n")
                f.write(f"{score}\n")
    except Exception as e:
        print(f"Error saving high scores: {e}")

def run_high_scores():
    ReadHighScores()
    OutputHighScores()
    playername, score = GetPlayerInput()
    if calculate_top(playername, score):
        print(f"Congratulations {playername}! You made it to the Top 10!")
    else:
        print(f"Sorry {playername}, you didn't make it to the Top 10.")
    OutputHighScores()
    SaveHighScores()

if __name__ == "__main__":
    run_high_scores()
