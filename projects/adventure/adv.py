from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

def oppositeDirection(direction):
    if direction == 'n':
        opposite = 's'
    elif direction == 's':
        opposite = 'n'
    elif direction == 'e':
        opposite = 'w'
    elif direction == 'w':
        opposite = 'e'
    return opposite

# traversal graph to track visited room and their direction
traversal_graph = {}
for i in range(len(room_graph)):
    traversal_graph[i] = {'n': '?', 's':'?', 'e':'?', 'w':'?'}

# traversal path to track directions
traversal_path = []

# Create a Dictionary of visited (previously seen) rooms
visited = set()
visited.add(player.current_room)

current_room = player.current_room
previous_room = current_room

# tracking return path to last room with unexplored exits
stack = Stack()

backTracking = False

# checking avaiable exits
def check_exits(exits):
    # allowing backtracking to be modify  globally 
    global backTracking
    # taking the players current room number
    room = player.current_room.name.split(' ')
    index = int(room[1])
    available_paths = []
    # find all unknown paths
    for exit in exits:
        # if the exit is unknown, add onto available paths to explore
        if traversal_graph[index][exit] == '?':
            available_paths.append(exit)
    # if there is nothing in the available path
    if len(available_paths) == 0:
        backTracking = True
        return stack.pop()
    # if backtracking
    if backTracking:
        for path in available_paths:
            if path:
                backTracking = False
                return path
            else:
                backTracking = True
                return stack.pop()
    # else not backtracking
    else:
        if len(traversal_path) != 0:
            if player.current_room not in visited:
                for path in available_paths:
                    if traversal_graph[index][path] != oppositeDirection(traversal_path[-1]):
                        backTracking = False
                        return path
            # if current_room is in visited set, backtrack around
            else:
                backTracking = True
                return stack.pop()
        # if not in traversal path, this means we're still at the start
        else:
            for path in available_paths:
                backTracking = False
                return path
                
# when visiting room
def visitRoom(room):
    # if previous room not in visited
    if previous_room not in visited:
        # add it to the set
        visited.add(previous_room)
    # taking the previous room number/name since current room 
    previous_room_split = previous_room.name.split(' ')
    previous_index = int(previous_room_split[1])

    # taking the current room number/name
    current_room_split = room.name.split(' ')
    currentIndex = int(current_room_split[1])
    # the last direction is the end of the traversal path
    # this will add the last viisted room in the traversal path the traversal graph as current room
    last_direction = traversal_path[-1]

    # connecting the two rooms together, adding both current path and reversed path to traversal graph
    traversal_graph[previous_index][last_direction] = room
    traversal_graph[currentIndex][oppositeDirection(last_direction)] = previous_room

# when the len of the visited set does not equal the room graph
while len(visited) != len(room_graph):
    # player starting in the current room
    current_room = player.current_room
    # taking the room number/name
    room_split = current_room.name.split(' ')
    index = int(room_split[1])
    # taking all exits in the current room
    current_exits = current_room.get_exits()
    # when player moves
    travel_direction = check_exits(current_exits)
    if travel_direction is not None:
        # add the directions the player travel to traversal path
        traversal_path.append(travel_direction) 
        # tracking the path to the last room that still have unvisted exits/rooms
        if not backTracking:
            stack.push(oppositeDirection(travel_direction))

    previous_room = current_room
    # player to move to travel direction
    player.travel(travel_direction)
    # player to vist next room
    visitRoom(player.current_room)

print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
