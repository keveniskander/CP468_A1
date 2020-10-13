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
from copy import deepcopy

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
                        print("x:      {}       y:    {}".format(x, y))
                        print("puzzle: {}       goal: {}".format(self.table[x][y], goal8[x][y]))
                        a = abs(x - map8[self.table[x][y]][0])
                        b = abs(y - map8[self.table[x][y]][1])
                        print("d1:     {}       d2:   {}".format(a, b))
                        total_distance += a + b
                        print("----------------")
                        print("movement needed:      {}".format(a+b))
                        print()
                    
        return total_distance

    def tileAt(self, row, col):
        tile = self.table[row-1][col-1]
        return tile
    
    def matrixToList(self):
        new_list = [j for sub in self.table for j in sub]
        return new_list
    
    def isSolvable(self):
        new_list = self.matrixToList()

        count = 0
        for i in range(len(new_list) -1):
            for j in range(i+1, len(new_list)):
                if(new_list[j] and new_list[i] and new_list[i] > new_list[j]):
                    count += 1
        if (count % 2 == 0):
            ans = True
        else:
            ans = False
        return ans


    def checkTable(self, table, key):
        for i in range(self.size):
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
                if self.checkTable(self.table, temp) == False:
                    self.table[j].append(temp)

        # print(self.table)

    def __eq__(self, table1):
        if self.table == table1:
            return True
        return False

    def printPuzzle(self):
        for i in range(len(self.table)):
            print(self.table[i])

    def h1(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
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

    def findParentBlank(self):
        blank_position = [0,0]
        for i in range(self.size):
            for j in range(self.size):
                if self.parent_table[i][j] == 0:
                    blank_position = [i,j]
                    return blank_position
        return blank_position


    def makeBabies(self):   
        blank_position = self.findParentBlank()
        babies = []
        i=0

        # first we figure out what moves we can make from 0 (up, down, left or right)
        possible_values = [[blank_position[0], blank_position[1]+1], [blank_position[0], blank_position[1]-1],
            [blank_position[0]-1, blank_position[1]], [blank_position[0]+1, blank_position[1]]]

        while i< len(possible_values):
            if not (0 <= possible_values[i][0] < 3 and 0 <= possible_values[i][1] < 3):
                possible_values.pop(i)
            
            i+=1

        # now possible_values returns a list of the indices of possible squares that the blank square (or 0) can travel to

        # next we need swap function working to make children puzzles by swapping indices and see which has bes manhattan score
    
        self.printPuzzle()
        copy = deepcopy(self)
        print()
        new = copy.swap(blank_position[0], blank_position[1], possible_values[0][0], possible_values[0][1])
        print(new)
        

        return possible_values

    def swap(self, x, y, sx, sy):
        # swaps space (or 0 value) in puzzle for either top, bottom, left or right value.
        # top, bottom, left and right values are determined in makeBabies function

        temp = self.parent_table
        temp[x][y] = self.parent_table[sx][sy]
        temp[sx][sy] = 0
        
        return temp
        
        

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
    #print()
    puzzle = Puzzle(3)
    puzzle.printPuzzle()
    print()
    # print(puzzle.h1(3, goal8))
    child = ChildNode(puzzle, 3)
    #child.printPuzzle()
    # print(child.around(puzzle, 3))
    print("Manhattan Distance:", puzzle.manhattan())
    print("list: ", puzzle.matrixToList())
    print("Is puzzle solvable:", puzzle.isSolvable())
    # up, down, left, right
    print(child.makeBabies())


if __name__ == "__main__":
    main()