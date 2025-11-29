class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)

        result = max_p = min_p = nums[0]

        for i in range(1,N):
            # if max_p < min_p:
            #     min_p, max_p = max_p, min_p
            # if nums[i] < 0:
                # min_p, max_p = max_p, min_p

            c_max = max(nums[i], nums[i]*max_p, nums[i]*min_p)
            c_min = min(nums[i], nums[i]*min_p, nums[i]*max_p)

            max_p, min_p = c_max, c_min

            result = max(result, max_p, min_p)
        
        return result

