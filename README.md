**Prerequisites:** Python programming, Object-oriented programming, Linkedlist

```
888b     d888        d8888 8888888888P 8888888888      8888888b.  888     888 888b    888 888b    888 8888888888 8888888b.  
8888b   d8888       d88888       d88P  888             888   Y88b 888     888 8888b   888 8888b   888 888        888   Y88b 
88888b.d88888      d88P888      d88P   888             888    888 888     888 88888b  888 88888b  888 888        888    888 
888Y88888P888     d88P 888     d88P    8888888         888   d88P 888     888 888Y88b 888 888Y88b 888 8888888    888   d88P 
888 Y888P 888    d88P  888    d88P     888             8888888P"  888     888 888 Y88b888 888 Y88b888 888        8888888P"  
888  Y8P  888   d88P   888   d88P      888             888 T88b   888     888 888  Y88888 888  Y88888 888        888 T88b   
888   "   888  d8888888888  d88P       888             888  T88b  Y88b. .d88P 888   Y8888 888   Y8888 888        888  T88b  
888       888 d88P     888 d8888888888 8888888888      888   T88b  "Y88888P"  888    Y888 888    Y888 8888888888 888   T88b 
```

This project contains an algorithm that figures out a way out of the maze.

The implementation here uses a Stack to store the coordinates to be explored at each step. The Stack data structure is implemented using a LinkedList.

`main.py` and `maze.py` contain complete code to solve a maze, but `datastruct.py` and `adt.py` are incomplete!

----------

# Your task

## Part 1: LinkedList

1. Implement the `LinkedList` class in `datastruct.py` to enable the maze to be solved.
2. Use your own tests, to check your `LinkedList` implementation.

Remember to remove the `raise NotImplementedError` lines. While the `pass` keyword allows the program to continue silently without any code to run, the `NotImplementedError` halts the program. Very useful to remind yourself of parts of the code that are not yet ready and still need work!

**Technical notes:**

LinkedList is a **data structure**. That means there is a detailed specification for how it should be implemented.

Run `python test_datastruct.py` to test your LinkedList code.

----------

## Part 2: Stack and Queue

The program in `main.py` uses a Stack to implement a **depth-first search** strategy. This approach checks a single route at a time, exploring until it reaches a dead end before backtracking to the last unexplored fork.

1. Implement the `Stack` and `Queue` classes in `adt.py` to enable the maze to be solved.
2. Check and debug your `Stack` and `Queue` implementations.  
   You can use `test_adt.py` to help you do a more comprehensive check.
If it works correctly, you should see the program successfully find its way out of the maze!
3. Observe the difference in the way the maze is explored when Stack and Queue are used.
4. Edit the program in `main.py`, replacing the Stack with a Queue (and using appropriate queue methods). This switches the strategy to a **breadth-first search**. All encountered routes are checked simultaneously and advance one step each cycle.

**Technical notes:**

Stacks and queues are not data structures; instead, they are **abstract data types**. That means:

- "Abstract": There is no detailed specification for they should be implemented. One can reasonably use any implementation so long as the behaviour of the class is correct.  
  However, the choice of implementation will have implications for efficiency.
- "Data type": there are expectations of how stacks and queues should behave.
  - Stacks are expected to behave first-in-last-out (FILO)
  - Queues are expected to behave first-in-first-out (FIFO)

----------

## Part 3: CircularQueue

A Circular Queue is a **fixed size** queue where the next item that comes after the tail (last item) is the head (first item).

The fixed size of a Circular Queue makes it much easier to implement `enqueue()` and `dequeue()` methods, as there is no need to implement insert/append/delete methods. Instead, the `head` and `tail` attributes keep track of the indexes where exising items will be dequeued, and where new items will be enqueued.

1. Implement the `CircularQueue` class in `cq.py` to enable the maze to be solved.
2. Use your own tests, to check your `Circular Queue` implementation.
3. Edit `main.py` to use a `CircularQueue` class instead of a `Queue`.  
If it works correctly, you should see the program successfully find its way out of the maze (using breadth-first search)!

## Implementation

### Head and tail
There is no standard convention which end the circular queue should be dequeued at or dequeued from. For this project, we will enqueue at `tail` and dequeue from `head`.

When the circular queue is empty, no dequeueing is possible. The `head` is thus initialised with an invalid index, and reset to the same invalid index whenever the queue is empty again.

When the circular queue is full, no enqueueing is possible (because the size is fixed). The `tail` is set to an invalid index whenever the queue is full.

### Enqueue

When enqueueing an item, the following operations need to be carried out:

1. Check if queue is full (`tail` is invalid), raise an error if so.
2. Add the item at the `tail` index.
3. Increment the `tail` index, with wrap-around.
4. Check if the queue is full (`tail` points to `head`), invalidate `head` if necessary.

### Dequeue

When dequeueing an item, the following operations need to be carried out:

1. Check if queue is empty (`head` is invalid), raise an error if so.
2. Increment the `head` index, with wrap-around.
3. Check if the queue is empty (`head` points to `tail`), invalidate `tail` if necessary.
4. Return the item

**Technical notes:**

CircularQueue is *not* an abstract data type. It has an expected implementation, with its slots statically allocated beforehand, which typically implies using static arrays.

At the same time, there are expectations of how the circular queue should behave. The circular queue must follow the same behaviour as queues, and it must be implemented such that the head wraps around to its tail. This makes it closer to a **concrete** data type, not abstract data type.
