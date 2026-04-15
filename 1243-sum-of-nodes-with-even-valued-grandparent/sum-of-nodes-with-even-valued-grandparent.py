# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        parents = []
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            if node.val % 2 == 0:
                if node.left: parents.append(node.left)
                if node.right: parents.append(node.right)
            inorder(node.right)
        inorder(root)

        ans = 0
        while parents:
            node = parents.pop()
            if node.left: ans+=node.left.val
            if node.right: ans+=node.right.val
        
        return ans