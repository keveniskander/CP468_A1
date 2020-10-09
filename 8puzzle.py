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

# This class represents the 8-puzzle
class Puzzle:

    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '12345678 '

    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        for j in range(3):
            while len(self.table[j])<3:
                temp = random.choice(self.fill)
                if self.checkTable(self.table, 3, temp) == False:
                    self.table[j].append(temp)

        # print(self.table)

    def __eq__(self, table1):
        if self.table == table1:
            return True
        return False

    def printPuzzle(self):
        for i in range(len(self.table)):
            print(self.table[i])

puzzle = Puzzle(3)
puzzle.printPuzzle()
        