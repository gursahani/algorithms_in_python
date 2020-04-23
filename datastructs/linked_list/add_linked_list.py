class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail


class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.addNode(_)

    def addNode(self, val):
        self.head = LinkedNode(val, self.head)

    def remove(self, value):
        n = self.head
        last = None
        while n is not None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n
            n = n.next
        return False

    def pop(self):
        if self.head is None:
            raise Exception("Empty List")
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __str__(self):
        str_ = ""
        for i in self.__iter__():
            str_ += str(i)

        return str_