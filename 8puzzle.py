"""
-------------------------------------------------------
8puzzle.py
A* algorithm for the 8-puzzle, with heuristics h1 and h2, as
seen in class.
-------------------------------------------------------
CP468
Assignment 1
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alex Francis
__updated__ = "2020-10-06"
-------------------------------------------------------
"""

import utilities
import math
import random

# Table = [[][][],[][][],[][][]]

# table = [[random.sample(fill,3)] for i in range(3)]



# This class represents the 8-puzzle
class Puzzle:

    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '12345678 '
    def __init__(self, size, table):
        self.size = size
        self.table = [[] for i in range(size)]
        for j in range(3):
            while len(table[j])<3:
                temp = random.choice(self.fill)
                if self.checkTable(table, 3, temp) == False:
                    self.table[j].append(temp)
        