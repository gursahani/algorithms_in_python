import random, sys


class BST:
    """
Simple binary search tree implementation.
This BST supports insert, find, and delete-min operations.
Each tree contains some (possibly 0) BSTnode objects, representing nodes,
and a pointer to the root.
"""

    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key t into this BST, modifying it in-place."""
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    # Go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left

                    if self.root.heightDifference() == 2:
                        if t <= self.rotateRight():
                            new = self.roo
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def __contains__(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return True
                # return node.key
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def removeNode(self, t):
        node = self.root

        def removeHelper(node, t):
            if t < node.key:
                node.left = removeHelper(node.left, t)
            elif t > node.key:
                node.right = removeHelper(node.right, t)
            elif t == node.key:
                if node.left is None:
                    return node.right

                child = node.left
                while child.right:
                    child = child.right
                if child:
                    childKey = child.key
                    node.left = removeHelper(node.left, childKey)
                    node.key = childKey

            return node

        return removeHelper(node, t)

    def findMin(self):
        node = self.root
        min_ = 1000
        while node is not None:
            if min_ > node.key:
                min_ = node.key
            node = node.left
        return min_

    def findMax(self):
        node = self.root
        # max_ = -1000
        # while node is not None:
        #     if max_ < node.key:
        #         max_ = node.key
        #     node = node.right

        def findMaxHelper(node):
            if node.right is None:
                return node.key
            return findMaxHelper(node.right)

        return findMaxHelper(node)

    def closest(self, num):
        if self.root is None:
            return None
        node = self.root
        best = node
        distance = abs(num - node.key)

        while node:
            if abs(node.key - num) < distance:
                best = node
                distance = abs(node.key - num)

            if num < node.key:
                node = node.left
            elif num > node.key:
                node = node.right
            else:
                return num
        return best.key

    def __sizeof__(self):
        def size(node):
            if node is None:
                return 0
            else:
                return size(node.left) + 1 + size(node.right)

        node = self.root
        return size(node)

    def max_depth(self):
        def maxDepth(node):
            if node is None:
                return 0
            else:
                lDepth = maxDepth(node.left)
                rDepth = maxDepth(node.right)

                return max(lDepth, rDepth) + 1

        return maxDepth(self.root)

    def delete_min(self):
        """Delete the minimum key (and return the old node containing it)."""
        if self.root is None:
            return None, None
        else:
            # Walk to leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree.
            if node.parent is not None:
                node.parent.left = node.right
            else:  # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

    def __str__(self):
        if self.root is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                    node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])

    def printTree(self):
        def print_tree(node):
            if node is None:
                return node
            else:
                print_tree(node.left)
                print(node.key)
                print_tree(node.right)

        node = self.root
        print_tree(node)

    def printPostOrder(self):
        def print_tree1(node):
            if node is None:
                return
            else:
                print_tree1(node.left)
                print_tree1(node.right)
                print(node.key)

        node = self.root
        print_tree1(node)

    def hasPathSum(self, total):
        def pathSum(node, target):
            if node is None:
                return False

            if node.key == target:
                if node.left is None and node.right is None:
                    return True
                else:
                    return pathSum(node.left, 0) or pathSum(node.right, 0)
            else:
                leftover = target - node.key
                return pathSum(node.left, leftover) or pathSum(node.right, leftover)

        node = self.root
        return pathSum(node, total)

    def printPaths(self):
        def listOfPaths(node, out, arr):
            if node is None:
                arr.append(out)
                out.clear()

            while node is not None:
                out.append(node.key)
                listOfPaths(node.left, out, arr)
                listOfPaths(node.right, out, arr)

            return arr

        return listOfPaths(self.root, [], [])
        # return outArr

    def mirror(self):
        def returnMirror(node):
            if node is None:
                return None
            if node is not None:
                temp = node.left
                node.left = node.right
                node.right = temp

            returnMirror(node.left)
            returnMirror(node.right)

        node = self.root
        returnMirror(node)

    def doubleTree(self):
        def createDoubleTree(node):
            if node is None:
                return

            createDoubleTree(node.left)
            createDoubleTree(node.right)
            oldLeft = node.left
            node.left = BSTnode(node.key)
            node.left.left = oldLeft

        createDoubleTree(self.root)

    def isSame(self, node1, node2):
        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            sameTree(node1.left, node2.left)
            sameTree(node1.right, node2.right)

            return False

        return sameTree(node1, node2)





    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v

class BSTnode:
    """
Representation of a node in a binary search tree.
Has a left child, right child, and key value.
"""

    def __init__(self, t):
        """Create a new leaf with key t."""
        self.key = t
        self.disconnect()

    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0


    def computeHeight(self):
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1


    def heightDifference(self):
        leftTarget = 0
        rightTarget = 0
        if self.left:
            leftTarget = 1 + self.left.height
        if self.right:
            rightTarget = 1 + self.right.height

        return leftTarget - rightTarget


    # def rotateLeft

    def inorder(self):
        if self.left:
            for v in self.inorder():
                yield v

        yield self.key

        if self.right:
            for v in self.inorder():
                yield v


if __name__ == '__main__':
    items = [1, 3, -1, 5, 2, 9]

    tree = BST()
    # tree.inorder()
    for item in items:
        tree.insert(item)

    print(tree)
    print("postorder ", tree.printPostOrder())

    print("has sum , ", tree.hasPathSum(4))
    # print(tree.printPaths())
    # print("mirror ", tree.mirror())
    # print("doubletree \n", tree.doubleTree())
    print(tree)
    print("max is ", tree.findMax())
    tree.removeNode(-1)
    print(tree)
    # for i in tree:
    #     print(t)
    # print(tree2.isSame(tree2, tree))
