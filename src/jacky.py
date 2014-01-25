from graph import Graph
from random import choice
from game import Game
from bot import Bot 



SCORE_BASE = 10
SCORE_MINE = -10
SCORE_DISTANCE = 1




class JackyBot(Bot):
    """Our Bot !"""

    def __init__(self):
        """Jacky is creat !"""
        self.firstMove = True
        self.game = None # creat by Game class

    def move(self, state):
        """Call at each step of game. Must return a direction choose between ['Stay', 'North', 'South', 'East', 'West'] """
        # INIT
        self.game = Game(state)
        if self.firstMove:
            self.creatGraph(self.game)
            self.firstMove = False
        directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        finalPath = {}
        for key in self.game.mines_locs.iterkeys():
            if self.game.mines_locs[key] != self.id:
                path = shortestPath(self, self.loc, key, path)
                if finalPath.isEmpty() or path.lentgh() < finalPath.length() :
                    finalPath = path
        # Go to this direction
        direction = (finalPath(0)-self.loc(0), finalPath(1)-self.loc(1))
        # RETURN
        return direction


    def creatGraph(self, game):
        """Creation of graph of map. Use of Game class
        Initialization of self.graph."""
        self.graph = Graph({}) # graph of map
        




    def evalNode(self, node):
        """Return score of Node in self.graph since hero position"""
        return 10





