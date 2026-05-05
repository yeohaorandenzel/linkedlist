"""Unit tests for datastruct module - Node, LinkedList, and CircularQueue.

This test file uses LAYERED TESTING:
- We start with the simplest tests (initialization)
- Then build up to testing single operations
- Then test multiple operations
- Finally test edge cases and error conditions

If you see a test fail, read the error message carefully - it will tell you:
1. What was expected
2. What actually happened
3. Where in your code to look

All tests use DEFENSIVE TESTING - they wrap operations in try/except
to skip tests for methods that haven't been implemented yet.
"""

import unittest
from datastruct import Node, LinkedList
from cq import CircularQueue


class TestNode(unittest.TestCase):
    """Test cases for Node class.

    A Node is the building block of a LinkedList.
    It stores data and has a reference to the next node.
    """

    def test_node_init_with_data(self):
        """TEST 1: Node initialization - can we create a Node?

        This is the FIRST test to fix. If this fails, check your __init__ method.
        """
        try:
            node = Node((1, 2))
            self.assertIsNotNone(node,
                "Node.__init__ returned None - did you forget to return self?")
        except NotImplementedError:
            self.skipTest("Node.__init__ not implemented yet - implement it first!")

    def test_node_get_returns_data(self):
        """TEST 2: Node.get() - does it return the stored data?

        This test checks if your get() method returns the data that was passed to __init__.
        If this fails, check that your get() method returns the stored data.
        """
        try:
            node = Node((3, 4))
            result = node.get()
            self.assertEqual(result, (3, 4),
                f"Expected get() to return (3, 4), but got {result}")
        except NotImplementedError:
            self.skipTest("Node.get() not implemented yet - implement __init__ first, then get()!")


    def test_node_has_next_attribute(self):
        """TEST 3: Node has a 'next' attribute.

        Each node needs a 'next' attribute that points to the next node.
        It should be None by default (for the tail node).
        """
        try:
            node = Node((7, 8))
            self.assertTrue(hasattr(node, 'next'),
                "Node must have a 'next' attribute. Add: self.next = None in __init__")
            # next can be None or another Node
            if node.next is not None:
                self.assertIsInstance(node.next, Node,
                    f"next should be None or another Node, but got type {type(node.next)}")
        except NotImplementedError:
            self.skipTest("Node not implemented yet")


