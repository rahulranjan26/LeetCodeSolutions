class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = [(self.findDigitSum(nums[i]), nums[i], i) for i in range(len(nums))]
        arr.sort(key=lambda x: (x[0], x[1]))

        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue
            j = i
            clen = 0
            while not visited[j]:
                visited[j] = True
                clen += 1
                j = arr[j][2]
            ans += clen - 1
        return ans

    def findDigitSum(self, number):
        ans = 0
        while number > 0:
            ans += number % 10
            number //= 10
        return ans
