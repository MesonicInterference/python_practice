#!/usr/bin/python3

import sys, getopt
from random import choice

overwatch_heroes = {
    'Genji'         : 'offense',
    'McCree'        : 'offense',
    'Pharah'        : 'offense',
    'Reaper'        : 'offense',
    'Soldier: 76'   : 'offense',
    'Tracer'        : 'offense',
    'Bastion'       : 'defense',
    'Hanzo'         : 'defense',
    'Junkrat'       : 'defense',
    'Mei'           : 'defense',
    'Torbjorn'      : 'defense',
    'Widowmaker'    : 'defense',
    'D.Va'          : 'tank',
    'Reinhardt'     : 'tank',
    'Roadhog'       : 'tank',
    'Winston'       : 'tank',
    'Zarya'         : 'tank',
    'Lucio'         : 'support',
    'Mercy'         : 'support',
    'Symmetra'      : 'support',
    'Zenyatta'      : 'support'}

class Hero(object):
    def __init__(self, choose_role = 'default'):
        self.name = 'default'
        self.role = 'default'
        self.choose_role = choose_role

    def set_name(self, name):
        self.name = name

    def set_role(self, role):
        self.role = role

#   Chooses a random hero, either totally random or within
#   a role determined by an optional argument passed to the Hero class
    def randomize_hero(self):
        if self.choose_role == 'default':
            print('Choosing a random hero.')
            self.name = choice(list(overwatch_heroes.keys()))
            self.role = overwatch_heroes[self.name]
        else:
            print('Choosing a random %s hero.' % (self.choose_role))
            self.set_role(self.choose_role)
            possible_heroes = []
            for hero_name in overwatch_heroes.keys():
                if overwatch_heroes[hero_name] == self.role:
                    possible_heroes.append(hero_name)
            self.name = choice(possible_heroes)

    def hero_info(self):
        print('hero name: %s' % (self.name))
        print('hero role: %s' % (self.role))


def main(argv):
    if argv != []:
        selected_role = argv[0].lower()
    else:
        selected_role = 'default'

    if selected_role == '-h' or selected_role == '-help' or selected_role == '--help':
        print("========================================================")
        print("Provides a random Overwatch hero.")
        print("")
        print("Run with no argument to get a fully")
        print("random hero or provide one of the following")
        print("roles to get a random hero within that role:")
        print("   > offense")
        print("   > defense")
        print("   > tank")
        print("   > support")
        print("========================================================")
        quit()


    if selected_role != 'offense' and \
        selected_role != 'defense' and \
        selected_role != 'tank' and \
        selected_role != 'support' and \
        selected_role != 'default':
            print("Run this program without an argument or enter a valid role.")
            quit()

    random_hero = Hero(selected_role)
    random_hero.randomize_hero()
    random_hero.hero_info()

if __name__ == '__main__':
    main(sys.argv[1:])