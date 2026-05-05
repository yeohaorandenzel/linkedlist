"""Unit tests for adt module - Stack, Queue, and CircularQueue.

This test file uses LAYERED TESTING:
- Tests progress from SIMPLE to COMPLEX
- Each test builds on the previous ones
- Read the test names to see the progression

DEFENSIVE TESTING APPROACH:
- Tests skip if methods aren't implemented yet
- Tests provide detailed error messages to help debug
- Tests check both positive cases (should work) and negative cases (should raise errors)

LEARNING OBJECTIVES:
- Stack: LIFO (Last In, First Out) - like a stack of plates
- Queue: FIFO (First In, First Out) - like a line at a store
- CircularQueue: FIFO with fixed size - wraps around when full

If a test fails:
1. Read the ERROR MESSAGE - it tells you what went wrong
2. Read the TEST DOCSTRING - it explains what we're testing
3. Check the HINT in the assertion message - it suggests where to look
"""

import unittest
from adt import Stack, Queue, IsEmptyError
from cq import CircularQueue


class TestStack(unittest.TestCase):
    """Test cases for Stack ADT.

    A STACK follows LIFO (Last In, First Out):
    - The LAST item you PUSH IN is the FIRST item you POP OUT
    - Think of it like a stack of plates:
      * You put plates on top (push)
      * You take plates from the top (pop)
      * You can't access plates in the middle

    Test progression:
    1. Create empty stack
    2. Push one item
    3. Push multiple items
    4. Pop items (verify LIFO order)
    5. Handle edge cases (empty stack)
    """


    def test_stack_init_empty(self):
        """TEST 1: Stack initialization - can we create an empty stack?

        If this fails, your Stack class might not be properly inheriting from LinkedList.
        Check: class Stack(LinkedList)
        """
        try:
            stack = Stack()
            self.assertIsNotNone(stack,
                "Stack() should not return None")

            # Stack inherits from LinkedList, so it should have length()
            length = stack.length()
            self.assertEqual(length, 0,
                f"New Stack should have length 0, but got {length}")

        except NotImplementedError:
            self.skipTest("Stack.length() not implemented - inherits from LinkedList")

    def test_stack_push_single_item(self):
        """TEST 2: Stack.push() - can we add one item to the stack?

        A stack push should:
        1. Create a node with the data
        2. Add it to the TOP of the stack (head of the linkedlist)

        If this fails, check your push() method.
        Remember: In a linkedlist-based stack, the TOP is the HEAD.
        """
        try:
            stack = Stack()
            stack.push((1, 2))

            # Check that the item was added
            length = stack.length()
            self.assertEqual(length, 1,
                f"After pushing 1 item, length should be 1, but got {length}")

        except NotImplementedError:
            self.skipTest("Stack.push() not implemented - add it now!")

    def test_stack_push_multiple_items(self):
        """TEST 3: Stack.push() - can we add multiple items?

        If this fails, check that each push adds to the TOP.
        After pushing (1,2), (3,4), (5,6):
        - TOP is (5,6) (most recent)
        - Then (3,4)
        - Bottom is (1,2) (first item)
        """
        try:
            stack = Stack()
            stack.push((1, 2))
            stack.push((3, 4))
            stack.push((5, 6))

            length = stack.length()
            self.assertEqual(length, 3,
                f"After pushing 3 items, length should be 3, but got {length}")

        except NotImplementedError:
            self.skipTest("Stack.push() not implemented")

    def test_stack_pop_returns_last_pushed(self):
        """TEST 4: Stack.pop() - does it return the MOST RECENT item?

        This is the KEY LIFO property test!

        If you push: (1,2) then (3,4)
        Then pop should return: (3,4) (the LAST one pushed)

        If this fails, check your pop() method.
        It should remove and return from the HEAD (top) of the stack.
        """
        try:
            stack = Stack()
            stack.push((1, 2))  # Bottom
            stack.push((3, 4))  # TOP

            result = stack.pop()
            self.assertEqual(result, (3, 4),
                f"Expected to pop (3, 4) (the last pushed), but got {result}")

            # Check that the item was removed
            length = stack.length()
            self.assertEqual(length, 1,
                f"After popping from 2 items, length should be 1, but got {length}")

        except NotImplementedError:
            self.skipTest("Stack.push() or pop() not implemented")

    def test_stack_pop_multiple_returns_reverse_order(self):
        """TEST 5: Stack.pop() - does it return items in REVERSE order?

        LIFO means items come out REVERSE of how they went in.

        Push order: (1,2) -> (3,4) -> (5,6)
        Pop order:  (5,6) -> (3,4) -> (1,2)  (REVERSE!)

        If this fails, your pop() isn't removing from the correct end.
        Remember: Always pop from the HEAD (top)!
        """
        try:
            stack = Stack()
            stack.push((1, 2))
            stack.push((3, 4))
            stack.push((5, 6))

            # Should pop in REVERSE order
            first_pop = stack.pop()
            self.assertEqual(first_pop, (5, 6),
                f"First pop should return (5, 6) (last pushed), but got {first_pop}")

            second_pop = stack.pop()
            self.assertEqual(second_pop, (3, 4),
                f"Second pop should return (3, 4) (middle), but got {second_pop}")

            third_pop = stack.pop()
            self.assertEqual(third_pop, (1, 2),
                f"Third pop should return (1, 2) (first pushed), but got {third_pop}")

            # Stack should now be empty
            length = stack.length()
            self.assertEqual(length, 0,
                f"After popping all items, length should be 0, but got {length}")

        except NotImplementedError:
            self.skipTest("Stack.push() or pop() not implemented")

    def test_stack_push_pop_sequence(self):
        """TEST 6: Stack - mixed push/pop operations

        Real programs mix push and pop operations.
        This test verifies the stack maintains LIFO through a sequence.

        If this fails, trace through the operations:
        push(1,2) -> stack: [(1,2)]
        push(3,4) -> stack: [(1,2), (3,4)]
        pop()      -> returns (3,4), stack: [(1,2)]
        push(5,6) -> stack: [(1,2), (5,6)]
        pop()      -> returns (5,6), stack: [(1,2)]
        pop()      -> returns (1,2), stack: []
        """
        try:
            stack = Stack()
            stack.push((1, 2))
            stack.push((3, 4))

            # Pop should return (3, 4)
            result1 = stack.pop()
            self.assertEqual(result1, (3, 4),
                f"After push(1,2), push(3,4), pop should return (3,4), but got {result1}")

            stack.push((5, 6))

            # Pop should return (5, 6)
            result2 = stack.pop()
            self.assertEqual(result2, (5, 6),
                f"After push(5,6), pop should return (5,6), but got {result2}")

            # Pop should return (1, 2)
            result3 = stack.pop()
            self.assertEqual(result3, (1, 2),
                f"Final pop should return (1,2), but got {result3}")

        except NotImplementedError:
            self.skipTest("Stack.push() or pop() not implemented")

    def test_stack_pop_from_empty_raises(self):
        """TEST 7: Stack.pop() - does it raise an error when stack is empty?

        You can't pop from an empty stack - that's an error!

        Your pop() method should raise IsEmptyError (defined in adt.py).
        If you raise a different error, that might still work, but IsEmptyError is preferred.

        If this test fails, add a check at the START of your pop() method:
        if self.length() == 0:
            raise IsEmptyError("Cannot pop from empty stack")
        """
        try:
            stack = Stack()

            # This should raise an error - stack is empty!
            try:
                stack.pop()
                self.fail("pop() on empty stack should raise an error, but it didn't!")
            except (IsEmptyError, Exception) as e:
                # Good - it raised an error
                # But if it's NotImplementedError, the method isn't done
                if isinstance(e, NotImplementedError):
                    self.skipTest("Stack.pop() not implemented")
                # IsEmptyError or another error is acceptable
                pass

        except NotImplementedError:
            self.skipTest("Stack.pop() not implemented")


