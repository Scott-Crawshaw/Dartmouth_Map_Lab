# Scott Crawshaw
# 3/6/19
# map_plot_extra.py
# Lab 4 Extra Credit

from cs1lib import *
from dfs_extra import dfs_search
from load_graph_extra import load_graph

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
MAP_FILE_NAME = "dartmouth_map.png"
GRAPH_FILE_NAME = "dartmouth_graph.txt"
VERTEX_RADIUS = 8
RED = (1, 0, 0)
BLUE = (0, 0, 1)
LINE_WIDTH = 5


def pressed(mx, my):
    global clicked
    clicked = True


def released(mx, my):
    global clicked
    clicked = False


def reset_vertex_colors():  # reset all of the vertexes to blue and take them off the path
    for key in vertex_dict:
        if key != start_vertex_key and key != end_vertex_key:
            vertex_dict[key].set_vertex_color(BLUE)
            vertex_dict[key].set_highlighted(False)
        vertex_dict[key].set_next_vertex(None)


def check_mouse(mx, my):  # get the position of the mouse and see if its on a vertex
    global end_vertex_key, start_vertex_key
    if start_vertex_key is not None or clicked:
        for key in vertex_dict:
            vx = vertex_dict[key].get_xy()[0]
            vy = vertex_dict[key].get_xy()[1]
            if (vx - VERTEX_RADIUS < mx < vx + VERTEX_RADIUS) and (vy - VERTEX_RADIUS < my < vy + VERTEX_RADIUS):
                vertex_dict[key].set_vertex_color(RED)
                if clicked:
                    start_vertex_key = key
                else:
                    end_vertex_key = key
                reset_vertex_colors()
                make_path()
                break


def make_path():  # call bfs.py to generate the shortest path
    if start_vertex_key is not None and end_vertex_key is not None and end_vertex_key is not start_vertex_key:
        path = dfs_search(vertex_dict[start_vertex_key], vertex_dict[end_vertex_key])
        old_item = None
        for item in path:
            item.set_vertex_color(RED)
            item.set_highlighted(True)
            if old_item is not None:
                old_item.set_next_vertex(item)
            old_item = item


def draw_map():
    draw_image(map_image, 0, 0)
    check_mouse(mouse_x(), mouse_y())

    # I use two for loops to ensure that the vertexes all get drawn on top of the edges
    # Important because edges are double drawn
    for key in vertex_dict:
        vertex_dict[key].draw_lines(LINE_WIDTH)
    for key in vertex_dict:
        vertex_dict[key].draw_vertex(VERTEX_RADIUS)

    # draw start and end vertex names
    set_font_size(20)
    set_font_bold()
    enable_stroke()
    set_stroke_color(0, 0, 0)

    if start_vertex_key is not None:
        draw_text(vertex_dict[start_vertex_key].get_name(), vertex_dict[start_vertex_key].get_xy()[0],
                  vertex_dict[start_vertex_key].get_xy()[1] - VERTEX_RADIUS * 2)

    if end_vertex_key is not None:
        draw_text(vertex_dict[end_vertex_key].get_name(), vertex_dict[end_vertex_key].get_xy()[0],
                  vertex_dict[end_vertex_key].get_xy()[1] - VERTEX_RADIUS * 2)


map_image = load_image(MAP_FILE_NAME)
vertex_dict = load_graph(GRAPH_FILE_NAME)
start_vertex_key = None
end_vertex_key = None
clicked = False  # keeps track of whether the mouse has been pressed

start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=pressed, mouse_release=released)
