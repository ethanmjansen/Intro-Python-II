# Classes
from room import Room
from player import Player
from item import Item

# Utility func to clear screen on all platforms
from utils import clear_terminal

import sys


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons..."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
    'goose': Item("A goose", "A goose that lays golden eggs!"),
    
    'sword': Item("A sword", "Don't hold on to the wrong end."),

    'lantern': Item("A lantern", "Shines light in dark places."),

    'nothing': Item("nothing", "Something to represent nothing.")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].add_item(item['sword'])
room['treasure'].add_item(item['goose'])
room['overlook'].add_item(item['lantern'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Clear screen in preparation for game
clear_terminal()

print(
"""
      /| ________________
O|===|* >________________>
      \|  Text Adventure
	       By: Ethan Jansen
"""
)

print('Welcome Adventurer!')
player_name = input('Please enter your name: ')
player = Player(name=player_name, current_room=room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

location = f"""\nYou find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground."""

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Clear screen in preparation for game
clear_terminal()

print(
    f"""Welcome {player.name}! You find yourself at the {player.current_room}"""
)

while True:

    selection = input(
        """
Please pick a direction, action, or view your intventory:
North(n) South(s) East(e) West(w)
Take item(take [name]) Drop item(drop [name])
View inventory(i)
Quit(q).
--> """
    )

    if selection == 'q':
        clear_terminal()
        print(f'Thank you for playing {player.name}!\nUntil next time...')
        break
    
    selection = selection.strip().split()

    if selection[0] in ('n','s','e','w'):
        clear_terminal()
                    
        if hasattr(player.current_room, f'{selection[0]}_to'):
            player.current_room = getattr(player.current_room, f'{selection[0]}_to')
            print(player)

    elif selection[0] in ('take'):
        clear_terminal()
        for item in player.current_room.inventory:
            if selection[1] in item.name:
                player.add_item(item)
                player.current_room.remove_item(item)
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

            else:
                print(f'\n{selection[1]} not in room.')
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

    elif selection[0] in ('drop', 'd'):
        clear_terminal()
        for item in player.inventory:
            if selection[1] in item.name:
                player.drop_item(item)
                player.current_room.add_item(item)
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

            else:
                clear_terminal()
                print(f'\n{selection[1]} not in inventory')
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

    elif selection[0] in ('i', 'inventory'):
        clear_terminal()
        print(f"\n{player.name}'s inventory:\n{player.items_in_inventory()}")

    else:
        clear_terminal()
        print(f"""That is not a valid command\n
You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")
