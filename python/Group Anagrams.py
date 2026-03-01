class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps=defaultdict(list)
        for word in strs:
            sorted_words="".join(sorted(word))
            maps[sorted_words].append(word)
        return list(maps.values())
        
