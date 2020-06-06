import Vertex
''' Undirected weighted graph '''

class Graph:
    def __init__(self):
        self.vertices = {}  # {node(string) : Vertex(object)}
        self.num_vertices = 0
    
    def __iter__(self):
        return iter(self.vertices.values())
    
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex.Vertex(node)
        self.vertices[node] = new_vertex

    def get_vertex(self, node):
        if node in self.vertices:
            return self.vertices[node]
        else:
            return None
    
    def add_edge(self, start, end, cost = 0):
        if start not in self.vertices:
            self.add_vertex(start)
        if end not in self.vertices:
            self.add_vertex(end)

        self.vertices[start].add_neighbour(self.vertices[end], cost)
        self.vertices[end].add_neighbour(self.vertices[start], cost)
    
    def get_vertices(self):
        return self.vertices.keys()


