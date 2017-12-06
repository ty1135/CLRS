# insert is trival , deleting branches a lot conditions
# and even more in black-red tree
# so both operation in both algorithms are omitted but read


class Node(object):
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None


def inorder_tree_walk(node):
    if node is not None:
        inorder_tree_walk(node.left)
        print(node.key)
        inorder_tree_walk(node.right)


def tree_search(node, k):
    if node is not None:
        print(node.key, k)
        if node.key == k:
            return node
        elif node.key < k:
            return tree_search(node.right, k)
        else:
            return tree_search(node.left, k)


def tree_min(node):
    while node.left is not None:
        node = node.left
    return node


def tree_max(node):
    while node.right is not None:
        node = node.right
    return node


def successor(node):
    if node.right is not None:
        return tree_min(node.right)
    else:
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = node.parent
        return y


if __name__ == '__main__':
    nodes = [Node() for i in range(6)]
    for index, k in enumerate([6, 5, 7, 2, 5, 8]):
        nodes[index].key = k

    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].right = nodes[5]

    nodes[1].parent = nodes[0]
    nodes[2].parent = nodes[0]
    nodes[3].parent = nodes[1]
    nodes[4].parent = nodes[1]
    nodes[5].parent = nodes[2]



    inorder_tree_walk(nodes[0])
    print("-"*10)
    found = tree_search(nodes[0], 5)
    if found is not None:
        print(found.key)


    print("minimum: ", tree_min(nodes[0]).key)
    print("maximum: ", tree_max(nodes[0]).key)


    print(successor(nodes[3]).key)