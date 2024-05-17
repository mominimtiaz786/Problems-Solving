# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def toRemove(root):
            if not root:    return False
            if root.left or root.right:
                if toRemove(root.left) and root.left.val == target:
                    root.left = None

                if toRemove(root.right) and root.right.val == target:
                    root.right = None

            return not root.left and not root.right

        if root and toRemove(root) and root.val == target:
            return None
        
        return root
