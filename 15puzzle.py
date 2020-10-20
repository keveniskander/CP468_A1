"""
-------------------------------------------------------
15puzzle.py
A* algorithm for the 15-puzzle, with heuristics h1 and h2, as
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
from utilities import _PQNode, PriorityQueue, SortedList
from random import shuffle

goal15 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 0]]
# This class represents the 8-puzzle
map15 = [[3,3], [0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2]]

class Puzzle:

    table = None
    size = 0
    id = -1

    def __init__(self, table, size):
        self.size = size
        self.table=table
        self.id = hash(str(self.table))


    def __getitem__(self, item):
        return self.table[item]

    def manhattan(self):

        total_distance = 0

        if self.table != goal15:
            for x in range(self.size):
                for y in range(self.size):
                    if self.table[x][y] != goal15[x][y]:
                        
                        a = abs(x - map15[self.table[x][y]][0])
                        b = abs(y - map15[self.table[x][y]][1])
                        
                        total_distance += a + b
                        
                    
        return total_distance

    def tileAt(self, row, col):
        tile = self.table[row-1][col-1]
        return tile
    
    def matrixToList(self):
        new_list = [j for sub in self.table for j in sub]
        return new_list

    def findEmpty(self):
        new_list = self.matrixToList()
        count = 0
        rcount = 4
        for i in range(len(new_list)):
            if count == 4:
                count = 0
                rcount -= 1
            if new_list[i] == 0:
                row = rcount
            count += 1
        return row

    def isSolvable(self):
        new_list = self.matrixToList()
        row = self.findEmpty()
        count = 0
        for i in range(len(new_list) -1):
            for j in range(i+1, len(new_list)):
                if(new_list[j] > 0 and new_list[j] and new_list[i] and new_list[i] > new_list[j]):
                    count += 1
        if (row % 2 == 0 and count % 2 != 0):
            ans = True
        elif (row % 2 != 0 and count % 2 == 0):
            ans = True
        else:
            ans = False
        return ans
    

    def checkTable(self, table, size, key):
        for i in range(size):
            if key in table[i]:
                return True
        return False

    fill = '0123456789'

    

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


    def h1(self):
        count = 0

        for i in range(self.size):
            for j in range(self.size):
                #print("this is self table",self.table)
                #print("this is goal15",goal15)
                if self.table[i][j] != goal15[i][j] and self.table[i][j]!=0:
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

    def shuffle_moves(self,moves,blank_spot):
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

            puzzle = random.choice(list_moves)
            
            return puzzle

    def shuffle(self):
        for _ in range(100):
            blank_index=self.find_blankspot()
            moves=self.possible_moves(blank_index)
            puzzle = self.shuffle_moves(moves,blank_index)
            self.table = puzzle
        return puzzle
    """
    -------------------------------------------------------
    Calculates heuristic 3 for 8-puzzle
    Use: Puzzlenode.h3()
    -------------------------------------------------------
    Postconditions:
        Returns total_distance traveled by nodes
    -------------------------------------------------------
    """

    def h3(self):

        return (self.h1()+self.manhattan())




"""
-------------------------------------------------------
Solver function to find viable solution
Use: solve(root, heuristic)
-------------------------------------------------------
Preconditions:
        root - Puzzle
        heuristic - int {1, 2, 3}
Postconditions:
    Solves 8-puzzle problem and prints confirmation
    if solved. 
