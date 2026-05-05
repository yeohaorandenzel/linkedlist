"""This module solves a maze using breadth-first or depth-first search.
Depth-first search (DFS) is carried out with a stack, while
breadth-first search (BFS) is carried out with a queue.

Submodules:
- maze.py
  Maze class encapsulates maze data and provides methods for accessing
  and displaying it.
- datastruct.py
  Contains the LinkedList class which Stack and Queue inherit.
- adt.py
  Contains the Stack and Queue classes, which are used to keep track of
  unexplored paths.
- cq.py
  Contains the CircularQueue class, as an alternative to Queue.
"""
############################### 72 chars ###############################

# Builtin imports
import time

# Local imports
from adt import IsEmptyError, Stack, Queue
from cq import CircularQueue
from maze import Maze


class OutOfOptionsError(Exception):
    pass


# Initialise options as a Stack or Queue (choose one)
# Used to store available path options for the next step.
options = Stack()
# options = Queue()
# options = CircularQueue(20)

# Stores a list of visited coords
visited: list[tuple[int, int]] = []

maze = Maze('maze.txt')

here = maze.start
counter = 0
while here != maze.end:
    print(f'== STEP {counter} ==')
    maze.display(
        position=here,
        options=options,
        visited=visited,
    )
    print(f'Here: {here}')
    print(f'Visited: {visited}')

    # Add possible paths to options
    for coord in maze.around(here):
        if coord not in visited:
            options.push(coord)
    # Store visited coord
    visited.append(here)

    # Visit the next option
    try:
        here = options.pop()
    except IsEmptyError:
        raise OutOfOptionsError("Stuck! No available paths")
    counter += 1

    # Slow down program so that humans can follow
    time.sleep(0.5)
