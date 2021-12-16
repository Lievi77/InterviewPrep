# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import math
        # idea set a valid range

        def isBST(root, min=-math.inf, max=math.inf):

            if not root:
                return True

            # valid range check
            if(root.val <= min or root.val >= max):
                return False

            is_left_bst = isBST(root.left, min, root.val)
            is_right_bst = isBST(root.right, root.val, max)

            return is_left_bst and is_right_bst

        # tripwire
        return isBST(root)
