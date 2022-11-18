# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hacker = Character("Hacker", color="#7ABEC5")


# The game starts here.

label start:

    call hack from demonstrate
    call scam from help
    call learn from detect


    # This ends the game.

    return
