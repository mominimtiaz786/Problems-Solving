class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N= len(nums)
        currSum = sum(nums[:k])
        maxSum = currSum

        for i in range(k,N):
            currSum = currSum - nums[i-k] + nums[i]
            maxSum = max(maxSum, currSum)
        
        return maxSum/k