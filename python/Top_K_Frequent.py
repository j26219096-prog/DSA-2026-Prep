class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map={}
        for num in nums:
            count_map[num]=count_map.get(num,0)+1
        sorts=sorted(count_map.items(),key=lambda x :x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorts[i][0])
        return result
