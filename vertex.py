# Scott Crawshaw
# 3/2/19
# vertex.py
# Lab 4 Checkpoint

from cs1lib import *

class Vertex:
    def __init__(self, name, xy, adj_list, vertex_color=(0, 0, 1), highlighted_edge_color=(1, 0, 0),
                 edge_color=(0, 0, 1), highlighted=False):
        self.name = name
        self.xy = xy
        self.adj_list = adj_list
        self.vertex_color = vertex_color
        self.edge_color = edge_color
        self.highlighted_edge_color = highlighted_edge_color
        self.highlighted = highlighted

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

    def get_xy(self):
        return self.xy

    def set_vertex_color(self, color):
        self.vertex_color = color

    def draw_vertex(self, radius):
        set_fill_color(self.vertex_color[0], self.vertex_color[1], self.vertex_color[2])
        disable_stroke()
        draw_circle(self.xy[0], self.xy[1], radius)

    def draw_lines(self, line_width):
        enable_stroke()
        set_stroke_width(line_width)
        for vertex in self.adj_list:
            if vertex.is_highlighted() and self.is_highlighted():
                set_stroke_color(self.highlighted_edge_color[0], self.highlighted_edge_color[1],
                                 self.highlighted_edge_color[2])
            else:
                set_stroke_color(self.edge_color[0], self.edge_color[1], self.edge_color[2])

            adj_xy = vertex.get_xy()
            draw_line(self.xy[0], self.xy[1], adj_xy[0], adj_xy[1])

    def is_highlighted(self):
        return self.highlighted

    def set_highlighted(self, highlighted):
        self.highlighted = highlighted
