class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node

        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
        
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root