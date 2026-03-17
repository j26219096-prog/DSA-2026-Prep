import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return[]
        res=[]
        q=collections.deque([root])
        while q:
            qlen=len(q)
            for i in range (qlen):
                node=q.popleft()
                if i==qlen-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
