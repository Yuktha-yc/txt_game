def start_game():
    print("Welcome to the Maze Adventure!")
    print("You find yourself standing at the entrance of a dark and thick forest.")
    print("Do you want to enter the forest maze? (yes/no)")

    choice = input(">>> ").lower()

    if choice == "yes":
        enter_dungeon()
    elif choice == "no":
        print("You decide to leave.Game over!")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        start_game()

def enter_dungeon():
    print("\nYou step into the Forest.")
    print("You find there are two paths available, Towards right and towards left.")
    print("Which path would you take? (left/right)")

    choice = input(">>> ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        enter_dungeon()

def left_path():
    print("\nYou walk down the left path and you find another way towards right.")
    print("Do you want to take the right path or, continue the same path.? (straight/right)")

    choice = input(">>> ").lower()

    if choice == "straight":
        str()
    elif choice == "right":
        print("You took  the right path, but unfortunately you get yourself trapped! ")
        print("Game Over!..")
        start_game()
    else:
        print("Invalid choice. Please type 'straight' or 'right'.")
        left_path()
def str():
    print("\n You continue to walk on the straight path")
    print("You reach a dead end, and find there's a right turn.")
    print("Do you want to take the right turn, or head back to the starting point and begin all-over..? (right/startover)")
    choice= input(">>> ").lower()
    if choice=="right":
        rit()
    elif choice== "startover":
        start_game()
    else:
        print("Invalid choice. Please type 'right' or 'startover'.")
        str()
def rit():
    print("\n You chose to walk on the right path")
    print("On the same path, you encounter another right turn. ")
    print("Do you want to take the right turn, or continue on the straight path..? (right/straight)")
    choice= input(">>> ").lower()
    if choice=="right":
        print("Oh no.! There was a beast waiting for a prey. You get attacked by it and get killed. ")
        print("Game Over!.")
    elif choice== "straight":
        print("\nAfter walking for so long on the same path, you reach the end of the maze..!")
        print("Horay..! You win, Game Over")
    else:
        print("Invalid choice. Please type 'right' or 'straight'.")
        rit()


def right_path():
    print("\nYou take the right path, it was a dense way , you could hardly see anything..")
    print("You hear a lot of haunting noises... \n After walking for several minutes, on the same path you find another way towards left")
    print("Do you want to continue straight or head to the left path.? (left/ straight)")

    choice = input(">>> ").lower()

    if choice == "left":
        print("You take a left turn, but unfortunately get yourself in a trap!")
        print("Badluck :( Game Over..!")
    elif choice == "straight":
        str2()
    else:
        print("Invalid choice. Please type 'left' or 'straight'.")
        right_path()
def str2():
    print("\n You continued to walk on the straight path")
    print("You find there's a left turn and a straight path.")
    print("Do you want to take the left turn,or continue straight path, or head back to the starting point and begin all-over..? (left/startover/straight)")
    choice= input(">>> ").lower()
    if choice=="left":
        print("After walking for so long on the same path, you reach the end of the maze..!")
        print("Horay..! You win, Game Over")
    elif choice== "startover":
        start_game()
    elif choice=="straight":
        print("Boom..! you fall into the pit-fall...  >>_<<  \n")
        print("Game Over..! :( ")
    else:
        print("Invalid choice. Please type 'left' or 'straight' or 'startover.")
        str2()
# Start the game
start_game()