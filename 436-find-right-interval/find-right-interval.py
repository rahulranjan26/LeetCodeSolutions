class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervalDict = {}
        for i in range(len(intervals)):
            x,y = intervals[i]
            intervalDict[x]=i
        
        xPoints = []
        for i in range(len(intervals)):
            xPoints.append(intervals[i][0])
        xPoints.sort()
        
        ans= []
        for x,y in intervals:
            temp = self.findFloor(xPoints,y)
            # print(temp)
            if temp!=-1:
                ans.append(intervalDict[xPoints[temp]])
            else:
                ans.append(-1)
        return ans
        
        
    
    def findFloor(self,arr,target):
        lo = 0
        hi = len(arr)-1
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
            