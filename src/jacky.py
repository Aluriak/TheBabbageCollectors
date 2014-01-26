# -*- encoding: utf-8 -*-
from graph import Graph
from valuateGraph import ValuateGraph
from random import choice
from game import Game
import game
from bot import Bot 


BOT_JACKY_NAME = 'Jacky'
BOT_WILSON_NAME = 'Wilson'
SCORE_BASE = 10
SCORE_MINE = -10
SCORE_DISTANCE = 1

HERO_LIMIT_LIFE_PERIL = 42


INTEREST_MINE = 50
NON_INTEREST_MINE = 1000
INTEREST_LOWER = 500
INTEREST_MEDIUM = 200
INTEREST_HIGH = 150
INTEREST_VERY_HIGH = 100
INTEREST_HIGHER = 70
NON_INTEREST_HERO = 1000
INTEREST_INN = 1
NON_INTEREST_INN = 1000



class JackyBot(Bot):
    """Our Bot !"""

    def __init__(self, name = BOT_JACKY_NAME):
        """Jacky is creat !"""
        self.firstMove = True
        self.game = None # creat by Game class
        self.hero = None
        self.name = name

    def move(self, state):
        """Call at each step of game. Must return a direction choose between ['Stay', 'North', 'South', 'East', 'West'] """
        # INIT
        self.game = Game(state)
        self.hero = self.game.getHeroNamed(self.name)
        if self.firstMove:
            self.creatGraph(self.game)
            self.firstMove = False
        #directions = ['Stay', 'North', 'South', 'East', 'West']
        # CHOOSE A DIRECTION
        finalPath = []
        finalEvaluation = -1
        path = []
        targets = []
        # définitions des cibles
        # Tarvernes
        if self.hero.life < HERO_LIMIT_LIFE_PERIL:
            for tvrn in self.game.taverns_locs:
                targets.append(tvrn)

        # Mines
        for mine in self.game.mines_locs.iterkeys():
            if self.game.mines_locs[mine] != self.hero.id:
                targets.append(mine)

        # Heros
        for hero in self.game.heroes:
            if hero.id != self.hero.id:
                targets.append(hero.pos)
        # Choix de cible 
        #print "targets: "+str(targets)
        for target in targets:
            #print self.hero.pos, target
            path, evaluation = self.graph.Dijkstra(self.hero.pos, target)
            # On garde le + petit
            if finalEvaluation == -1 or evaluation < finalEvaluation:
                finalPath = path
                finalEvaluation = evaluation
                #print finalPath
        #print "\n\n\n"


        # Get direction of 2nd node in finalPath (2nd node = adjacent neighbor)
        if len(finalPath) > 1:  direction = self.directionOf(finalPath[1]) 
        else:                   direction = 'Stay'
        print self.hero
        print "FINAL = "+str(finalPath)
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
        #self.graph = Graph({}) # graph of map
        self.graph = ValuateGraph({}, self) # graph of map

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
        """Function that evaluate nodes of the graph. Wait a node.
        Seek if the node is a mine, a tavern, a hero or none. The more a node will give golds(or HP if in need), 
        the more interest will be set as a return of the function."""
        ponderation = 0
        coord = node
        y, x = coord
        node = self.game.board.tiles[y][x]
        # Si une mine nous appartient elle n'est pas intéressante
        if isinstance(node, game.MineTile):
            if str(self.game.mines_locs[coord]) == self.hero.id:
                ponderation = NON_INTEREST_MINE
            else:
                ponderation = INTEREST_MINE
        # Si nous ne sommes pas en péril la taverne n'est pas intéressante
        elif node == game.TAVERN:
            if self.hero.life > HERO_LIMIT_LIFE_PERIL:
                ponderation = NON_INTEREST_INN
                # Si nous sommes en péril la terverne prend des airs de paradis
            else:
                ponderation = INTEREST_INN
        # Si le hero est plus faible que nous il est intéressant suivant son nombre de mine
        elif isinstance(node, game.HeroTile):
            idHero = self.game.heroes_locs[coord]
            if self.game.getHeroWithId(idHero).life < self.hero.life:
                nbMines = 0
                for key in self.game.mines_locs.iterkeys():
                    if self.game.mines_locs[key] == self.game.heroes_locs[coord]: nbMines += 1
                if   nbMines == 0: ponderation = INTEREST_LOWER
                elif nbMines == 1: ponderation = INTEREST_MEDIUM
                elif nbMines == 2: ponderation = INTEREST_HIGH
                elif nbMines == 3: ponderation = INTEREST_VERY_HIGH
                elif nbMines >= 4: ponderation = INTEREST_HIGHER
        # Si le hero est plus fort que nous c'est loin d'être une bonne idée d'aller lui dire bonjour
            else:
                ponderation = NON_INTEREST_HERO
        return ponderation




