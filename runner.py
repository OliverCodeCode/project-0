"""
Handles the main game loop and flow of the text adventure game.

This module contains the main entry point for the game, which prompts the player to make choices and updates the game state accordingly. It includes logic for picking up items, making wishes, and navigating through different areas of the game world.
"""
from character import Character
from item import Item
import wordle
from wordle import hint



print("Welcome to the game!")
d1 = input("You come up to a field and see a star, do you want to pick it up? (y/n)")
player = Character("Player", 100, [], {})
if d1 == "y":
    print("You picked up the star")
    star = Item("Star", "A star that can be used to make wishes", 10)
    print("You have picked up the star. It is worth 10 points. You can now use it to make a wish.")
    player.recieve_item(star)
else:
    print("You did not pick up the star")
    print("As you leave the star you find yourself lost in the field as long stocks of corn stand around you. That star would be really helpful right now")
d2 = input("Would you like to go pick up the star? (y/n)")
if d2 == "y":
    print("You picked up the star")
    star = Item("Star", "A star that can be used to make wishes", 10)
    print("You have picked up the star. It is worth 10 points. You can now use it to make a wish.")
    player.recieve_item(star)
    print("It seems the only way out of here is to use the star to make a wish, what would you like to wish for?")
    wish = input("Do you wish for a way out of the field? (y/n)")
    if wish == "y":
        print("You wish for a way out of the field")
        star.use_item(player)
        print("You have been transported to a new area, suddenly you find yourself in a run down house")
        print("The lights are out and you can't see anything, you feel around the room and find yourself walking down a stairwell, at the end theres a locked door.")
        d3 = input("Would you like to search for a key? (y/n)")
        if d3 == "y":
            print("You search for a key")
            print("You find yourself in a room with a single chair in the center, sitting in the chair is the skeletone of a man with a key in his hand")
            key = Item("Key", "A key that can be used to open the door", 10)
            d31 = input("You start freaking out, but remind yourself that you need to find a way out. Would you like to take the key? (y)")
            if d31 == "y":
                print("You take the key")
                print("You have picked up the key. It is worth 10 points. You can now use it to open the door.")
                player.recieve_item(key)
                print("You walk back down to the door and use the key to open it")
                print("You have opened the door")
                key.use_item(player)
                print("You find yourself locked behind another door, this time it has a puzzle lock on it.")
                d33 = input("Would you like to play (y/n)")
                if d33 == "y":
                    wordle.playwordle()
                    if hint == "ggggg":
                        print("You win")
                        print("The door opens and you finally find yourself outside")
                        print(" standing infront of you is a woman, she looks towards you")
                        Woman = character("Woman", "Lilah", 10, "Nothing", "Well look at that, you escaped.")
                        character.talk_to_player(Woman, "")
                        print("You have won the game")

        else:
            print("Your scared out of your mind and cant find any other way out of the house, you eventually tear off the boards on the window and jump outside")
            print("You are now in a new area, suddenly you find yourself stranded at the top of a building")
            print("As you look down you realize that the city seems overgrown, as if humans didnt exist hear anymore")
            d32 = input("Would you like to try to find a way down? (y/n)")
            if d32 == "y":
                print("you get inside the building and find a way down")
                print("as you walk outside the city seems peaceful, like living here is a nice life")
                print("You find a new life in the city, Peaceful Ending")
            else:
                print("As you stay ontop of the building crying you hear a noise, as if there is someone else here")
                print("You look around and see a man with a knife, he starts to walk towards you")
                Man = character("Man", "David", 10, "knife", "awwww Im dying")
                print("You try to run but he catches you and as he is about to gut you for food you see another star in his hand")
                d33 = input("Would you like to take the star? (y/n)")
                if d33 == "y":
                    print("You take the star")
                    print("You have picked up the star. It is worth 10 points. You can now use it to make a wish.")
                    player.recieve_item(star)
                    print("It seems the only way out of here is to use the star to make a wish, what would you like to wish for?")
                    wish = input("Do you wish for a way out of the city? (y/n)")
                    if wish == "y":
                        print("You wish for a way out of the field")
                        player.use_item(star)
                        print("You have been transported back to the house, your back where you started")
                    else:
                        print("You dont make a wish and the man attacks you")
                        print("You kick him in the stomach and grab his knife")
                        print("You stab him in the chest and he falls to the ground")
                        character.Man.health = 0
                        character.talk_to_player(Man, "")
                        print("You slowly bleed out from your wounds and die.")

        
else:
    print("You did not pick up the star")
    print("As you leave the star you find yourself lost in the field, you cant seem to find a way out of the field and get lost.")


