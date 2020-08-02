# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

class Solution:
    
    def _helper(self, postorder: List[int], inorder_map: Dict[int, int], left: int, right: int) -> TreeNode:
        if left == right:
            return None
        
        root_val = postorder[self.head]
        root = TreeNode(root_val)
        
        pivot = inorder_map[root_val]
        self.head -= 1
        
        root.right = self._helper(postorder, inorder_map, pivot + 1, right)
        root.left = self._helper(postorder, inorder_map, left, pivot)
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.head = len(postorder) - 1
        inorder_map = {val : i for i, val in enumerate(inorder)}
        return self._helper(postorder, inorder_map, 0, len(inorder))