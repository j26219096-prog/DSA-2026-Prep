class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        
        
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

       
        for u, v in edges:
            root1 = find(u)
            root2 = find(v)
            
            
            if root1 == root2:
                return [u, v]
            
            
            parent[root1] = root2
