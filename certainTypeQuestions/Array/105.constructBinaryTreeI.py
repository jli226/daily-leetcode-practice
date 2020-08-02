# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = None
        d_in = {num:i for i,num in enumerate(inorder)}
        stack = []
        for ele in preorder:
            node = TreeNode(ele)
            if not root: root = node
            if stack:
                if d_in[ele] < d_in[stack[-1].val] :
                    stack[-1].left = node
                else:
                    while stack and d_in[ele] > d_in[stack[-1].val]:
                        parent = stack.pop()
                    parent.right = node
            stack.append(node)
        return root