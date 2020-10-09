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

goal8 = [['1', '2', '3'],['4', '5', '6'],['7', '8', ' ']]

# This class represents the 8-puzzle


class Puzzle:

    # for x in goal:
    #     print(x)

    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '12345678 '

    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        for j in range(size):
            while len(self.table[j])<size:
                temp = random.choice(self.fill)
                if self.checkTable(self.table, size, temp) == False:
                    self.table[j].append(temp)

        # print(self.table)

    def __eq__(self, table1):
        if self.table == table1:
            return True
        return False

    def printPuzzle(self):
        for i in range(len(self.table)):
            print(self.table[i])

    def h1(self, size, goal):
        count = 0
        for i in range(size):
            for j in range(size):
                if self.table[i][j] != goal[i][j]:
                    count += 1
        return count



class ChildNode:

    puzzleq = utilities.PriorityQueue()

    def __init__(self, table, size):
        self.size = size
        self.table = [[] for i in range(size)]
        # puzzle = Puzzle(size)

    def storePuzzle(self, puzzleq):
        puzzleq.insert(self.table)

    def getNext(self, puzzle, size):
        possible_moves = []
        
        return None
            


print()
puzzle = Puzzle(3)
puzzle.printPuzzle()
print(puzzle.h1(3, goal8))