import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        res=right
        while left<=right:
            mid=(left+right)//2
            hs=0
            for pile in piles:
                hs+=math.ceil(pile/mid)
            if hs<=h:
                res=min(mid,res)
                right=mid-1
            else:
                left=mid+1
        return res
