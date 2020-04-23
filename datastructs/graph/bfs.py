class BFSAlgo:
    graph = {
        0: [1, 4],
        1: [0, 3, 4],
        2: [3, 4],
        3: [1, 2],
        4: [0, 1, 2]
    }


    def DFS(self, vertex, graph):
        visited = set()
        visited.add(vertex)
        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                self.DFS(v, graph)

    def BFS(self, vertex: int, graph: dict) -> list:

        queue = [vertex]

        visitedNodes = []
        while queue:
                visitedNode = queue.pop(0)
                # print(visitedNode)
                visitedNodes.append(visitedNode)
                for item in graph[visitedNode]:
                    if item not in queue and item not in visitedNodes:
                        queue.append(item)
        return visitedNodes


if __name__ == '__main__':
    b = BFSAlgo()
    print(b.BFS(0, b.graph))
