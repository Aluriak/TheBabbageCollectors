#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import re
from jacky import JackyBot

TIMEOUT=15

def get_new_game_state(server_url, key, mode='training', number_of_turns = 10):
    """Get a JSON from the server containing the current state of the game"""

    if(mode=='training'):
        #Don't pass the 'map' parameter if you want a random map
        params = { 'key': key, 'turns': number_of_turns, 'map': 'm1'}
        api_endpoint = '/api/training'
    elif(mode=='arena'):
        params = { 'key': key}
        api_endpoint = '/api/arena'

    #Wait for 10 minutes
    r = requests.post(server_url + api_endpoint, params, timeout=10*60)

    if(r.status_code == 200):
        return r.json()
    else:
        print("Error when creating the game")
        print(r.text)

def move(url, direction):
    """Send a move to the server
    
    Moves can be one of: 'Stay', 'North', 'South', 'East', 'West' 
    """

    try:
        r = requests.post(url, {'dir': direction}, timeout=TIMEOUT)

        if(r.status_code == 200):
            return r.json()
        else:
            print("Error HTTP %d\n%s\n" % (r.status_code, r.text))
            return {'game': {'finished': True}}
    except requests.exceptions.RequestException as e:
        print(e)
        return {'game': {'finished': True}}


def is_finished(state):
    return state['game']['finished']

def start(server_url, key, mode, turns, bot):
    """Starts a game with all the required parameters"""


    if(mode=='arena'):
        print(u'Connected and waiting for other players to join…')
    # Get the initial state
    state = get_new_game_state(server_url, key, mode, turns)
    print("Playing at: " + state['viewUrl'])
    fd = open("playing", "w")
    fd.write(state['viewUrl'])
    fd.close()

    while not is_finished(state):
        # Some nice output ;)
        sys.stdout.write('.')
        sys.stdout.flush()

        # Move to some direction
        url = state['playUrl']
        direction = bot.move(state)
        state = move(url, direction)


if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print("Usage: %s <key> <[training|arena]> <number-of-games|number-of-turns> <botName> [server-url]" % (sys.argv[0]))
        print('Example: %s mySecretKey training 20 Jacky' % (sys.argv[0]))
    else:
        key = sys.argv[1]
        mode = sys.argv[2]
        botname = sys.argv[4]

        if(mode == "training"):
            number_of_games = 1
            number_of_turns = int(sys.argv[3])
        else: 
            number_of_games = int(sys.argv[3])
            number_of_turns = 300 # Ignored in arena mode

        if(len(sys.argv) == 6):
            server_url = sys.argv[5]
        else:
            server_url = "http://vindinium.jousse.org"

        for i in range(number_of_games):
            bot = JackyBot(botname)
            start(server_url, key, mode, number_of_turns, bot)
            print("\nGame finished: %d/%d" % (i+1, number_of_games))
