# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(root1=node, root2=node):
            if root1 is None and root2 is None:
                return True
            if (root1 is not None and root2 is not None):
                if root1.val == root2.val:
                    return (isMirror(root1.left, root2.right)and isMirror(root1.right, root2.left))
            return False
        return isMirror(node,node)

root = [1,2,2,3,4,4,3]
node = TreeNode(root[0])
node.left = TreeNode(root[1])
node.right = TreeNode(root[2])
node.left.left = TreeNode(root[3])
node.left.right = TreeNode(root[4])
node.right.left = TreeNode(root[5])
node.right.right = TreeNode(root[6])

s = Solution()
print(s.isSymmetric(node))
