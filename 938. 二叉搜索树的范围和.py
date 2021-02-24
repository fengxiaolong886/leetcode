"""
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(root, low, high):
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
