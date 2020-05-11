# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root


Maybe make it four lines for better readability:


def invertTree(self, root):
    if root:
        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left)
        return root


And an iterative version using my own stack:


def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root
