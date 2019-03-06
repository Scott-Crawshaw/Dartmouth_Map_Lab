# Scott Crawshaw
# 3/6/19
# bfs.py
# Lab 4
# based on psuedocode found here http://projectpython.net/chapter18/

from collections import deque


def search(start_vertex, end_vertex):
    backpointers = {start_vertex: None}
    queue = deque()
    queue.append(start_vertex)

    while len(queue) != 0:
        vertex = queue.popleft()
        for adj in vertex.get_adj_list():
            if adj not in backpointers:
                backpointers[adj] = vertex
                if adj is not end_vertex:
                    queue.append(adj)
                else:
                    return get_path(adj, backpointers, [])


def get_path(vertex, backpointers, path):
    # recursively go back through the backpointers to find the shortest path
    path.append(vertex)
    if backpointers[vertex] is None:
        return path

    return get_path(backpointers[vertex], backpointers, path)
