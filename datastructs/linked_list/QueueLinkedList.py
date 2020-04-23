class Empty(Exception):
    pass


class QueueLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')

        return self._head._element

    def dequeue(self):

        if self.is_empty():
            raise Empty('queue is empty')

        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans

    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail = newest
        self._tail = newest
        self._size += 1

    @property
    def tail(self):
        return self._tail
