from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        startingPattern = ""
        for i in range(2):
            for j in range(3):
                startingPattern+=str(board[i][j])

        possibleMoves = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        targetPattern = "123450"
        queue = deque()
        queue.append(startingPattern)

        visited = set()

        level = 0
        while queue:
            length = len(queue)
            while length>0:
                pat = queue.popleft()
                if pat==targetPattern:
                    return level
                idx = pat.find('0')
                visited.add(pat)
                for i in possibleMoves[idx]:
                    newPat = self.findNextPat(i,idx,pat)
                    if newPat not in visited:
                        queue.append(newPat)
                
                length-=1
            level+=1
        return -1
    
    def findNextPat(self,index,idx0,pat):
        pat = list(pat)
        pat[index],pat[idx0]=pat[idx0],pat[index]
        return ''.join(pat)




        
        
        