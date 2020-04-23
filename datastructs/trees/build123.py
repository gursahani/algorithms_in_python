class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build123():
    lchild = Node(1)
    rchild = Node(3)
    parent = Node(2)
    parent.left = lchild
    parent.right = rchild
    return parent


if __name__ == '__main__':
    parent = build123()

    def traverse(parent):
        if parent is None:
            return parent
        else:
            traverse(parent.left)
            print(parent.val)
            traverse(parent.right)