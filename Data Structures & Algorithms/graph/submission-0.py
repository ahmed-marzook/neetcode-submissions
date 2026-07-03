class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        self.graph[src].discard(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        visit.add(src)
        queue = deque()
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True
                
                for neigbour in self.graph[curr]:
                    if neigbour not in visit:
                        visit.add(neigbour)
                        queue.append(neigbour)
        return False
