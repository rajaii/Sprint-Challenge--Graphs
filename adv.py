from room import Room
from player import Player
from world import World
from util import Stack, Queue
from traversal_graph import Graph


import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# You may find the commands `player.current_room.id`, 
# `player.current_room.get_exits()` and `player.travel(direction)`
#  useful
gg = Graph()

#travel and append in t_p, create graph and dft on it


# def populate_small_graph():
#     directions = ['w','w','s','s','e','e','n','n','e','e','w','w','n','n','s','e','e','n','s','w','w','w','w','n']
#     gg.add_vertex(player.current_room.id)
#     for i in directions:
#         old_room = player.current_room
#         player.travel(i)
#         traversal_path.append(i)
#         gg.add_vertex(player.current_room.id)
        
#         gg.add_edge(old_room.id, player.current_room.id, old_room, player.current_room)
        
# populate_small_graph()

def populate_big_graph():
    exits = player.current_room.get_exits()
    gg.add_vertex(player.current_room.id, exits)
    prev = None
    backwards_direction = None
    forward_direction = None
    reverse = []
    
    while True:
        cur = player.current_room
        if cur.id not in gg.vertices:
            exits = player.current_room.get_exits()
            gg.add_vertex(player.current_room.id, exits)
        print(f'prev: {prev}, b_d: {backwards_direction}, f_d: {forward_direction}')
        if prev is not None and backwards_direction is not None and forward_direction is not None:
            gg.add_edge(prev.id, cur.id, prev, cur)
            print('inside the if')
        ali = True
        while ali:#current room has exits with ?
            # print('?' in gg.vertices[player.current_room.id].values())
            if '?' in gg.vertices[player.current_room.id].values(): 
                ali = False
            if len(reverse) > 0:
            
                bk = reverse.pop()
                player.travel(bk)
                traversal_path.append(bk)

        for e, v in gg.vertices[cur.id].items():
            print(f'e is {e}')
            if v == '?':
                prev = cur
                backwards_direction = set_opposite_of_dir(e)
                forward_direction = e
                player.travel(e)
                
                # gg.add_edge(prev.id, cur.id, prev, cur)
                reverse.append(backwards_direction)
                traversal_path.append(e)
                break
        
        print(f'vertices: {gg.vertices}')
        
                
        
 


def set_opposite_of_dir(d):
    if d == 's':
        return 'n'
    elif d == 'n':
        return 's'
    elif d == 'w':
        return 'e'
    elif d == 'e':
        return 'w'

    # for e in exits:
    #     old_room = player.current_room
    #     player.travel(e)
    #     if player.current_room.id not in visited:
    #         visited.append()


populate_big_graph()

  

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
