class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        oddEven = 0
        flag = False if nums[0]%2==1 else True

        for x in nums:
            if x%2==0:
                even+=1
                if flag is True:
                    flag = False
                    oddEven+=1
            else:
                odd+=1
                if flag is False:
                    flag=True
                    oddEven+=1
        return max(odd,even,oddEven)



        # parity0 = [0]*len(nums)
        # parity1 = [0]*len(nums)

        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if (nums[i]+nums[j])%2==0:
        #             parity0[i]=max(parity0[i],1+parity0[j])
        #         else:
        #             parity1[i]=max(parity1[i],parity1[j]+1)
        # return max(max(parity0),max(parity1)) + 1
        