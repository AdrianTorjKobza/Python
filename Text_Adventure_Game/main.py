from room import Room
from character import Character, Enemy

# Create the Kitchen object and set the name and description.
kitchen = Room("Kitchen")
kitchen.set_description("The perfect place to cook human brains.")

# Create the Dining Hall object and set the name and description.
dining_hall = Room("Dining Hall")
dining_hall.set_description("The place to eat human brains.")

# Create the Ballroom object and set the name and description.
ballroom = Room("Ballroom")
ballroom.set_description("The place to dance with Zombies.")

# Create the map of the rooms.
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Create Dave character and define his weakness.
dave = Enemy("Dave", "A smelly zombie.")
dave.set_conversation("Arrrr.... I will eat your brain... brrrgghhh...")
dave.set_weakness("cake")

# Set Dave character in the Kitchen.
kitchen.set_character(dave)

# Create Elena character and define her weakness.
elena = Enemy("Elena", "The wonder woman.")
elena.set_conversation("How do I look?")
elena.set_weakness("banana")

# Set Elena character in the Kitchen.
dining_hall.set_character(elena)

# Set the starting point in the Dining Hall.
current_room = dining_hall

# Set the alive status
alive = True

# Play the game while alive.
while (alive):

    # Display the current room details
    current_room.get_details()

    inhabitant = current_room.get_character()

    # Check if there is a character in the room.
    if inhabitant is not None:
        inhabitant.describe()

    command = input("What to you want to do? (move / talk / fight): ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print ("There is no one here to talk to!")
    elif command == "fight":
        if inhabitant is not None:
            combat_item = input("Choose your weapon (banana, cake): ")
            alive = inhabitant.fight(combat_item)
        else:
            print ("There is no one to fight with!")
