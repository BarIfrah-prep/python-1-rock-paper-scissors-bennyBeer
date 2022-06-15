# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like randome and time packages wev'e discussed about) 
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
game_on = True
dict_game = {1: "rock", 2: "paper", 3: "scissors"}

while game_on:
    player_choice = int(input("choose your number:\n"))
    x = random.randint(1, 3)
    if  player_choice < 4 and player_choice > 0:
        # same number checking
        if player_choice == x:
            print("teko teko press y below if you want to play again")
        # player choose rock and computer choose scissors.
        elif player_choice == 1 and player_choice + 2 == x:
            print(f"{dict_game[1]} won")
        # player choose paper and computer choose rock.
        elif player_choice == 2 and x == 1:
            print(f"{dict_game[2]} won")
        # player choose scissors and computer choose paper.
        elif player_choice - 1 == x and x == 2:
            print(f"{dict_game[3]} won")
        else:
            print("computer won")
    else:
        print("mister player follow the instructions")
        continue
    re_game = input("press y if you want to continue and press n if you want to stop")
    while re_game != "y" and re_game != "n":
        re_game = input("press y if you want to continue and press n if you want to stop")
    if re_game == "n":
        print("nice match")
        break










