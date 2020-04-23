import collections
class QueueWithMax:
    def __init__(self):
        self.queue = collections.deque
        self.aux = collections.deque
        self.max = 0

    def enqueue(self, element):
        self.max = element
        self.queue.append(element)
        while self.aux and element > self.aux[-1]:
            self.aux.pop()
        self.aux.append(element)

    def dequeue(self):
        x = self.queue.popleft()
        if x == self.aux[0]:
            self.aux.popleft()
        return x

    def max(self):
        if self.aux:
            return self.aux[0]

