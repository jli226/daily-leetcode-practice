# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# Follow up: Solve it both recursively and iteratively.

# Recursive solution:
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.equals(root.left, root.right)

    def equals(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2 and node1.val == node2.val:
            return self.equals(node1.left, node2.right) and self.equals(node1.right, node2.left)
        else:
            return False


# Non-Recursive solution :

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        stack = []
        stack.append((root.left, root.right))

        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

        return True
