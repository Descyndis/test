"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia.contrib.rpsystem import ContribRPCharacter


class Character(ContribRPCharacter):
    # [...]
    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character
        generation step instead.
        """
        super().at_object_creation()
        #set persistent attributes
        self.db.strength = 5
        self.db.agility = 4
        self.db.magic = 2

    def get_abilities(self):
        """
        Simple access method to return ability
        scores as a tuple (str,agi,mag)
        """
        return self.db.strength, self.db.agility, self.db.magic

    pass
