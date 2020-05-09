# Implement a class to hold item information. This should have name and
# description attributes.

class Item:
    """ Abstract representation of an item"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}:\n{self.description}'

if __name__ == '__main__':
    item = Item('Goose', "Goose that lays golden eggs!")
    print(item)


