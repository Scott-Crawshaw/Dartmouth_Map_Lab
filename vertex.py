# Scott Crawshaw
# 3/2/19
# vertex.py
# Lab 4 Checkpoint


class Vertex:
    def __init__(self, name, xy, adj_list):
        self.name = name
        self.xy = xy
        self.adj_list = adj_list

    def __str__(self):
        string = self.name + "; Location: " + str(self.xy) + "; Adjacent vertices: "
        string = string.replace("[", "").replace("]", "").replace("'", "").replace(",", ", ")
        string += self.get_adj_names()

        return string

    def get_adj_list(self):
        return self.adj_list

    def set_adj_list(self, set_list):
        self.adj_list = set_list

    def get_name(self):
        return self.name

    def get_adj_names(self):
        # get the names of the adjacent vertices in the appropriate format
        names_string = ""
        for vertex in self.adj_list:
            names_string += (vertex.get_name() + ", ")

        return names_string[:-2]
