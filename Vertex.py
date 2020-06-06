class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}   # {id : weight}
    
    # .toStr()
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def add_neighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbour):
        return self.adjacent[neighbour]

    