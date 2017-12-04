class LinkedList(object):
    def __init__(self, head):
        self.head = head


class Node(object):
    def __init__(self, *arg, **kwargs):
        super(Node, self).__init__(*arg, **kwargs)
        self.next = None


def list_search(linked_list, key):
    x = linked_list.head

    while x is not None:
        if x.key == key:
            return x
        else:
            x = x.next


def list_insert(linked_list, node):
    node.next = linked_list.head
    linked_list.head = node


def list_delete(linked_list, node):
    # boundary condition : prev/next of 'node'
    # it requires double linked list

    # also circular, doubly linked list with a sentinel
    # works perfectly without boundary considerations
    pass


def list_print(linked_list):
    x = linked_list.head
    while x is not None:
        print(x.key)
        x = x.next


if __name__ == "__main__":
    n1 = Node()
    n1.key = 1

    n2 = Node()
    n2.key = 2

    n3 = Node()
    n3.key = 3

    n1.next = n2
    n2.next = n3

    linked_list = LinkedList(n1)

    ret = list_search(linked_list, 3)
    print(ret)

    if ret is not None:
        print(ret.key)

    n4 = Node()
    n4.key = 4

    print("-"*10)
    list_insert(linked_list, n4)
    list_print(linked_list)