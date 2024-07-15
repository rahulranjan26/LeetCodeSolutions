class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaderBoard = {}
        self.candidates = {}
        self.leader = -1
        self.maxVotes = -1
        self.createLeaderBoard()
        # print(self.leaderBoard)
    def createLeaderBoard(self):
        for i in range(len(self.persons)):
            if self.persons[i] in self.candidates:
                self.candidates[self.persons[i]]+=1
            else:
                self.candidates[self.persons[i]]=1
            if self.maxVotes<=self.candidates[self.persons[i]]:
                self.maxVotes = self.candidates[self.persons[i]]
                self.leader = self.persons[i]
                self.leaderBoard[self.times[i]]=self.leader
            else:
                self.leaderBoard[self.times[i]]=self.leader
    def q(self, t: int) -> int:
        return self.leaderBoard[self.findTheLeastTime(t)]
    
    def findTheLeastTime(self,t):
        lo = 0
        hi = len(self.times)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            if self.times[mid]==t:
                return t
            elif self.times[mid]>t:
                hi = mid-1
            else:
                lo = mid+1
        
        return self.times[hi]
            
            
            
            
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
