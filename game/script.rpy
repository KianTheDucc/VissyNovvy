# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ronnie")

define f = Character("Duckman")

define r = Character("Halo3RAT")

define n = Character("Narrator")

define ronnie = Image("ronnie.png")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ronnie

    # These display lines of dialogue.

    e "Hello there, I am Ronnie, Saviour of KFC."

    e "I have acquired the legendary KFG, the Kentucky Fried Gun."

    e "As you probably already know, It is very deadly and shoots popcorn chicken."

    hide ronnie

    show ducki

    f "Ronnie! There are rats invading, we need your help!"

    f "Take the KFG and GO!"

    show ronnie

    default menuset = set()


    menu chapter_1_places:

        set menuset
        "What should I do?"

        "Kill the rats":
            jump kill_the_rats

        "kill my boss":
            jump kill_my_boss

    
    label kill_the_rats:

        show ronnie

        e "Got it boss."

        hide ronnie

        show halo3rat

        r "NOOO MY BRETHREN, I WILL AVENGE YOUUU"

        n "To be continued..."


        return
    

    label kill_my_boss:

        show ronnie

        e "Sorry boss, these are my brethren"
   

    

    # This ends the game.

    return
