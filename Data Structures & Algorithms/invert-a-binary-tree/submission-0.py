# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        ret = TreeNode(root.val)
        def helper(ro):
            if ro.right and ro.left:
                return TreeNode(ro.val, helper(ro.right), helper(ro.left))
            elif ro.right:
                return TreeNode(ro.val, helper(ro.right), None) 
            elif ro.left:
                return TreeNode(ro.val, None, helper(ro.left))
            else:
                return TreeNode(ro.val)
        if root.right:
            ret.left = helper(root.right)
        if root.left:
            ret.right = helper(root.left)
        return ret
