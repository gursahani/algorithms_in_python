import heapq
import collections

class Node:
    def __init__(self, prob, symbol=None):
        """Create node for given symbol and probability"""
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob


    def __lt__(self, other):
        return self.prob < other.prob

    def encode(self, encoding):
        """Return bit encoding in traversal"""
        if self.left is None and self.right is None:
            yield self.symbol, encoding
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v


class Huffman:
    def __init__(self, s):
        self.s = s
        c = collections.Counter(self.s)

        #construct priority queue
        pq = []
        for symbol in c:
            pq.append(Node(c[symbol], symbol))
        heapq.heapify(pq)

        #huffman encoding algorithm
        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            n3 = Node(n1.prob + n2.prob)
            n3.left = n1
            n3.right = n2
            heapq.heappush(pq, n3)

        #Record
        self.root = pq[0]
        self.encoding = {}
        for sym, code in pq[0].encode(''):
            self.encoding[sym] = code

    def __repr__(self):
        return 'huffman: ' + str(self.encoding)

    def encode(self, s):
        """Return bit string for encoding"""

        bits = ''
        for _ in s:
            if _ not in self.encoding:
                raise ValueError("" + _ + " is not encoded")

            bits += self.encoding[_]

        return bits


if __name__ == '__main__':
    s = Huffman("aaabc")
    print(s.encode("aaabc"))
    print(s)
