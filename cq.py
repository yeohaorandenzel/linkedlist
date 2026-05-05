"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        # Delete the line below and write your code here
        raise NotImplementedError("__init__ not implemented")

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        # Delete the line below and write your code here
        raise NotImplementedError("enqueue not implemented")

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        # Delete the line below and write your code here
        raise NotImplementedError("dequeue not implemented")


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass
