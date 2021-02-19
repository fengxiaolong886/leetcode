"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""

def isSymmetric(root):
    def dfs(left, right):
        if left and not right:
            return False
        elif not left and right:
            return False
        elif not left and not right:
            return True
        else:
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

    if not root:
        return True

    return dfs(root.left, root.right)
