import Graph

# g: Graph, src: Vertex
def dijkstra(g, src):
    short_dist = {}   # {vertex: [shortest distance, previous vertex]} shortest distance from source
    visited = []
    unvisited = list(g.get_vertices())
    for v in unvisited:
        if (v == src):
            short_dist[v] = [0, None]
        else:
            short_dist[v] = [float('inf'), None]
    while (len(unvisited) > 0):
        u = get_closest_vertex(short_dist, visited)
        unvisited.remove(u)
        visited.append(u)
        for v in g.vertices[u].get_connections():
            alt = short_dist[u][0] + v.get_weight(g.vertices[u])
            if (alt < short_dist[v.get_id()][0]):
                short_dist[v.get_id()][0] = alt
                short_dist[v.get_id()][1] = u
    return short_dist

def get_closest_vertex(short_dist, visited):
    min_dist = float('inf')
    min_vertex = None
    for v in short_dist:
        if (short_dist[v][0] < min_dist and v not in visited):
            min_vertex = v
    return min_vertex

if __name__ == '__main__':

    g = Graph.Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    print(g.get_vertices())
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    for v in g:
        print ('g.vertices[%s]=%s' %(v.get_id(), g.vertices[v.get_id()]))
    
    print(dijkstra(g, 'c'))