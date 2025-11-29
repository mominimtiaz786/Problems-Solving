class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)

        result = max_p = min_p = nums[0]

        for i in range(1,N):

            nums_to_compare = [nums[i], nums[i]*max_p, nums[i]*min_p]
            max_p, min_p = max(nums_to_compare), min(nums_to_compare)

            result = max(result, max_p, min_p)
        
        return result

