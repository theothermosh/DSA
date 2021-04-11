class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    
def create_tree(root_node, left_node, right_node):
    root_node.left = left_node
    root_node.right = right_node


def pre_order(node):
    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)

    print(node)


def in_order(node):
    if node.left:
        in_order(node.left)

    print(node)

    if node.right:
        in_order(node.right)


#        2
#       / \
#      7   9
#     / \   \
#    1   6   8
#       / \   \
#      3   5   4

if __name__ == "__main__":
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    create_tree(two, seven, nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    three = Node(3)
    five = Node(5)
    six.add_left(three)
    six.add_right(five)
    eight = Node(8)
    nine.add_right(eight)
    four = Node(4)
    eight.add_right(four)
    print("Pre-order: ")
    pre_order(two)
    print("Post-order: ")
    post_order(two)
    print("In-order:")
    in_order(two)