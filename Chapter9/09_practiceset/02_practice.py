# # Game function

# import random

# def game():
#     print("Welcome to the game!")
#     score = random.randint(1,56)
#     # read a file from hiscore.txt
#     with open("hiscore.txt", "r") as f:
#         hiscore = f.read()
#         if (hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score is: {score}")
#     if(score > hiscore or hiscore == ""):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
#             return score
# game()


# Game function

import random

def game():
    print("Welcome to the game!")
    score = random.randint(1,56)
    # read a file from hiscore.txt

    File = open("hiscore.txt", "r")
    hiscore = File.read()
    if (hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    File.close()

    print(f"Your score is: {score}")
    if(score > hiscore or hiscore == ""):
        File = open("hiscore.txt", "w")
        File.write(str(score))
        File.close()
        return score
    
game()