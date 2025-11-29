class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)

        result = max_p = min_p = nums[0]

        for i in range(1,N):
            if nums[i] < 0:
                min_p, max_p = max_p, min_p

            max_p = max(nums[i], nums[i]*max_p)
            min_p = min(nums[i], nums[i]*min_p)

            result = max(result, max_p)
        
        return result

