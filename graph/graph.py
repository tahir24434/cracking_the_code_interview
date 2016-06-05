class Vertex(object):
    def __init__(self, key):
        self.neighbours = dict()
        self.id = key

    def add_neighbour(self, nbr_key, weight=0):
        self.neighbours[nbr_key] = weight

    def get_neighbours(self):
        return self.neighbours.keys()

    def get_id(self):
        return self.id

    def get_nbr_weight(self, nbr_key):
        return self.neighbours[nbr_key]


class Graph(object):
    def __init__(self):
        self.vertices = dict()
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        vertex = Vertex(key)
        self.vertices[key] = vertex
        return vertex

    def add_edge(self, from_vert_key, to_vert_key, weight=0):
        if from_vert_key not in self.vertices.keys():
            Vertex(from_vert_key)
        if to_vert_key not in self.vertices.keys():
            Vertex(to_vert_key)

        self.vertices[from_vert_key].add_neighbour(to_vert_key, weight)

    def get_vertices_ids(self):
        return self.vertices.keys()

    def get_edges(self):
        print self.vertices
        for vertex in self.vertices.values():
            for nbrs in vertex.get_neighbours():
                print ("%s --> %s" % (vertex.get_id(), nbrs))