class TestLinkedList(unittest.TestCase):
    """Test cases for LinkedList class.

    Tests are organized from SIMPLEST to MOST COMPLEX:
    1. Initialization (create empty list)
    2. Single operations (add one item, get one item)
    3. Multiple operations (add many items)
    4. Complex operations (insert, delete)
    5. Edge cases and errors (invalid indices)

    Fix tests in ORDER - if test 3 fails, test 4 will also fail!
    """


    def test_linkedlist_length_empty(self):
        """TEST 1: LinkedList.length() - does it return 0 for an empty list?

        If this fails, your length() method doesn't handle empty lists correctly.
        Hint: Check if self._head is None.
        """
        try:
            ll = LinkedList()
            length = ll.length()
            self.assertEqual(length, 0,
                f"Empty LinkedList should have length 0, but got {length}")
        except NotImplementedError:
            self.skipTest("LinkedList.length() not implemented - implement it now!")

    def test_linkedlist_append_single_item(self):
        """TEST 2: LinkedList.append() - can we add one item?

        If this fails, check your append() method:
        - Does it create a new Node with the data?
        - Does it set self._head to this new node (for the first item)?
        - Does it link nodes correctly using the 'next' attribute?
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))

            # Check that length increased
            length = ll.length()
            self.assertEqual(length, 1,
                f"After appending 1 item, length should be 1, but got {length}")

            # Check that we can get the item back
            item = ll.get(0)
            self.assertEqual(item, (1, 2),
                f"Expected to get (1, 2), but got {item}")

        except NotImplementedError:
            self.skipTest("LinkedList.append() or get() not implemented")

    def test_linkedlist_append_multiple_items(self):
        """TEST 3: LinkedList.append() - can we add multiple items?

        If this fails, your append() method doesn't handle the tail correctly.
        Hint: When appending to a non-empty list, you need to:
        1. Traverse to the last node (where node.next is None)
        2. Set the last node's next to the new node
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))
            ll.append((3, 4))
            ll.append((5, 6))

            # Check length
            length = ll.length()
            self.assertEqual(length, 3,
                f"After appending 3 items, length should be 3, but got {length}")

            # Check each item is in the correct position
            item0 = ll.get(0)
            self.assertEqual(item0, (1, 2),
                f"Item at index 0 should be (1, 2), but got {item0}")

            item1 = ll.get(1)
            self.assertEqual(item1, (3, 4),
                f"Item at index 1 should be (3, 4), but got {item1}")

            item2 = ll.get(2)
            self.assertEqual(item2, (5, 6),
                f"Item at index 2 should be (5, 6), but got {item2}")

        except NotImplementedError:
            self.skipTest("LinkedList.append() or get() not implemented")

    def test_linkedlist_insert_at_head(self):
        """TEST 4: LinkedList.insert(0, item) - can we insert at the beginning?

        Inserting at index 0 (head) is special - you need to update self._head.
        If this fails, check that your insert() handles n=0 correctly.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))  # List: [(1, 2)]

            ll.insert(0, (0, 0))  # Should become: [(0, 0), (1, 2)]

            # Check length
            length = ll.length()
            self.assertEqual(length, 2,
                f"After inserting, length should be 2, but got {length}")

            # Check that new item is at the head
            head_item = ll.get(0)
            self.assertEqual(head_item, (0, 0),
                f"After insert(0, (0,0)), item at index 0 should be (0, 0), but got {head_item}")

            # Check that old item moved to index 1
            next_item = ll.get(1)
            self.assertEqual(next_item, (1, 2),
                f"Old head item should now be at index 1, but got {next_item}")

        except NotImplementedError:
            self.skipTest("LinkedList.insert() not implemented")

    def test_linkedlist_insert_at_tail(self):
        """TEST 5: LinkedList.insert(length, item) - can we insert at the end?

        Inserting at index == length should work like append.
        If this fails, check that your insert() allows n == length.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))  # List: [(1, 2)]

            ll.insert(1, (3, 4))  # Should become: [(1, 2), (3, 4)]

            # Check length
            length = ll.length()
            self.assertEqual(length, 2,
                f"After insert at tail, length should be 2, but got {length}")

            # Check that new item is at the end
            tail_item = ll.get(1)
            self.assertEqual(tail_item, (3, 4),
                f"Item at index 1 should be (3, 4), but got {tail_item}")

        except NotImplementedError:
            self.skipTest("LinkedList.insert() not implemented")

    def test_linkedlist_insert_at_middle(self):
        """TEST 6: LinkedList.insert() - can we insert in the middle?

        If this fails, check that your insert() method:
        1. Finds the node at position n-1
        2. Creates a new node
        3. Links the new node between n-1 and n
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))  # List: [(1, 2)]
            ll.append((3, 4))  # List: [(1, 2), (3, 4)]

            ll.insert(1, (2, 3))  # Should become: [(1, 2), (2, 3), (3, 4)]

            # Check items
            self.assertEqual(ll.get(0), (1, 2))
            self.assertEqual(ll.get(1), (2, 3),
                f"Item at index 1 should be (2, 3), but got {ll.get(1)}")
            self.assertEqual(ll.get(2), (3, 4))

        except NotImplementedError:
            self.skipTest("LinkedList.insert() not implemented")

    def test_linkedlist_insert_invalid_index_raises(self):
        """TEST 7: LinkedList.insert() - does it raise IndexError for invalid index?

        If n > length, insert() should raise IndexError.
        If this fails, check that your insert() validates the index.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))  # Length is 1

            # Trying to insert at index 5 should fail
            with self.assertRaises(IndexError,
                msg="insert(5, ...) on a list of length 1 should raise IndexError"):
                ll.insert(5, (3, 4))

        except NotImplementedError:
            self.skipTest("LinkedList.insert() not implemented")

    def test_linkedlist_get_invalid_index_raises(self):
        """TEST 8: LinkedList.get() - does it raise IndexError for invalid index?

        If n >= length, get() should raise IndexError.
        If this fails, add index validation to your get() method.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))

            with self.assertRaises(IndexError,
                msg="get(10) on a list of length 1 should raise IndexError"):
                ll.get(10)

        except NotImplementedError:
            self.skipTest("LinkedList.get() not implemented")

    def test_linkedlist_delete_from_head(self):
        """TEST 9: LinkedList.delete(0) - can we delete the first item?

        Deleting the head requires updating self._head.
        If this fails, check that your delete() handles n=0 correctly.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))
            ll.append((3, 4))  # List: [(1, 2), (3, 4)]

            ll.delete(0)  # Should become: [(3, 4)]

            self.assertEqual(ll.length(), 1,
                "After deleting 1 item from 2, length should be 1")

            self.assertEqual(ll.get(0), (3, 4),
                f"After deleting head, new head should be (3, 4), but got {ll.get(0)}")

        except NotImplementedError:
            self.skipTest("LinkedList.delete() not implemented")

    def test_linkedlist_delete_from_tail(self):
        """TEST 10: LinkedList.delete() - can we delete the last item?

        If this fails, check that your delete() method:
        1. Finds the node BEFORE the one to delete (at n-1)
        2. Sets that node's next to None
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))
            ll.append((3, 4))  # List: [(1, 2), (3, 4)]

            ll.delete(1)  # Should become: [(1, 2)]

            self.assertEqual(ll.length(), 1)
            self.assertEqual(ll.get(0), (1, 2),
                f"After deleting tail, remaining item should be (1, 2), but got {ll.get(0)}")

        except NotImplementedError:
            self.skipTest("LinkedList.delete() not implemented")

    def test_linkedlist_delete_from_middle(self):
        """TEST 11: LinkedList.delete() - can we delete from the middle?

        If this fails, check that your delete() method:
        1. Finds the node BEFORE the one to delete
        2. Links it to the node AFTER the one to delete
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))
            ll.append((2, 3))
            ll.append((3, 4))  # List: [(1, 2), (2, 3), (3, 4)]

            ll.delete(1)  # Should become: [(1, 2), (3, 4)]

            self.assertEqual(ll.length(), 2)
            self.assertEqual(ll.get(0), (1, 2))
            self.assertEqual(ll.get(1), (3, 4),
                f"After deleting middle, items should be (1, 2) and (3, 4)")

        except NotImplementedError:
            self.skipTest("LinkedList.delete() not implemented")

    def test_linkedlist_delete_invalid_index_raises(self):
        """TEST 12: LinkedList.delete() - does it raise IndexError for invalid index?

        If n >= length, delete() should raise IndexError.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))

            with self.assertRaises(IndexError):
                ll.delete(10)

        except NotImplementedError:
            self.skipTest("LinkedList.delete() not implemented")

    def test_linkedlist_contains_item_found(self):
        """TEST 13: LinkedList.contains() - can we find an existing item?

        If this fails, check that your contains() method:
        1. Traverses the list
        2. Compares each node's data with the target item
        3. Returns True if found, False otherwise
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))
            ll.append((3, 4))

            found = ll.contains((3, 4))
            self.assertTrue(found,
                f"contains((3, 4)) should return True when (3, 4) is in the list")

        except NotImplementedError:
            self.skipTest("LinkedList.contains() not implemented")

    def test_linkedlist_contains_item_not_found(self):
        """TEST 14: LinkedList.contains() - does it return False for missing items?

        If this fails, make sure contains() returns False when item is not found.
        """
        try:
            ll = LinkedList()
            ll.append((1, 2))

            found = ll.contains((5, 6))
            self.assertFalse(found,
                f"contains((5, 6)) should return False when (5, 6) is not in the list")

        except NotImplementedError:
            self.skipTest("LinkedList.contains() not implemented")

    def test_linkedlist_contains_empty_list(self):
        """TEST 15: LinkedList.contains() - does it handle empty lists?

        Empty lists should always return False for contains().
        """
        try:
            ll = LinkedList()

            found = ll.contains((1, 2))
            self.assertFalse(found,
                "contains() on empty list should return False")

        except NotImplementedError:
            self.skipTest("LinkedList.contains() not implemented")


