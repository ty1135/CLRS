# Page 595
# O(V+E)
# bfs computes shortest-path distances
# r0 s1 t2 u3 v4 w5 x6 y7
import math

class Vertex(object):
    def __init__(self, symbol):
        self.symbol = symbol


def bfs(vertice, s):
    for vertex in vertice:
        if vertex is not s:
            vertex.color = 'white'
            vertex.distance = math.inf
            vertex.parent = None
        else:
            vertex.color = 'gray'
            vertex.distance = 0
            vertex.parent = None

    queue = []
    queue.append(s)
    while len(queue) > 0:
        u = queue.pop()
        for each in u.adj:
            if each.color == 'white':
                each.color = 'gray'
                each.distance = u.distance + 1
                each.parent = u
                queue.append(each)
        u.color = 'black'


def print_path(vertice, s, v):
    if v is s:
        print(s.symbol)
    elif v.parent is None:
        print('no path from s th v exists')
    else:
        print(v.symbol)
        print_path(vertice, s, v.parent)


if __name__ == "__main__":
    r, s, t, u, v, w, x, y = [Vertex(i) for i in 'rstuvwxy']
    vertice = r, s, t, u, v, w, x, y

    r.adj = [v, s]
    s.adj = [r, w]
    t.adj = [w, x, u]
    u.adj = [t, x, y]
    v.adj = [r]
    w.adj = [s, t, x]
    x.adj = [w, t, u, y]
    y.adj = [x, u]

    bfs(vertice, s)

    for each in vertice:
        print(each.symbol, None if each.parent is None else each.parent.symbol, each.distance, each.color)

    print("-"*10)
    print_path(vertice, s, y)