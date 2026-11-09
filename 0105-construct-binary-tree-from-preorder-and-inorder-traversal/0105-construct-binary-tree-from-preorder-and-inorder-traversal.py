# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def solve(preorder,inorder,start,end,idx):
            if start > end :
                return None
            root = preorder[idx[0]]
            i = start
            while i <= end :
                if inorder[i] == root:
                    break
                i = i+1   
            idx[0] = idx[0] + 1
            root = TreeNode(root)
            root.left = solve(preorder,inorder,start,i-1,idx)    
            root.right = solve(preorder,inorder,i+1,end,idx)    
            return root
        idx = [0]
        return solve(preorder,inorder,0,len(inorder)-1,idx)    
 

        