import Character from character
import Item from item
import playworlde from wordle

print("Welcome to the game!")
d1 = input("You come up to a field and see a star, do you want to pick it up? (y/n)")
if d1 == "y":
    print("You picked up the star")
    star = Item("Star", "A star that can be used to make wishes", 10)
    print("You have picked up the star. It is worth 10 points. You can now use it to make a wish.")
    player.recieve_item(star)
    d1a = input("You see a house, do you want to go inside? (y/n)")
    if d1a == "y":
        print("You went inside the house")
        d1b = input("You see a door, do you want to go through it? (y/n)")
        if d1b == "y":
            print("You went through the door")
            d1c = input("You see a chest, do you want to open it? (y/n)")
            if d1c == "y":
                print("You opened the chest")
                d1d = input("You see a key, do you want to pick it up? (y/n)")
                if d1d == "y":
                    print("You picked up the key")
                    key = Item("Key", "A key that can be used to open doors", 5)



