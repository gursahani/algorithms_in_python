class LinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next



    def __init__(self):
        self._head = None
        self._size = 0

    def reverseList(self, head):
        # start, _ = self._reverse(head)
        # return start
        return self._iter_reverse(head)

    def _reverse(self, head):
        if head is None:
            return None, None
        if head.next is None:
            return head, head
        start, tail = self._reverse(head.next)
        head.next = None
        tail.next = head
        return start, head

    def _iter_reverse(self, head):
        prev, start = None, head

        while start is not None:
            tmp = start.next
            start.next = prev
            prev = start
            start = tmp
        return prev

