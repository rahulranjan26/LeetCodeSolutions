from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj = [[] for _ in range(V)]
        inDegrees = [0]*V
        ans = []
        
        for u, v in edges:
            adj[u].append(v)
            inDegrees[v] += 1
        
        queue = deque()
        for i in range(V):
            if inDegrees[i] == 0:
                queue.append(i) 
        
        while queue:
            
            node = queue.popleft()
            ans.append(node)
            
            for nbr in adj[node]:
                inDegrees[nbr]-=1
                if inDegrees[nbr]==0:
                    queue.append(nbr)
        
        if len(ans) != V:
            return []
        return ans
            
        