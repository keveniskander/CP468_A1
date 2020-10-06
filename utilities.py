"""
-------------------------------------------------------
priority_queue_linked.py
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-11-07"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQNode:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node.
        Use: node = _PQNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _next - another priority queue node (_PQNode)
        Postconditions:
            Initializes a priority queue node that contains a copy of value
            and a link to the next node in the priority queue.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = _next
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
        Use: b = pq.empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

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
        Use: pq.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        node = None
        if self._count == 0:
            node = _PQNode(value,None)
            self._front = node
            self._count+=1
        else:
            node = _PQNode(value,None)
            self._rear = node
            self._count+=1
            

        return

    def remove(self):
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

        value = self._front._data
        self._front = self._front._next
        self._count-=1
        

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

        value = deepcopy(self._front._data)

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
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        current = self._front

        while current!=None:
            if current._data>=key:
                pq3.insert(current._data)
                self.remove()
            elif current._data<key:
                pq2.insert(current.remove())
                self.remove()
            current = current._next
        return pq2, pq3

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
            yield current._data
            current = current._next
