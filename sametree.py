# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            elif p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False
        return dfs(p, q)

P = [1,1,1]
Q = [1,1,1]

p = TreeNode(P[0])
p.left = TreeNode(P[1])
p.right = TreeNode(P[2])

q = TreeNode(Q[0])
q.left = TreeNode(Q[1])
q.right = TreeNode(Q[2])

s= Solution()
print(s.isSameTree(p,q))
