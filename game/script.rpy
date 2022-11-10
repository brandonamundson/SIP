# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hacker = Character("Hacker", color="#7ABEC5")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "hacker.png" or "hacker.jpg") to the
    # images directory to show it.

    scene hacker

    # These display lines of dialogue.

    hacker "You've created a new Ren'Py game."

    hacker "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
