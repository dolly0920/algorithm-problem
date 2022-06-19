import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ## val 0 : no monitoring, 1 : camera, 2 : no camera but monitoring (nearby camera)

        def dfs(node):  ## return 'node - leaf' camera count
            if node is None:  ## leaf case
                return 0
            res = dfs(node.left) + dfs(node.right)

            ## no child node => infinite value
            left_child_state = node.left.val if node.left else sys.maxsize
            right_child_state = node.right.val if node.right else sys.maxsize

            curr_state = min(left_child_state, right_child_state)
            if curr_state == 0:  ## no monitoring
                node.val = 1  ## setup camera
                res += 1
            elif curr_state == 1:  ## monitoring
                node.val = 2  ## update status (no camera, but monitoring)

            return res

        return dfs(root) + (root.val == 0)