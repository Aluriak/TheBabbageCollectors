from random import choice
import time

class Bot:
    pass

class RandomBot(Bot):

    def move(self, state):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)


class FighterBot(Bot):
    def move(self, state):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)



class SlowBot(Bot):
    def move(self, state):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        time.sleep(2)
        return choice(dirs)


class JackyBot(Bot):
    """Our Bot !"""

    def move(self, state):
        """"""
        directions = ['Stay', 'North', 'South', 'East', 'West']
        direction = choice(directions)
        return direction

