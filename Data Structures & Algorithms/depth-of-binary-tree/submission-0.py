# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, depth):
            if not root:
                return 0
            if not (root.left or root.right):
                return depth
            ldis = depth
            rdis = depth
            if root.left:
                ldis = helper(root.left, depth + 1)
            if root.right:
                rdis = helper(root.right, depth + 1)
            return max(ldis, rdis)
        return helper(root,1)