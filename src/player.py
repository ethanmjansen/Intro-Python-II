# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    ''' A player class with name, current room and items'''

    def __init__(self, name, current_room):
        ''' Constructor'''

        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'


if __name__ == '__main__':

    player = Player(name='Ethan', current_room='Outside')
    print(player) 