# Game function

import random

def game():
    print("Welcome to the game!")
    score = random.randint(1,200)
    # read a file from hiscore.txt
    with open("hiscore.txt", "r") as f:
        Hiscore = f.read()
        if (Hiscore != ""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0
        

    print(f"Your score is: {score}")
    if(score > Hiscore or Hiscore == ""):

        with open("hiscore.txt", "a") as f:
            f.write(str(score) + "\n")

        return score
    
game()