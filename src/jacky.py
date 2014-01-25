from graph import Graph
from random import choice
from game import Game
from bot import Bot 


BOT_JACKY_NAME = 'Jacky'
SCORE_BASE = 10
SCORE_MINE = -10
SCORE_DISTANCE = 1




class JackyBot(Bot):
    """Our Bot !"""

    def __init__(self):
        """Jacky is creat !"""
        self.firstMove = True
        self.game = None # creat by Game class
        self.hero = None

    def move(self, state):
        """Call at each step of game. Must return a direction choose between ['Stay', 'North', 'South', 'East', 'West'] """
        # INIT
        self.game = Game(state)
        if self.firstMove:
            self.creatGraph(self.game)
            self.firstMove = False
            print self.graph # DEBUG
            self.hero = self.game.getHeroNamed(BOT_JACKY_NAME)
        #directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        finalPath = []
        path = []
        for key in self.game.mines_locs.iterkeys():
            if self.game.mines_locs[key] != self.hero.id:
                path = self.graph.shortestPath(self.hero.pos, key)
                if path == None:
                    # No path founded !
                    return 'Stay'
                if len(finalPath) == 0 or len(path) < len(finalPath) :
                    finalPath = path
        # Go to this direction
        direction = (finalPath(0)-self.loc(0), finalPath(1)-self.loc(1))
        # RETURN
        return direction


    def creatGraph(self, game):
        """Creation of graph of map. Use of Game class
        Initialization of self.graph."""
        self.graph = Graph({}) # graph of map
        
        # For each tile (not next to the border of world)
        for row in range(1, len(self.game.board.tiles)-1):
            for col in range(1, len(self.game.board.tiles[row])-1):

                neighbors = []
                # for each neighbors
                for coord in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                    # add it only if passable 
                    if self.game.board.passable(coord):
                        neighbors.append(coord)

                # add neighbors as successors
                self.graph.addSuccTo((row, col), neighbors)




    def evalNode(self, node):
        """Return score of Node in self.graph since hero position"""
        return 10





