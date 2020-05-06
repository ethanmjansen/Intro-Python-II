# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    ''' A room class that a player can interact with'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
 

    def __str__(self):
        return f'{self.name}.\n{self.description}'       
