# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        node = self.dfs(root,ans,to_delete)
        if node:
            ans.append(node)
        return ans
    
    def dfs(self,root,ans,to_delete):
        if root is None:
            return None
        root.left = self.dfs(root.left,ans,to_delete)
        root.right = self.dfs(root.right,ans,to_delete)
        if root.val in to_delete:
            if root.left is None and root.right is None:
                return None
            else:
                if root.left!=None:
                    ans.append(root.left)
                if root.right!=None:
                    ans.append(root.right)
                return None
        return root
        