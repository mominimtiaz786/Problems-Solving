class Solution:
    #Kandan algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        ans = nums[0]

        curr = 0
        for i in range(N):
            if curr + nums[i] > nums[i]:
                curr+=nums[i]
            else:
                curr = nums[i]
            ans = max(ans, curr)

            
        return ans

