# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:    return []

        is_child = not root.left and not root.right

        if targetSum == root.val and is_child:
            return [[root.val]]
        


        paths = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)

        return [
            [root.val]+path for path in paths
        ]