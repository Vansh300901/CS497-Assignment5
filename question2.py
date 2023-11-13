# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        array_list = []

        def inOrder(root):
            if root is None:
                return

            inOrder(root.left)
            array_list.append(root.val)
            inOrder(root.right)

        inOrder(root)

        maxi = float('-inf')

        for index in range(0, len(array_list)-1):
            maxi = max(maxi, abs(array_list[index] - array_list[index+1]))

        return maxi
        