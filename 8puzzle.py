"""
-------------------------------------------------------
8puzzle.py
A* algorithm for the 8-puzzle, with heuristics h1, h2
and h3, as seen in class.
-------------------------------------------------------
CP468
Assignment 1
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-10-19"
-------------------------------------------------------
"""

import math
import random
from copy import deepcopy
from utilities import _PQNode, PriorityQueue

# Global variables representing goal for 8-puzzle and mapping of indexes for the goal state
goal8 = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
map8 = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]


"""
-------------------------------------------------------
Initializes Puzzle class
Use: puzzle = Puzzle(table, size)
-------------------------------------------------------
Preconditions:
        table - 8-puzzle table as a 2d array
        if table = None, random 8-puzzle generated
        size - int
Postconditions:
    Initializes a Puzzle class that contains a 3x3
    8-puzzle
-------------------------------------------------------
"""


class Puzzle:

    # returns specific item 
    def __getitem__(self, item):
        return self.table[item]

    """
    -------------------------------------------------------
    Calculates heuristic 2 for 8-puzzle (aka manhattan)
    Use: Puzzle.manhattan()
    -------------------------------------------------------
    Postconditions:
        Returns total_distance traveled by nodes
    -------------------------------------------------------
    """
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

    """
    -------------------------------------------------------
    Determines tile value at index [x,y]
    Use: Puzzle.tileAt(row, col)
    -------------------------------------------------------
    Preconditions:
            Puzzle object
            int(row)
            int(col)
    Postconditions:
        Returns tile at position in specified 8-puzzle
    -------------------------------------------------------
    """

    def tileAt(self, row, col):
        # return index of blank tile 
        tile = self.table[row-1][col-1]
        return tile

    """
    -------------------------------------------------------
    Converts 2d matrix to 1d list
    Use: Puzzle.matrixToList
    -------------------------------------------------------
    Postconditions:
        Returns flat 1 dimensional list
    -------------------------------------------------------
    """
    
    def matrixToList(self):
        # converts 2d matrix to 1d list
        new_list = [j for sub in self.table for j in sub]
        return new_list
        
    """
    -------------------------------------------------------
    Determines if 8-puzzle is solvable
    Use: Puzzle.isSolvable
    -------------------------------------------------------
    Postconditions:
        Returns True if solvable, False otherwise
    -------------------------------------------------------
    """

    def isSolvable(self):
        # check if generated 8-puzzle is solvable
        new_list = self.matrixToList()

        count = 0
        for i in range(len(new_list) -1):
            for j in range(i+1, len(new_list)):
                if(new_list[j] and new_list[i] and new_list[i] > new_list[j]):
                    count += 1

        # if number of inversions is even, 8-puzzle is solvable
        if (count % 2 == 0):
            ans = True
        else:
            ans = False
        return ans

    """
    -------------------------------------------------------
    Checks puzzle elements to determine if specific element
    is already in puzzle
    Use: Puzzle.checkTable(table, size, key)
    -------------------------------------------------------
    Preconditions:
            table - list (2D)
            size - int
            key - int
    Postconditions:
        Returns True if element found, False otherwise
    -------------------------------------------------------
    """
    
    def checkTable(self, table, size, key):
        # checks puzzle elements to determine if specific element is already in puzzle
        # used to generate random puzzle and ensures no two elements repeat
        for i in range(size):
            if key in table[i]:
                return True
        return False

    # global variable fill, used to fill puzzle with random values in string

    fill = '012345678'

    """
    -------------------------------------------------------
    Initializes Puzzle object
    Use: puzzle = Puzzle(table=None, size)
    -------------------------------------------------------
    Preconditions:
            table - list (2D)
            size - int
    Postconditions:
        Initialized puzzle object
    -------------------------------------------------------
    """

    def __init__(self,table, size):

        # puzzle is initialized based on size and if table is given
        self.size = size
        # size = 3 for 8-puzzle and 4 for 15-puzzle

        if (table is None):
            # if no table is given as parameter, generate random 8-puzzle
            self.table = [[] for i in range(size)]
            for j in range(size):
                while len(self.table[j])<size:
                    temp = int(random.choice(self.fill))
                    if self.checkTable(self.table, size, temp) == False:
                        self.table[j].append(temp)

        else:
            self.table=table

    
    """
    -------------------------------------------------------
    Compares two puzzle object
    Use: puzzle1==puzzle2
    -------------------------------------------------------
    Preconditions:
            table - list (2D)
    Postconditions:
        Returns True if puzzle data matches, False otherwise
    -------------------------------------------------------
    """

    def __eq__(self, table1):
        # function to compare two puzzles
        if self.table == table1:
            return True
        return False

    """
    -------------------------------------------------------
    Prints Puzzle object's data table
    Use: puzzle.printPuzzle()
    -------------------------------------------------------
    Postconditions:
        Prints puzzle data table as list (2D)
    -------------------------------------------------------
    """

    def printPuzzle(self):
        for i in range(len(self.table)):
            print(self.table[i])

    """
    -------------------------------------------------------
    Converts puzzle table to string
    Use: str = str(puzzle)
    -------------------------------------------------------
    Postconditions:
        converted puzzle string
    -------------------------------------------------------
    """
    def __str__(self):

        return str(self.table)

    """
    -------------------------------------------------------
    Calculates heuristic 1 for 8-puzzle
    Use: puzzle.h1(size)
    -------------------------------------------------------
    Preconditions:
            size - int
    Postconditions:
        Returns number of misplaced puzzle pieces
    -------------------------------------------------------
    """

    def h1(self, size):
        count = 0

        for i in range(size):
            for j in range(size):

                if self.table[i][j] != goal8[i][j] and self.table[i][j]!=0:
                    count += 1
        return count

    """
    -------------------------------------------------------
    Locates blank string in puzzle
    Use: puzzle.find_blankspot()
    -------------------------------------------------------
    Postconditions:
        Returns index of blank string in puzzle (aka 0)
    -------------------------------------------------------
    """

    def find_blankspot(self):
        index=[0,0]
        for i in range(self.size):
            for j in range(self.size):
                if (self.table[i][j]==0):
                    index[0]=i
                    index[1]=j
        return index

    """
    -------------------------------------------------------
    Determines possible moves for the blank space. Either
    up, down left or right
    Use: puzzle.possible_moves(index)
    -------------------------------------------------------
    Preconditions:
            index - int
    Postconditions:
        Returns list of possible moves for blank space
    -------------------------------------------------------
    """

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

    """
    -------------------------------------------------------
    Performs translations for blank spaces within possible
    move spaces
    Use: puzzle.moves(moves, blank_spot)
    -------------------------------------------------------
    Preconditions:
            moves - list
            blank_spot - list
    Postconditions:
        Returns list of moves performed succesfully
    -------------------------------------------------------
    """
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


