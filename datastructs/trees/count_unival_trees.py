class Solution:
    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def is_unival(self, root):
        return self.is_unival_helper(root, root.value)

    def is_unival_helper(self, root, value):
        if root is None:
            return True

        elif root.value == value:
            return self.is_unival_helper(root.left, value) and \
                   self.is_unival_helper(root.right, value)

        return False

    def count_unival(self, root):
        if root is None:
            return 0

        left = self.count_unival(root.left)
        right = self.count_unival(root.right)

        return 1 + left + right if self.is_unival(root) else left + right