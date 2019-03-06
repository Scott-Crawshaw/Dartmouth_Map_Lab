from bfs import search
from cs1lib import *
from load_graph import load_graph

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


def reset_vertex_colors():
    for key in vertex_dict:
        if key != start_vertex_key and key != end_vertex_key:
            vertex_dict[key].set_vertex_color(BLUE)
            vertex_dict[key].set_highlighted(False)


def check_mouse(mx, my):
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


def make_path():
    if start_vertex_key is not None and end_vertex_key is not None and end_vertex_key is not start_vertex_key:
        path = search(vertex_dict[start_vertex_key], vertex_dict[end_vertex_key])
        for item in path:
            item.set_vertex_color(RED)
            item.set_highlighted(True)


def draw_map():
    draw_image(map_image, 0, 0)
    check_mouse(mouse_x(), mouse_y())
    for key in vertex_dict:
        vertex_dict[key].draw_lines(LINE_WIDTH)
    for key in vertex_dict:
        vertex_dict[key].draw_vertex(VERTEX_RADIUS)


map_image = load_image(MAP_FILE_NAME)
vertex_dict = load_graph(GRAPH_FILE_NAME)
start_vertex_key = None
end_vertex_key = None
clicked = False

start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=pressed, mouse_release=released)
