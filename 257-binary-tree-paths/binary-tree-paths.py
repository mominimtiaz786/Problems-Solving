# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if not root:    return paths

        def traverse(root, currPath):
            if root.right or root.left:    
                if root.left:   traverse(root.left, currPath+"->"+str(root.left.val))
                if root.right:   traverse(root.right, currPath+"->"+str(root.right.val))
            else:
                paths.append(currPath)
        
        traverse(root, str(root.val))
        return paths