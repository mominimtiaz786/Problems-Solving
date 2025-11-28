class Solution:
    #Brute Force -> Time Limit Exceeding
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        ans = float('-inf')

        curr = 0
        for i in range(N):
            if curr + nums[i] > nums[i]:
                curr+=nums[i]
            else:
                curr = nums[i]
            ans = max(ans, curr)

            
        return ans


    def maxSubArray1(self, nums: List[int]) -> int:
        N = len(nums)

