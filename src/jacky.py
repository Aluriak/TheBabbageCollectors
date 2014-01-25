from graph import Graph
from random import choice
from game import Game
import game
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
            #print self.graph # DEBUG
            self.hero = self.game.getHeroNamed(BOT_JACKY_NAME)
        #directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        finalPath = []
        path = []
        # for each mine
        for key in self.game.mines_locs.iterkeys():
            # if mine is not Jacky's mine
            if self.game.mines_locs[key] != self.hero.id:
                path = self.graph.Dijkstra(self.hero.pos, key)
                if path == None:
                    # No path founded !
                    print 'move: No path founded'
                    return 'Stay'
                if len(finalPath) == 0 or len(path) < len(finalPath) :
                    finalPath = path
        # Get direction of 2nd node in finalPath (2nd node = adjacent neighbor)
        direction = self.directionOf(finalPath[1]) 
        # RETURN
        return direction

    def directionOf(self, neighbor):
        """Return direction of move for go in targeted neighbors"""
        y, x = neighbor
        x = x - self.hero.pos[0]
        y = y - self.hero.pos[1]
        direction = game.AIMreversed[(y,x)]
        print direction
        return direction

    def creatGraph(self, game):
        """Creation of graph of map. Use of Game class
        Initialization of self.graph."""
        self.graph = Graph({}) # graph of map
        
        # For each tile 
        for row in range(len(self.game.board.tiles)):
            for col in range(len(self.game.board.tiles[row])):

                # if tile exist and is praticable
                if self.game.board.exist((row,col)) and self.game.board.notAWall((row,col)):

                    neighbors = []
                    # for each neighbors
                    for coord in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                        # add it only if passable and valable in board
                        if self.game.board.exist(coord) and  self.game.board.notAWall(coord):
                            neighbors.append(coord)

                    # add neighbors as successors
                    self.graph.addSuccTo((row, col), neighbors)
        #print self.graph



    def evalNode(self, node):
        """Return score of Node in self.graph since hero position"""
        return 10





