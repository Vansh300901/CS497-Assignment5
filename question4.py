# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        returnList = []
        returnList.append(root.val)


        def recursiveDFS(root):
            if root is None:
                return 0
            
            left = recursiveDFS(root.left)
            left = max(0, left)

            right = recursiveDFS(root.right)
            right = max(0, right)

            returnList[0] = max(left + right + root.val, returnList[0])

            return (root.val + max(left, right))

        recursiveDFS(root)
        return returnList[0]

        
        