"""
-------------------------------------------------------
Initializes A_Solver class
Use: A_Solver(puzzle,list_moves,blank_index)
-------------------------------------------------------
Preconditions:
        Puzzle - object
        list_moves - list
        blank_index - int
Postconditions:
    Solves 8-puzzle problem and prints confirmation
    if solved. 
-------------------------------------------------------
"""

class A_Solver:
        def __init__(self,root,moves,blank_index):

            pq=PriorityQueue()
            node = _PQNode(Puzzle(root,3))
            pq.insert(node)

            visited=[]

            count=0
            expanded=0

            while(pq.is_empty()!=True ):
                expanded+=1
                u=pq.remove()
                visited.append(u._data)

                if u._data==Puzzle(goal8,3):
                    goal_node=u
                    print("Goal puzzle reached")
                    print()
                    print('[1, 2, 3]')
                    print('[4, 5, 6]')
                    print('[7, 8, 0]')
                    print()
                    break

                else:


                    blank_index=u._data.find_blankspot()
                    moves=u._data.possible_moves(blank_index)
                    list_moves=u._data.moves(moves,blank_index)
                

                    for i in (list_moves):
                        node = _PQNode(Puzzle(i,3),None,u)
 
                        if node._data in visited:
                            continue
                        new=u.g+1
                        if (node not in pq or new<node.g):
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

            print('# of steps to find solution: ', move_count)
            print('# of nodes expanded: ', expanded)

            return 


"""
-------------------------------------------------------
Initializes main class
-------------------------------------------------------
Postconditions:
    Prints 100 randomly generated 8-puzzles by calling
    A_Solver to solve them. 
-------------------------------------------------------
"""   
            
def main():
    print()
    print('TESTING FOR 8-PUZZLE')
    print('====================================================================================')
    counter=0
    while(counter<100):
        puzzle=Puzzle(None,3)

        if (puzzle.isSolvable()):
            print('-----------------------------------------------------------------------------------')
            print('Generating puzzle #' + str(counter+1) + ' : ')
            print()
            puzzle.printPuzzle()
            print()
            blank_index=puzzle.find_blankspot()
            moves=puzzle.possible_moves(blank_index)
            list_moves=puzzle.moves(moves,blank_index)
            A_Solver(puzzle,list_moves,blank_index)
            print()
            counter+=1
            print('-----------------------------------------------------------------------------------')



if __name__ == "__main__":
    main()