class TestQueue(unittest.TestCase):
    """Test cases for Queue ADT.

    A QUEUE follows FIFO (First In, First Out):
    - The FIRST item you ENQUEUE is the FIRST item you DEQUEUE
    - Think of it like a line at a store:
      * People join at the back (enqueue)
      * People leave from the front (dequeue)
      * No cutting in line!

    Test progression:
    1. Create empty queue
    2. Enqueue one item
    3. Enqueue multiple items
    4. Dequeue items (verify FIFO order)
    5. Handle edge cases (empty queue)
    """


    def test_queue_init_empty(self):
        """TEST 1: Queue initialization - can we create an empty queue?

        If this fails, your Queue class might not be properly inheriting from LinkedList.
        Check: class Queue(LinkedList)
        """
        try:
            queue = Queue()
            self.assertIsNotNone(queue,
                "Queue() should not return None")

            # Queue inherits from LinkedList, so it should have length()
            length = queue.length()
            self.assertEqual(length, 0,
                f"New Queue should have length 0, but got {length}")

        except NotImplementedError:
            self.skipTest("Queue.length() not implemented - inherits from LinkedList")

    def test_queue_enqueue_single_item(self):
        """TEST 2: Queue.enqueue() - can we add one item to the queue?

        Enqueue means "add to the back of the line".
        In a linkedlist-based queue, the BACK is the TAIL.

        If this fails, check your enqueue() method.
        It should add to the TAIL of the linkedlist.
        """
        try:
            queue = Queue()
            queue.enqueue((1, 2))

            # Check that the item was added
            length = queue.length()
            self.assertEqual(length, 1,
                f"After enqueuing 1 item, length should be 1, but got {length}")

        except NotImplementedError:
            self.skipTest("Queue.enqueue() not implemented - add it now!")

    def test_queue_enqueue_multiple_items(self):
        """TEST 3: Queue.enqueue() - can we add multiple items?

        If you enqueue: (1,2), (3,4), (5,6)
        The order in the queue should be:
        - Front: (1,2) (first item, will be first to leave)
        - Middle: (3,4)
        - Back: (5,6) (last item, will be last to leave)

        If this fails, check that each enqueue adds to the TAIL.
        """
        try:
            queue = Queue()
            queue.enqueue((1, 2))
            queue.enqueue((3, 4))
            queue.enqueue((5, 6))

            length = queue.length()
            self.assertEqual(length, 3,
                f"After enqueuing 3 items, length should be 3, but got {length}")

        except NotImplementedError:
            self.skipTest("Queue.enqueue() not implemented")

    def test_queue_dequeue_returns_first_enqueued(self):
        """TEST 4: Queue.dequeue() - does it return the FIRST item enqueued?

        This is the KEY FIFO property test!

        If you enqueue: (1,2) then (3,4)
        Then dequeue should return: (1,2) (the FIRST one enqueued)

        If this fails, check your dequeue() method.
        It should remove and return from the HEAD (front) of the queue.
        """
        try:
            queue = Queue()
            queue.enqueue((1, 2))  # FRONT (will be first out)
            queue.enqueue((3, 4))  # BACK

            result = queue.dequeue()
            self.assertEqual(result, (1, 2),
                f"Expected to dequeue (1, 2) (the first enqueued), but got {result}")

            # Check that the item was removed
            length = queue.length()
            self.assertEqual(length, 1,
                f"After dequeuing from 2 items, length should be 1, but got {length}")

        except NotImplementedError:
            self.skipTest("Queue.enqueue() or dequeue() not implemented")

    def test_queue_dequeue_multiple_returns_order(self):
        """TEST 5: Queue.dequeue() - does it return items in the SAME order?

        FIFO means items come out in the SAME order they went in.

        Enqueue order: (1,2) -> (3,4) -> (5,6)
        Dequeue order: (1,2) -> (3,4) -> (5,6)  (SAME ORDER!)

        If this fails, your dequeue() isn't removing from the correct end.
        Remember: Always dequeue from the HEAD (front)!
        """
        try:
            queue = Queue()
            queue.enqueue((1, 2))
            queue.enqueue((3, 4))
            queue.enqueue((5, 6))

            # Should dequeue in SAME order
            first = queue.dequeue()
            self.assertEqual(first, (1, 2),
                f"First dequeue should return (1, 2) (first enqueued), but got {first}")

            second = queue.dequeue()
            self.assertEqual(second, (3, 4),
                f"Second dequeue should return (3, 4), but got {second}")

            third = queue.dequeue()
            self.assertEqual(third, (5, 6),
                f"Third dequeue should return (5, 6) (last enqueued), but got {third}")

            # Queue should now be empty
            length = queue.length()
            self.assertEqual(length, 0,
                f"After dequeuing all items, length should be 0, but got {length}")

        except NotImplementedError:
            self.skipTest("Queue.enqueue() or dequeue() not implemented")

    def test_queue_enqueue_dequeue_sequence(self):
        """TEST 6: Queue - mixed enqueue/dequeue operations

        Real programs mix enqueue and dequeue operations.
        This test verifies the queue maintains FIFO through a sequence.

        Trace through the operations:
        enqueue(1,2) -> queue: [(1,2)]
        enqueue(3,4) -> queue: [(1,2), (3,4)]
        dequeue()    -> returns (1,2), queue: [(3,4)]
        enqueue(5,6) -> queue: [(3,4), (5,6)]
        dequeue()    -> returns (3,4), queue: [(5,6)]
        dequeue()    -> returns (5,6), queue: []

        If this fails, trace each operation and check your implementation.
        """
        try:
            queue = Queue()
            queue.enqueue((1, 2))
            queue.enqueue((3, 4))

            # Dequeue should return (1, 2)
            result1 = queue.dequeue()
            self.assertEqual(result1, (1, 2),
                f"After enqueue(1,2), enqueue(3,4), dequeue should return (1,2)")

            queue.enqueue((5, 6))

            # Dequeue should return (3, 4)
            result2 = queue.dequeue()
            self.assertEqual(result2, (3, 4),
                f"After enqueue(5,6), dequeue should return (3,4)")

            # Dequeue should return (5, 6)
            result3 = queue.dequeue()
            self.assertEqual(result3, (5, 6),
                f"Final dequeue should return (5,6)")

        except NotImplementedError:
            self.skipTest("Queue.enqueue() or dequeue() not implemented")

    def test_queue_dequeue_from_empty_raises(self):
        """TEST 7: Queue.dequeue() - does it raise an error when queue is empty?

        You can't dequeue from an empty queue - that's an error!

        Your dequeue() method should raise IsEmptyError (defined in adt.py).

        Add a check at the START of your dequeue() method:
        if self.length() == 0:
            raise IsEmptyError("Cannot dequeue from empty queue")
        """
        try:
            queue = Queue()

            # This should raise an error - queue is empty!
            try:
                queue.dequeue()
                self.fail("dequeue() on empty queue should raise an error, but it didn't!")
            except (IsEmptyError, Exception) as e:
                # Good - it raised an error
                # But if it's NotImplementedError, the method isn't done
                if isinstance(e, NotImplementedError):
                    self.skipTest("Queue.dequeue() not implemented")
                # IsEmptyError or another error is acceptable
                pass

        except NotImplementedError:
            self.skipTest("Queue.dequeue() not implemented")


