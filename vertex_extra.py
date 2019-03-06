# Scott Crawshaw
# 3/6/19
# vertex.py
# Lab 4

from cs1lib import *


class Vertex:
    def __init__(self, name, xy, adj_list, vertex_color=(0, 0, 1), highlighted_edge_color=(1, 0, 0),
                 edge_color=(0, 0, 1), highlighted=False, next_vertex=None):
        self.name = name
        self.xy = xy
        self.adj_list = adj_list
        self.vertex_color = vertex_color
        self.edge_color = edge_color
        self.highlighted_edge_color = highlighted_edge_color
        self.highlighted = highlighted
        self.next_vertex = next_vertex

    def __str__(self):
        string = self.name + "; Location: " + str(self.xy) + "; Adjacent vertices: "
        string = string.replace("[", "").replace("]", "").replace("'", "").replace(",", ", ").replace("  ", " ")
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
            if self.get_next_vertex() is vertex or vertex.get_next_vertex() is self:
                set_stroke_color(self.highlighted_edge_color[0], self.highlighted_edge_color[1],
                                 self.highlighted_edge_color[2])
            else:  # draw the line blue if the vertexes are not both on the path
                set_stroke_color(self.edge_color[0], self.edge_color[1], self.edge_color[2])

            adj_xy = vertex.get_xy()
            draw_line(self.xy[0], self.xy[1], adj_xy[0], adj_xy[1])

    def is_highlighted(self):  # is the vertex on the path
        return self.highlighted

    def set_highlighted(self, highlighted):  # set if the vertex is on the path
        self.highlighted = highlighted

    def set_next_vertex(self, vertex):
        self.next_vertex = vertex

    def get_next_vertex(self):
        return self.next_vertex
