import Graph
import pygame

neighbours_matrix = [(0,1), (1,0), (1,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]

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

# g: 2d array, start: tuple, end: tuple
# finish once end is visited
def dijkstra_array(g, start, end):
    visited = []
    short_dst = {} # {tuple(int, int) : [cost, (tuple(int, int))]}
    dim = (len(g), len(g[0]))
    for row in range(dim[0]):
        for col in range(dim[1]):
            if (g[row][col] != -1):
                if ((row, col) == start):
                    short_dst[(row, col)] = [0, None]
                else:
                    short_dst[(row, col)] = [float('inf'), None]
    while (end not in visited):
        u = get_closest_vertex(short_dst, visited)
        visited.append(u)
        neighbours = get_neighbours(u, g)
        for v in neighbours:
            alt = short_dst[u][0] + g[u[0]][u[1]]
            if (alt < short_dst[v][0]):
                short_dst[v][0] = alt
                short_dst[v][1] = u
    return short_dst

def get_neighbours(u, g):
    neighbours = list(map(lambda x: (x[0]+u[0], x[1]+u[1]), neighbours_matrix))
    temp_neighbours = neighbours.copy()
    for x in neighbours:
        if (x[0] < 0 or x[1] < 0 or x[0] >= len(g[0]) or x[1] >= len(g[1]) or g[x[0]][x[1]] == -1):
            temp_neighbours.remove(x)
    return temp_neighbours


def build_path(short_dist, start, end):
    path = []
    path.insert(0, end)
    next_cell = short_dist[end][1]
    while (start not in path):
        path.insert(0, next_cell)
        next_cell = short_dist[next_cell][1]
    return path


if __name__ == '__main__':

    # g = Graph.Graph()

    # g.add_vertex('a')
    # g.add_vertex('b')
    # g.add_vertex('c')
    # g.add_vertex('d')
    # g.add_vertex('e')
    # g.add_vertex('f')

    # g.add_edge('a', 'b', 7)  
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    # g.add_edge('d', 'e', 6)
    # g.add_edge('e', 'f', 9)
    # print(g.get_vertices())
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    # for v in g:
    #     print ('g.vertices[%s]=%s' %(v.get_id(), g.vertices[v.get_id()]))
    
    # print(dijkstra(g, 'c'))
    g = []
    for row in range(3):
        g.append([])
        for col in range(3):
            g[row].append(0)
    g[1][1] = -1
    dij = dijkstra_array(g, (0,0), (2,2))
    print(build_path(dij, (0, 0), (2,2)))