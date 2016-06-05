import graph

g = graph.Graph()

for i in range(4):
    g.add_vertex(i)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(2, 2)
print g.get_vertices_ids()

g.get_edges()