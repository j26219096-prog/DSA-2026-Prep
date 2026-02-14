class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        max_=0
        while left<right:
            width=right-left
            c_length=min(height[left],height[right])
            max_=max(max_,width*c_length)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_
