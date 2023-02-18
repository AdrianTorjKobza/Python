time = [(30, 75), (0, 50), (60, 150), (90, 120), (10, 20), (0, 200)]
time.sort()

# List of max amount of rooms needed.
rooms = []
for i in range(len(time)):
    rooms.append([])
# Output: [[], [], [], [], [], []] - 6 empty lists / rooms inside one list.

def add_time_in_rooms (time):
    # Iterate over the rooms lists.
    for i in range(len(rooms)):
        flag = True
        
        # Check if current room is not empty.
        if len(rooms[i]) > 0:
            # Iterate over the time slots from the current room.
            for j in range(len(rooms[i])):
                # If we have an overlap set the flag to False. 
                if time[0][0] < rooms[i][j][1]:
                    flag = False
            
            # If we have no overlap, add the time slot in the current room. 
            if flag == True:
                rooms[i].append(time[0])
                break
        # If a room is empty, add the time slot in the room.
        else:
            rooms[i].append(time[0])
            break
    
    # Remove the element from the time list. 
    time.pop(0)
    
# Call the function, until we remove all the time slots from the list.
while len(time) > 0:
    add_time_in_rooms (time)

count = 0

# Display the time slots for each room.
for i in range (0, len(rooms)):
    if len(rooms[i]) > 0:
        print ("ROOM " + str(i) + ":" + str(rooms[i]))
        count = count + 1

print ("Number of booked rooms: " + str(count))
