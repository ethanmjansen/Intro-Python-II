# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    ''' A player class with name, current room'''

    def __init__(self, name, current_room):
        ''' Constructor'''

        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} was added to {self.name}'s inventory.")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"{item.name} was removed from {self.name}'s inventory.")

    def items_in_inventory(self):
        message = ''
        if self.inventory:
            for i in self.inventory:
                message += f'{i.name}: {i.description}\n'
            return message.rstrip('\n')
            
        else:
            return 'nothing'


# if __name__ == '__main__':
