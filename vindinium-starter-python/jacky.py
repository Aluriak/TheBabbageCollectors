from random import choice
from game import Game
from bot import Bot 



class JackyBot(Bot):
    """Our Bot !"""

    def __init__(self):
        """Jacky is creat !"""

    def move(self, state):
        """Call at each step of game. Must return a direction choose between ['Stay', 'North', 'South', 'East', 'West'] """
        # INIT
        directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        direction = choice(directions)
        # RETURN
        return direction


    def creatGraph(self, state):
        """Creation of graph of map. Use of Game class in module game
        Initialization of self.graph."""
        self.graph = {} # graph of map




