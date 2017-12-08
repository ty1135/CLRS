# Page 595
# O(V+E)
# bfs computes shortest-path distances
# r0 s1 t2 u3 v4 w5 x6 y7

# Parenthesis theorem
# u, v are either in the same tree or disjoint tress
# within a tree, ancestor.start< descendent.start
#                ancestor.finish > descendent.fisnish

# white path theorm just follows the parenthesis above
# view the figure on page 607

# tree edges back edges forward edges cross edges
# undirected grapy only has tree edges and back edges


class Vertex(object):
    def __init__(self, symbol):
        self.symbol = symbol


def dfs(vertice):
    def dfs_visit(vertex):
        nonlocal time
        time += 1

        vertex.color = 'gray'
        vertex.discover = time
        for neighbor in vertex.adj:
            if neighbor.color == 'white':
                neighbor.parent = vertex
                dfs_visit(neighbor)
        vertex.color = 'black'
        time += 1
        vertex.finish = time

    time = 0
    for each in vertice:
        each.color = 'white'
        each.parent = None

    for each in vertice:
        if each.color == 'white':
            dfs_visit(each)


def print_path(vertice, s, v):
    if v is s:
        print(s.symbol)
    elif v.parent is None:
        print('no path from s th v exists')
    else:
        print(v.symbol)
        print_path(vertice, s, v.parent)


if __name__ == "__main__":
    u, v, w, x, y, z = [Vertex(i) for i in 'uvwxyz']
    vertice = u, v, w, x, y, z

    u.adj = [v, x]
    v.adj = [y]
    w.adj = [y, z]
    x.adj = [v]
    y.adj = [x]
    z.adj = [z]

    dfs(vertice)

    for each in vertice:
        print(each.symbol, None if each.parent is None else each.parent.symbol, (each.discover, each.finish), each.color)

    print("-"*10)
    print_path(vertice, u, x)