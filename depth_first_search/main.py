class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        node = Node(name)
        self.children.append(node)
        return node

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            array = child.depthFirstSearch(array)
        return array

    def children_names(self):
        return [x.name for x in self.children]


def update_addresses(node, address):
    address.update({node.name: node})
    return address

def add_children(parent, children, address):
    for i in children:
        node = parent.addChild(i)
        address = update_addresses(node, address)
    return address

def construct_example():
    structure = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'D': ['G', 'H'],
        'F': ['I', 'J'],
        'G': ['K']
    }
    root = None
    addresses = {}
    for node_name, children in structure.items():
        if node_name in addresses:
            node = addresses[node_name]
        else:
            node = Node(node_name)
        addresses = add_children(node, children, addresses)
        if root is None:
            root = node
    
    return addresses, root

address, root = construct_example()

# for name, obj in address.items():
#     print(name, obj.children_names())
print(root.depthFirstSearch(array=[]))