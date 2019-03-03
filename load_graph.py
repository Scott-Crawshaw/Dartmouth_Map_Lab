# Scott Crawshaw
# 3/2/19
# load_graph.py
# Lab 4 Checkpoint

from vertex import Vertex


def load_graph(filename):
    vertex_dict = {}

    # initial creation of vertices
    file = open(filename, 'r')

    for line in file:
        data = line.split(";")
        name = data[0].strip()
        adj_names = data[1].strip().replace(", ", ",").split(",")
        xy = data[2].replace(" ", "").split()

        vertex_dict[name] = Vertex(name, xy, adj_names)

    file.close()

    # go through and change the list of adj names to vertex objects
    for key in vertex_dict:
        adj_objects = []
        for adj_name in vertex_dict[key].get_adj_list():
            adj_objects.append(vertex_dict[adj_name])

        vertex_dict[key].set_adj_list(adj_objects)

    return vertex_dict