class TestCircularQueue(unittest.TestCase):
    """Test cases for CircularQueue class.

    A CircularQueue is a queue with a fixed size that wraps around.
    Think of it like a circle - when you reach the end, you go back to the start.

    The key concept is FIFO (First In, First Out):
    - The first item enqueued is the first item dequeued
    """

    def test_circularqueue_init_with_size(self):
        """TEST 1: CircularQueue initialization - can we create a queue with a size?

        If this fails, check your __init__ method.
        Make sure you store the size parameter.
        """
        try:
            cq = CircularQueue(5)
            self.assertIsNotNone(cq,
                "CircularQueue.__init__ should not return None")
            self.assertEqual(cq.size, 5,
                f"CircularQueue.size should be 5, but got {cq.size}")

        except NotImplementedError:
            self.skipTest("CircularQueue.__init__ not implemented")


    def test_circularqueue_enqueue_single_item(self):
        """TEST 2: CircularQueue.enqueue() - can we add one item?

        If this fails, check your enqueue() method.
        You need to:
        1. Store the item in your internal array
        2. Update your rear/head pointers
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

    def test_circularqueue_enqueue_multiple_items(self):
        """TEST 3: CircularQueue.enqueue() - can we add multiple items?

        If this fails, check that your enqueue() method updates pointers correctly.
        Remember: it's CIRCULAR - when rear reaches the end, it wraps to 0!
        """
        try:
            cq = CircularQueue(5)
            cq.enqueue((1, 2))
            cq.enqueue((3, 4))
            cq.enqueue((5, 6))

            # Check FIFO order
            self.assertEqual(cq.dequeue(), (1, 2),
                "First item out should be first item in")
            self.assertEqual(cq.dequeue(), (3, 4),
                "Second item out should be second item in")
            self.assertEqual(cq.dequeue(), (5, 6),
                "Third item out should be third item in")

        except NotImplementedError:
            self.skipTest("CircularQueue.enqueue() or dequeue() not implemented")

    def test_circularqueue_dequeue_fifo_order(self):
        """TEST 4: CircularQueue - does it maintain FIFO order?

        FIFO = First In, First Out
        This is the KEY property of a queue.
        """
        try:
            cq = CircularQueue(5)
            cq.enqueue((1, 2))
            cq.enqueue((3, 4))
            cq.enqueue((5, 6))

            # First in, first out
            result1 = cq.dequeue()
            self.assertEqual(result1, (1, 2),
                f"FIFO order: first enqueued was (1, 2), but got {result1}")

            result2 = cq.dequeue()
            self.assertEqual(result2, (3, 4),
                f"FIFO order: second enqueued was (3, 4), but got {result2}")

            result3 = cq.dequeue()
            self.assertEqual(result3, (5, 6),
                f"FIFO order: third enqueued was (5, 6), but got {result3}")

        except NotImplementedError:
            self.skipTest("CircularQueue.enqueue() or dequeue() not implemented")


if __name__ == '__main__':
    # Run tests with verbose output to see which tests pass/fail
    unittest.main(verbosity=2)