-------------------------------------------------------
"""


def solve(root, heuristic):

    pq=PriorityQueue()
    node = _PQNode(Puzzle(root,4),None,None, heuristic)
    pq.insert(node)

    visited = SortedList(None)

    count=0
    expanded=0

    while(pq.is_empty()!=True ):
        expanded+=1
        u=pq.remove()
        visited.insert(u._id)
        #print(u._id)

        if u._data==Puzzle(goal15,4):
            goal_node=u
            break

        else:


            blank_index=u._data.find_blankspot()
            moves=u._data.possible_moves(blank_index)
            list_moves=u._data.moves(moves,blank_index)
        

            for i in (list_moves):
                node = _PQNode(Puzzle(i,4),None,u,heuristic)

                #if node._id in visited._values:
                if visited._binary_search(node._id) != -1:
                    continue
                new=u.g+1
                
                if (node not in pq  or new<node.g):
                    node.parent=u
                    node.g=new

                    if node not in pq:
                     pq.insert(node)

        count+=1
    #find the number of moves
    
    current=goal_node
    path=[]
    move_count=0
    while(current.parent!=None):

        current=current.parent
        path.append(current)
        move_count+=1

    #print('# of steps to find solution: ', move_count)
    #print('# of nodes expanded: ', expanded)

    return move_count, expanded


"""
-------------------------------------------------------
Initializes main class
-------------------------------------------------------
Postconditions:
    Prints 100 randomly generated 8-puzzles by calling
    A_Solver to solve them. 
-------------------------------------------------------
"""   

def gen1():
    puzzle_list = []

    while len(puzzle_list) < 100:
        n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        shuffle(n)
        p = [[], [], [], []]

        x = 0
        while len(n) != 0:
            p[(x+1) % 4].append(n.pop())
            x += 1

        puzzle = Puzzle(p, 4)
        if puzzle not in puzzle_list and puzzle.manhattan() < 24 and puzzle.isSolvable():
            puzzle_list.append(puzzle)
            
    return puzzle_list
            
def main():

    # p = Puzzle([[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]], 4)
    # s, n = solve(p, 3)

    # print('steps', s)
    # print('expanded', n)

    # arr = [2, 3, 4, 10, 40] 
    # v = SortedList(arr)

    # v.insert(5)
    # print(v._values)
    # print(v._binary_search(7))
    
    # a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    # u = Puzzle(a, 4)
    # q = _PQNode(u)
    # print(q._id)

    q = gen1()

    for x in q:
        s, n = solve(x, 3)
        print("steps:   {}      nodes:  {}".format(s, n))
        print("-----")









    # for x in q:
    #     print(x.table)

    # steps = []
    # nodes = []
    # steps2 = []
    # nodes2 = []
    # steps3 = []
    # nodes3 = []

    # print('TESTING FOR 15-PUZZLE')
    # print('='*90)
    # print("|{:10}|{:35}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|".format("Puzzle", "", "h1s", "h1n", "h2s", "h2n", "h3s", "h3n"))
    # print('-'*90)
    # counter=0
    # while(counter<100):
    #     puzzle=q[counter]

    #     if (puzzle.isSolvable()):

    #         s, n = solve(puzzle, 1)
    #         s2, n2 = solve(puzzle, 2)
    #         s3, n3 = solve(puzzle, 3)

    #         steps.append(s)
    #         nodes.append(n)
    #         steps2.append(s2)
    #         nodes2.append(n2)
    #         steps3.append(s3)
    #         nodes3.append(n3)

    #         print("|P{:<9}| {} |{:>6}|{:>6}|{:>6}|{:>6}|{:>6}|{:>6}|".format(counter+1, puzzle.table, s, n, s2, n2, s3, n3))
            
    #         counter+=1

    #         print('-'*90)

    # anodes = sum(nodes) / len(nodes)
    # asteps = sum(steps) / len(steps)
    # anodes2 = sum(nodes2) / len(nodes2)
    # asteps2 = sum(steps2) / len(steps2)
    # anodes3 = sum(nodes3) / len(nodes3)
    # asteps3 = sum(steps3) / len(steps3)
    
    # print()
    # print("-~ SUMMARY OF AVERAGES ~-")
    # print("h1 steps:  ", asteps)
    # print("h1 nodes:  ", anodes)
    # print("h2 steps:  ", asteps2)
    # print("h2 nodes:  ", anodes2)
    # print("h3 steps:  ", asteps3)
    # print("h3 nodes:  ", anodes3)


if __name__ == "__main__":
    main()