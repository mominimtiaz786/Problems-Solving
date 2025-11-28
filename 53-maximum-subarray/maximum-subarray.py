class Solution:
    #Brute Force -> Time Limit Exceeding
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        ans = float('-inf')

        curr = 0
        for i in range(N):
            curr = curr+nums[i] if curr + nums[i] > nums[i] else nums[i]
            ans = max(ans, curr)

            
        return ans


    def maxSubArray1(self, nums: List[int]) -> int:
        N = len(nums)

