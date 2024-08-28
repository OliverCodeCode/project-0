"""
    Represents a character in the game, with a name, health, inventory, and dialogue.
    
    The `character` class provides methods to interact with the character, such as talking to the player and receiving items.
    
    Attributes:
        name (str): The name of the character.
        health (int): The current health of the character.
        inventory (list): The items the character is carrying.
        dialogue (dict): A dictionary mapping player messages to the character's responses.
    
    Methods:
        talk_to_player(player_message: str) -> None:
            Prints the character's response to the given player message, if it exists in the dialogue dictionary.
        recieve_item(item: Any) -> None:
            Adds the given item to the character's inventory.
    """
class Character:
    def __init__(self, name, health, inventory, dialogue):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.dialogue = dialogue

    def talk_to_player(self, player_message):
        for sentence in self.dialogue:
            if player_message == sentence:
                print(self.dialogue[sentence])

    def recieve_item(self, item):
        self.inventory.append(item)
