class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def make_edge(self, vertex, vertex2):
        if vertex2 not in self.graph[vertex]:
            self.graph[vertex].append(vertex2)

    def getEdges(self):
        total = 0
        print("Edges in graph:")
        for x, y in self.graph.items():
            for i in y:
                print(x, i, sep=' --> ')
                total += 1
        print('Total edges =', total)

    def getVertices(self):
        total = 0
        print('Vertices of graph: ')
        for i in self.graph.keys():
            print(i)
            total += 1
        print('Total vertices = ', total)

    def indegree(self, vertex):
        incomingEdge = 0
        for i in self.graph.values():
            if vertex in i:
                incomingEdge += 1
        return incomingEdge

    def outdegree(self, vertex):
        outgoingEdge = 0
        if vertex in self.graph.keys():
            for _ in self.graph[vertex]:
                outgoingEdge += 1
        return outgoingEdge

    def breadthFirstSearch(self, root):
        init = [root]
        visited = []
        while init:
            value = init.pop(0)
            visited.append(value)
            print(value)
            for i in self.graph[value]:
                if i not in visited:
                    init.append(i)

    def depthFirstSearch(self, root, stack = None, vertex = None):
        init = stack or [root]
        visited = vertex or []
        while init:
            value = init.pop()
            print(value)
            visited.append(value)
            for i in self.graph[value]:
                if i not in visited:
                    init.append(i)
                    self.depthFirstSearch(None, init, visited)

graph = Graph()
for i in range(5): graph.add_vertex(i)

graph.make_edge(0, 1)
graph.make_edge(1, 2)
graph.make_edge(2, 3)
graph.make_edge(2, 4)
graph.make_edge(3, 0)
graph.make_edge(4, 2)

if __name__ == '__main__':
    print(graph.graph)
    graph.getEdges()
    graph.getVertices()
    
    for i in graph.graph.keys():
        print(f'\nVertex {i}')
        print(f'=>> In degree = {graph.indegree(i)}')
        print(f'=>> Out degree = {graph.outdegree(i)}')

    print('\nBreadth First Search from vertex 2:')
    graph.breadthFirstSearch(2)
    print('\nDepth First Search from vertex 2:')
    graph.depthFirstSearch(2)