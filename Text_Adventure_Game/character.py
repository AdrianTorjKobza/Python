# Create the class Character.
class Character():

    # Create a character.
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say.
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character.
    def talk(self):
        if self.conversation is not None:
            print(self.name + ": " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")

    # Fight with this character.
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you.")
        return True

# Create the class Enemy.
class Enemy(Character):

    # Create the enemy character.
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    # Set character weakness.
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    # Get character weakness.
    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You killed " + self.name + " with the " + combat_item + ".")
            return True
        else:
            print("Poor choice of weapon. " + self.name + " kills you.")
            return False
