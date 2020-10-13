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

import math
import random
from copy import deepcopy
from utilities import PriorityQueue, _PQNode

goal8 = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
# This class represents the 8-puzzle
map8 = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]

class Puzzle:

    # for x in goal:
    #     print(x)
    def __getitem__(self, item):
        return self.table[item]

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


    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '012345678'

    def __init__(self,table, size):
        self.size = size

        if (table is None):
            self.table = [[] for i in range(size)]
            for j in range(size):
                while len(self.table[j])<size:
                    temp = int(random.choice(self.fill))
                    if self.checkTable(self.table, size, temp) == False:
                        self.table[j].append(temp)

        else:
            self.table=table

        # print(self.table)

    def __eq__(self, table1):
        if self.table == table1:
            return True
        return False

    def printPuzzle(self):
        for i in range(len(self.table)):
            print(self.table[i])
    def __str__(self):
        # string=""
        # for i in range(self.size):
        #     string+=(self.table[i])
        return str(self.table)


    def h1(self, size):
        count = 0

        for i in range(size):
            for j in range(size):
                #print("this is self table",self.table)
                #print("this is goal8",goal8)
                if self.table[i][j] != goal8[i][j]:
                    count += 1
        return count

    def find_blankspot(self):
        index=[0,0]
        for i in range(self.size):
            for j in range(self.size):
                if (self.table[i][j]==0):
                    index[0]=i
                    index[1]=j
        return index

    def possible_moves(self,index):
        moves=[]
        move=[]
        if ((index[0]+1)<self.size and (index[0]+1)>-1):
            move=[index[0]+1,index[1]]
            moves.append(move)

        if ((index[0]-1)<self.size and (index[0]-1)>-1):
            move=[index[0]-1,index[1]]
            moves.append(move)

        if ((index[1]-1)<self.size and (index[1]-1)>-1):
            move=[index[0],index[1]-1]
            moves.append(move)

        if ((index[1]+1)<self.size and (index[1]+1)>-1):
            move=[index[0],index[1]+1]
            moves.append(move)


        return moves
    def moves(self,moves,blank_spot):
        current_table=deepcopy(self.table)
        blank= blank_spot
        current_number=0
        list_moves=[]

        for c in moves:

            for i in range (self.size):
                for j in range(self.size):
                    if (c[0]==i and c[1]==j):

                        current_number=self.table[i][j]

                        current_table[blank[0]][blank[1]]=current_number

                        current_table[c[0]][c[1]]=0

                        list_moves.append(current_table)
                        current_table=deepcopy(self.table)

        return list_moves



class A_Solver:
        def __init__(self,root,moves,blank_index):

            pq=PriorityQueue()
            node = _PQNode(Puzzle(root,3))
            pq.insert(node)
            # print("is_empty, ",pq.is_empty())
            # v=pq.peek()
            # v.printPuzzle()
            visited=[]
            visited.append(Puzzle(root,3).table)
            print("iterate through")

            for i in pq:
                print(i)
            print("removed")
            # u=pq.remove()
            # print(u._data)

            #u.printPuzzle()
            count=0
            a=pq.is_empty()
            print(a)
            while(pq.is_empty()!=True ):

                u=pq.remove()
                print("is it empty?")
                a=pq.is_empty()
                print(a)
                print("this was removed")
                print(u._data)
                print("value")
                print(u.g)
                print("everthing in the queue currently")
                for i in pq:
                    print(i)
                print()

                print("----------")
                
                #u.printPuzzle()
                
                print("F(g) value")
                #print(u._data.h1(3))
                if u._data==Puzzle(goal8,3):
                    print(u._data,"is the goal")
                    break
                else:
                    blank_index=u._data.find_blankspot()
                    moves=u._data.possible_moves(blank_index)
                    list_moves=u._data.moves(moves,blank_index)
                    for i in (list_moves):
                        if ((Puzzle(i,3)).table not in visited  ):
                            node = _PQNode(Puzzle(i,3),None,u)
                            print("inserted")
                            print(node._data)
                            print("value")
                            print(node.g)
                            pq.insert(node)
                            visited.append(Puzzle(i,3).table)
                count+=1

            return




            



# class ChildNode:

#     #puzzleq = utilities.PriorityQueue()

#     def __init__(self, parent, size):
#         self.size = size
#         self.parent = parent
#         self.parent_table = parent.table
        

#     def storePuzzle(self, puzzleq):
#         puzzleq.insert(self.parent_table)

#     def printPuzzle(self):
#         for i in range(self.size):
#             print(self.parent_table[i])

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
    # this works[[5,2,8],[4,1,7],[0,3,6]]
    #infinite looping [[1,2,5],[4,3,6],[7,8,0]]
    #this works: [[1,2,3],[4,0,6],[7,5,8]]
    # this works[[1,2,3],[0,4,6],[7,5,8]]
    #this works: [[1,2,5],[4,3,6],[8,7,0]]
    #infinite looping [[1,5,8],[3,2,0],[4,6,7]]
    puzzle = Puzzle([[5,2,8],[4,1,7],[0,3,6]],3)
    puzzle.printPuzzle()
    print()
    '''testing blank spot and possible moves'''
    blank_index=puzzle.find_blankspot()
    moves=puzzle.possible_moves(blank_index)
    print("blank index",blank_index)
    print("indices of moves",moves)
    print()
    print("list of moves")
    list_moves=puzzle.moves(moves,blank_index)
    for i in list_moves:
        print(i)
        print()
    
    print()
    puzzle.printPuzzle()
    print()

    A_Solver(puzzle,list_moves,blank_index)


    # print(puzzle.h1(3, goal8))
    #child = ChildNode(puzzle, 3)
    #child.printPuzzle()
    # print(child.around(puzzle, 3))
    #print("Manhattan Distance:", puzzle.manhattan())
    #print("Manhattan Distance:", puzzle.manhattan())



if __name__ == "__main__":
    main()