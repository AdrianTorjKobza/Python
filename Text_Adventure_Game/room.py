# Create the class Room.
class Room():

    # Create a room.
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    # Set the room name.
    def set_name(self, room_name):
        self.name = room_name

    # Get the room name.
    def get_name(self):
        return self.name

    # Set the room the description.
    def set_description(self, room_description):
        self.description = room_description

    # Get the room description.
    def get_description(self):
        return self.description

    # Set character in room.
    def set_character(self, new_character):
        self.character = new_character

    # Get character from room.
    def get_character(self):
        return self.character

    # Link the rooms between them. e.g. From Kitchen you can only go South to the Dining Hall.
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # Get the name and description of the current room. Display the valid directions.
    def get_details(self):
        print(self.name + ": " + self.description)

        valid_directions = ""

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction + ".")
            valid_directions = valid_directions + "--> " + str(direction) + " "

        print("You can go: " + valid_directions)

    # Move to the next room. If not possible, warn the user.
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\nYou can't go in that direction!")
            return self
