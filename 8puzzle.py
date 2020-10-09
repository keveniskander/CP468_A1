"""
-------------------------------------------------------
8puzzle.py
A* algorithm for the 8-puzzle, with heuristics h1 and h2, as
seen in class.
-------------------------------------------------------
CP468
Assignment 1
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-10-06"
-------------------------------------------------------
"""

import utilities
import math
import random

goal8 = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
# This class represents the 8-puzzle
map8 = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]


class Puzzle:

    # for x in goal:
    #     print(x)

    def manhattan(self):

        total_distance = 0

        if self.table != goal8:
            for x in range(self.size):
                for y in range(self.size):
                    if self.table[x][y] != goal8[x][y]:
                        a = abs(x - map8[self.table[x][y]][0])
                        b = abs(y - map8[self.table[x][y]][1])
                        total_distance += a + b
                    
        return total_distance

    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '012345678'

    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        for j in range(size):
            while len(self.table[j])<size:
                temp = int(random.choice(self.fill))
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

    def h1(self, size):
        count = 0
        for i in range(size):
            for j in range(size):
                if self.table[i][j] != goal8[i][j]:
                    count += 1
        return count



class ChildNode:

    puzzleq = utilities.PriorityQueue()

    def __init__(self, parent, size):
        self.size = size
        self.parent = parent
        self.parent_table = parent.table
        

    def storePuzzle(self, puzzleq):
        puzzleq.insert(self.parent_table)

    def printPuzzle(self):
        for i in range(self.size):
            print(self.parent_table[i])

    # def around(self, parent, size):
    #     possible_moves = []
    #     blank_index = [0,0]

    #     for i in range(size):
    #         for j in range(size):
    #             if self.table[i][j] == ' ':
    #                 blank_index[0] = i
    #                 blank_index[1] = j
    #                 break
    #     print(blank_index)

    #     return None
            
def main():
    print()
    puzzle = Puzzle(3)
    puzzle.printPuzzle()
    print()
    # print(puzzle.h1(3, goal8))
    child = ChildNode(puzzle, 3)
    child.printPuzzle()
    # print(child.around(puzzle, 3))
    print(puzzle.manhattan())


#TEST
print()

if __name__ == "__main__":
    main()