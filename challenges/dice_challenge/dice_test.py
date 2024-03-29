#!/usr/bin/python3

# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Greater_Three

def main():

    # create two cheater objects
    cheater1 = Cheat_Greater_Three() # make sure cannot roll below a 3
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6 

    # both players take turns
    cheater1.roll() 
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()
