class Solution:
    #Kandan algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        ans = nums[0]

        curr = 0
        for i in range(N):
            curr = max(curr + nums[i], nums[i])
            ans = max(ans, curr)

            
        return ans

