class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def mir(left,right):
            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False
            return mir(left.left,right.right)and mir(left.right,right.left)
        return mir(root.left,root.right)
