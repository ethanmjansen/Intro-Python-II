# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    ''' A room class that a player can interact with'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

    def __str__(self):
        return f'{self.name}.\n{self.description}'

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def items_in_room(self):
        message = ''
        if self.inventory:
            for i in self.inventory:
                message += f'{i.name}, '
            return message.rstrip(', ')

        else:
            return 'nothing'

# if __name__ == '__main__':
