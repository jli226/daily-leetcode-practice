# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# recursion


def maxDepth(self, root):


if not root:
return 0

return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
Always better to write a similar iterative solution:

    # stack for level order

    def maxDepth(self, root):
        if not root:
            return 0

        tstack, h = [root], 0

        # count number of levels
        while tstack:
            nextlevel = []
            while tstack:
                top = tstack.pop()
                if top.left:
                    nextlevel.append(top.left)
                if top.right:
                    nextlevel.append(top.right)
            tstack = nextlevel
            h += 1
        return h

# queue for level order

    def maxDepth(self, root):
        if not root:
            return 0

        tqueue, h = collections.deque(), 0
        tqueue.append(root)
        while tqueue:
            nextlevel = collections.deque()
            while tqueue:
                front = tqueue.popleft()
                if front.left:
                    nextlevel.append(front.left)
                if front.right:
                    nextlevel.append(front.right)
            tqueue = nextlevel
            h += 1
        return h
