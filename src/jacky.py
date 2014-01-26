# -*- encoding: utf-8 -*-
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
        yn, xn = neighbor
        yh, xh = self.hero.pos
        x = xn - xh
        y = yn - yh
        direction = game.AIMreversed[(y,x)]
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
        # Si une mine nous appartient elle n'est pas intéressante
        if isinstance(node, MineTile) and self.game.mines_locs[node] == self.hero.id:
            return 15
        # Si une mine ne nous appartient pas elle est intéressante
        if isinstance(node, MineTile) and self.game.mines_locs[node] != self.hero.id:
            return -10
        # Si le hero est plus faible que nous il est intéressant suivant son nombre de mine
        if isinstance(node, HeroTile) and self.game.heroes_locs[node].life < self.hero.life:
            nbMines = 0
            for key in self.game.mines_locs.iterkeys():
                if self.game.mines_locs[key] == self.game.heroes_locs[node]: nbMines += 1
            if nbMibes == 0: return 25
            if nbMines == 1: return -10
            if nbMines == 2: return -15
            if nbMines == 3: return -20
            if nbMines == 4: return -25
        # Si le hero est plus fort que nous c'est loin d'être une bonne idée d'aller lui dire bonjour
        if isinstance(node, HeroTile) and self.game.heroes_locs[node].life >= self.hero.life:
            return 25
        # Si nous ne sommes pas en péril la taverne n'est pas intéressant
        if self.hero.life > 50 and node in self.game.taverns_locs:
            return 25
        # Si nous sommes en péril la terverne prend des airs de paradis
        if self.hero.life < 50 and node in self.game.taverns_locs:
            return -25
        return 1




