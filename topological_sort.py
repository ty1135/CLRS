# the reason the choose finish time is as follow
# look at second figure on page 607
# consideration : tree edges, back edges, forwards edges, crossing edges

# tree edges just partially preserve the information(but there are other edges to consider)
# back edges forms cycle, which leads to no solution. thus assume it doesn't exist
# forwards edges does not change the topological order from both side(left, right)
# crossing edges: vertex with late (d or f) time always points to the other with early time

# therefore, finish time with backward direction(decs order) is chosen


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



def toplogical_sort(vertice):
    vertice.sort(key=lambda x: -x.finish)
    for each in vertice:
        print(each.symbol)


if __name__ == "__main__":
    cloths = []
    cloths_symbol = ['undershorts', 'pants', 'belt', 'shirt', 'tie', 'jacket', 'socks','shoes', 'watch']
    for each in cloths_symbol:
        exec('{each} = Vertex("{each}")'.format(each=each))

    cloths = [undershorts, pants, belt, shirt, tie, jacket, socks, shoes, watch]

    undershorts.adj = [pants, shoes]
    pants.adj = [shoes]
    belt.adj = [jacket]
    shirt.adj = [belt, tie]
    tie.adj = [jacket]
    jacket.adj = []
    socks.adj = [shoes]
    shoes.adj = []
    watch.adj = []

    dfs(cloths)
    toplogical_sort(cloths)