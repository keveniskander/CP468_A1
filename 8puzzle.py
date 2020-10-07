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

# This class represents the 8-puzzle

# Table = [[][][],[][][],[][][]]

class Puzzle:

    fill = '0123456789 '
    def __init__(self, size, table):
        self.size = size
        self.table = [[] for i in range(size)]
        