from random import choice
from bot import Bot 



class JackyBot(Bot):
    """Our Bot !"""

    def __init__(self):
        """"""

    def move(self, state):
        """"""
        directions = ['Stay', 'North', 'South', 'East', 'West']
        direction = choice(directions)
        return direction


    def creatGraph(self, state):
        pass



