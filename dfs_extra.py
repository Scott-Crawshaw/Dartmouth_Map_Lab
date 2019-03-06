# Scott Crawshaw
# 3/6/19
# dfs_extra.py
# Lab 4 Extra Credit -- Depth First Search Implementation
# based on psuedocode found here https://en.wikipedia.org/wiki/Depth-first_search and here http://projectpython.net/chapter18/

from stack_extra import Stack


def dfs_search(start_vertex, end_vertex):
    backpointers = {}
    stack = Stack()
    stack.push([start_vertex, None])
    while len(stack) != 0:
        vertex_list = stack.pop()
        vertex = vertex_list[0]
        back_vertex = vertex_list[1]
        if vertex is end_vertex:
            return get_path(back_vertex, backpointers, [vertex])
        elif vertex not in backpointers:
            backpointers[vertex] = back_vertex
            for adj in vertex.get_adj_list():
                stack.push([adj, vertex])
    return []


def get_path(vertex, backpointers, path):
    # recursively go back through the backpointers to find the path
    path.append(vertex)
    if backpointers[vertex] is None:
        return path

    return get_path(backpointers[vertex], backpointers, path)
