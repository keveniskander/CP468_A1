"""
-----------------------------------
priority_queue_linked.py
[program description]
----------------------------------
Author: Carla Castaneda
ID: 170804730
Email: cast4730@mylaurier.ca
_updated_= "2018-03-05"
implementation taken from cp164 by david brown
edited for this project
---------------------------------------
"""

import copy
from copy import deepcopy
import itertools

class _PQNode:

    def __init__(self,table,  _next=None,parent=None, heuristic = 1):
        """
        -------------------------------------------------------
        Initializes a priority queue node.
        Use: node = _PQNode(table, _next,parent)
        -------------------------------------------------------
        Preconditions:
             value - data value for node (?)
            _next - another priority queue node (_PQNode)
        Postconditions:
            Initializes a priority queue node that contains a copy of value
            and a link to the next node in the priority queue.
        -------------------------------------------------------
        """
        self._data = deepcopy(table)
        #self.table= deepcopy(table)

        self.parent = parent
        self._next = _next
        self._id = id(list(itertools.chain(*self._data)))

        self.g=0
        self.f=0
        if heuristic == 1:
            self.h=table.h1()
        elif heuristic == 2:
            self.h=table.manhattan()
        else:
            self.h=table.h3()

        if self.parent!=None:
            self.g=self.parent.g +1

            self.f= self.g + self.h

        return
    

class PriorityQueue:
    
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        if self._front is None:
            return True
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the priority queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the priority queue.
        Use: pq.insert(value,_next,parent)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        previous=None
        current=self._front
         
        while current is not None and current.f < value.f:
            previous=current
            current=current._next
        
        if previous is None:
            temp=self._front
            self._front=value
            #self._front= _PQNode(copy.deepcopy(value), temp,parent)
            self._front._next=temp
        else:
    
            #previous._next=_PQNode(copy.deepcopy(value), current,parent)
            previous._next=value
            previous._next._next=current

            
        self._count+=1
        

        return

    def remove(self,node=None):
        """
        -------------------------------------------------------
        Removes and returns value from the priority queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the highest priority value in the priority queue -
            the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"
        if node==None:
            value = self._front
            self._count-=1
            if self._count == 0:
                self._front = None
            else:
                self._front= self._front._next
        else:

            previous=None
            current=self._front
            
            while current is not None and current._data!=node._data:
                previous=current
                current=current._next

            if previous is None:
                #temp=self._front
                self._front=current._next
                #self._front= _PQNode(copy.deepcopy(value), temp,parent)
                #self._front._next=temp
            else:
    
                #previous._next=_PQNode(copy.deepcopy(value), current,parent)
                previous._next=current._next
                #previous._next._next=current




        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the highest priority value in the priority queue -
            the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        # your code here
        value=copy.deepcopy(self._front._data)

        return value

    def split(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The split is stable.
        Use: pq2, pq3 = pq1.split(key)
        -------------------------------------------------------
        Preconditions:
            key - a data object (?)
        Postconditions:
            returns
            pq2 - a priority queue that contains all values
                with priority less than key (PriorityQueue)
            pq3 - priority queue that contains all values with
                priority greater than or equal to key (PriorityQueue)
            The current priority queue is empty
        -------------------------------------------------------
        """
        pq2=PriorityQueue()
        pq3=PriorityQueue()
          
        previous2=None
        previous3=None 

        while self._front is not None:
              
            if self._front._data>key:
                  
                if previous2 is None:
  
                    pq2._front=self._front
                    
                    
                    previous2=pq2._front

                else:
                      
                    previous2._next=self._front
                    
                    

                    previous2=previous2._next
                self._front=self._front._next
                pq2._count+=1
                

            elif self._front._data<=key:
                if previous2 is not None:
                    previous2._next=None
                   
                if previous3 is None:
                    pq3._front=self._front
                    
                      
                    previous3=pq3._front
                    
                          
                else:
                    previous3._next=self._front
                    
   
                    previous3=previous3._next
                pq3._count+=1
                
                self._front=self._front._next
            self._count-=1
            
        if previous3 is not None:
            previous3._next=None
 
        return pq2, pq3

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs PriorityQueue to the front
        of the current PriorityQueue.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Preconditions:
            rs - a linked PriorityQueue (PriorityQueue)
        Postconditions:
            The current PriorityQueue contains the old front of the rs PriorityQueue and
            its count is updated. The rs PriorityQueue front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current
            current = current._next

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs PriorityQueue to the front
        of the current PriorityQueue.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Preconditions:
            rs - a linked PriorityQueue (PriorityQueue)
        Postconditions:
            The current PriorityQueue contains the old front of the rs PriorityQueue and
            its count is updated. The rs PriorityQueue front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here

        return