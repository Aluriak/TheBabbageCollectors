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


INTEREST_BASE = 25
INTEREST_MINE = -10
NON_INTEREST_MINE = 500
INTEREST_LOWER = 25
INTEREST_HIGHER = -25
INTEREST_FEW_HIGH = -10
INTEREST_HIGH = -15
INTEREST_VERY_HIGH = -20
NON_INTEREST_HERO = 500
INTEREST_INN = -25
NON_INTEREST_INN = 500



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
        self.hero = self.game.getHeroNamed(BOT_JACKY_NAME)
        if self.firstMove:
            self.creatGraph(self.game)
            self.firstMove = False
        #directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        finalPath = []
        path = []
        # Choix de cible -----> je suis français et je vous emmerde
        if self.hero.life > 50:

            for key in self.game.mines_locs.iterkeys():
                idOwner = self.game.mines_locs[key]
                if idOwner != self.hero.id:
                    path = self.graph.Dijkstra(self.hero.pos, key)
                    if len(finalPath) == 0 or len(path) < len(finalPath):
                        finalPath = path

        else:
            for key in self.game.taverns_locs.iterkeys():
                path = self.graph.Dijkstra(self, self.hero.pos, key)
                if len(finalPath) == 0 or len(path) < len(finalPath):
                    finalPath = path
        # Get direction of 2nd node in finalPath (2nd node = adjacent neighbor)
        direction = self.directionOf(finalPath[1]) 
        print self.hero
        # RETURN
        return direction

    def directionOf(self, neighbor):
        """Return direction of move to go to targeted neighbors"""
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
                    if self.game.board.passable((row,col)):
                        # for each neighbors
                        for coord in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                            # add it only if passable and valable in board
                            if self.game.board.exist(coord) and  self.game.board.notAWall(coord):
                                neighbors.append(coord)

                    # add neighbors as successors
                    self.graph.addSuccTo((row, col), neighbors)
        #print self.graph



    def evalNode(self, node):
        """Function that evaluate nodes of the graph. Wait a node.
        Seek if the node is a mine, a tavern, a hero or none. The more a node will give golds(or HP if in need), 
        the more interest will be set as a return of the function."""
        # Si une mine nous appartient elle n'est pas intéressante
        ponderation = INTEREST_BASE
        # Si une mine nous appartient elle n'est pas intéressante
        if isinstance(node, MineTile) and self.game.mines_locs[node] == self.hero.id:
            ponderation += NON_INTEREST_MINE
        # Si une mine ne nous appartient pas elle est intéressante
        if isinstance(node, MineTile) and self.game.mines_locs[node] != self.hero.id:
            ponderation += INTEREST_MINE
        # Si le hero est plus faible que nous il est intéressant suivant son nombre de mine
        if isinstance(node, HeroTile) and self.game.heroes_locs[node].life < self.hero.life:
            nbMines = 0
            for key in self.game.mines_locs.iterkeys():
                if self.game.mines_locs[key] == self.game.heroes_locs[node]: nbMines += 1
            if nbMines == 0: ponderation += INTEREST_LOWER
            if nbMines == 1: ponderation += INTEREST_FEW_HIGH
            if nbMines == 2: ponderation += INTEREST_HIGH
            if nbMines == 3: ponderation += INTEREST_VERY_HIGH
            if nbMines == 4: ponderation += INTEREST_HIGHER
        # Si le hero est plus fort que nous c'est loin d'être une bonne idée d'aller lui dire bonjour
        if isinstance(node, HeroTile) and self.game.heroes_locs[node].life >= self.hero.life:
            ponderation += NON_INTEREST_HERO
        # Si nous ne sommes pas en péril la taverne n'est pas intéressante
        if self.hero.life > 50 and node in self.game.taverns_locs:
            ponderation += NON_INTEREST_INN
        # Si nous sommes en péril la terverne prend des airs de paradis
        if self.hero.life < 50 and node in self.game.taverns_locs:
            ponderation += INTEREST_INN
        return ponderation