class TestCircularQueue(unittest.TestCase):
    """Test cases for CircularQueue in ADT context.

    A CircularQueue is a special type of queue:
    - Has a FIXED SIZE (set when created)
    - Wraps around when it reaches the end
    - Still follows FIFO (First In, First Out)

    Think of it like a circular track:
    - Runners start at position 0
    - When they reach the end, they loop back to 0
    - The "front" and "rear" pointers move around the circle

    Test progression:
    1. Create queue with size
    2. Enqueue items
    3. Dequeue items (verify FIFO)
    4. Mixed operations
    """

    def test_circularqueue_init_with_size(self):
        """TEST 1: CircularQueue initialization - can we create a queue with a size?

        The size parameter sets the MAXIMUM number of items.
        If this fails, check your __init__ method stores the size.
        """
        try:
            cq = CircularQueue(5)
            self.assertIsNotNone(cq,
                "CircularQueue(5) should not return None")
            self.assertEqual(cq.size, 5,
                f"CircularQueue.size should be 5, but got {cq.size}")

        except NotImplementedError:
            self.skipTest("CircularQueue.__init__ not implemented")


    def test_circularqueue_enqueue_adds_item(self):
        """TEST 2: CircularQueue.enqueue() - can we add one item?

        If this fails, check your enqueue() method.
        You need to:
        1. Store the item in your internal array at the 'rear' position
        2. Update the 'rear' pointer (wrap around if needed)
        """
        try:
            cq = CircularQueue(3)
            cq.enqueue((1, 2))

            # If we can dequeue it back, it was stored correctly
            result = cq.dequeue()
            self.assertEqual(result, (1, 2),
                f"Enqueued (1, 2) but dequeued {result}")

        except NotImplementedError:
            self.skipTest("CircularQueue.enqueue() or dequeue() not implemented")

    def test_circularqueue_fifo_ordering(self):
        """TEST 3: CircularQueue - does it maintain FIFO order?

        Even though it's circular, it's still a QUEUE!
        Items must come out in the same order they went in.

        If this fails, check your dequeue() method.
        It should remove from the 'front' position and update the pointer.
        """
        try:
            cq = CircularQueue(5)
            cq.enqueue((1, 2))
            cq.enqueue((3, 4))
            cq.enqueue((5, 6))

            # FIFO: First in, first out
            result1 = cq.dequeue()
            self.assertEqual(result1, (1, 2),
                f"First dequeued should be first enqueued (1, 2), but got {result1}")

            result2 = cq.dequeue()
            self.assertEqual(result2, (3, 4),
                f"Second dequeued should be second enqueued (3, 4), but got {result2}")

            result3 = cq.dequeue()
            self.assertEqual(result3, (5, 6),
                f"Third dequeued should be third enqueued (5, 6), but got {result3}")

        except NotImplementedError:
            self.skipTest("CircularQueue.enqueue() or dequeue() not implemented")

    def test_circularqueue_enqueue_dequeue_sequence(self):
        """TEST 4: CircularQueue - mixed enqueue/dequeue operations

        This tests that your circular queue handles a realistic sequence.

        Trace through:
        enqueue(1,2) -> queue: [(1,2)]
        enqueue(3,4) -> queue: [(1,2), (3,4)]
        dequeue()    -> returns (1,2), queue: [(3,4)]
        enqueue(5,6) -> queue: [(3,4), (5,6)]
        dequeue()    -> returns (3,4), queue: [(5,6)]
        dequeue()    -> returns (5,6), queue: []

        If this fails, check that both enqueue and dequeue update pointers correctly.
        Remember to WRAP AROUND when reaching the end of the array!
        """
        try:
            cq = CircularQueue(5)
            cq.enqueue((1, 2))
            cq.enqueue((3, 4))

            result1 = cq.dequeue()
            self.assertEqual(result1, (1, 2),
                "First dequeue should return (1, 2)")

            cq.enqueue((5, 6))

            result2 = cq.dequeue()
            self.assertEqual(result2, (3, 4),
                "Second dequeue should return (3, 4)")

            result3 = cq.dequeue()
            self.assertEqual(result3, (5, 6),
                "Third dequeue should return (5, 6)")

        except NotImplementedError:
            self.skipTest("CircularQueue.enqueue() or dequeue() not implemented")


if __name__ == '__main__':
    # Run with verbose output to see detailed test results
    unittest.main(verbosity=2)
