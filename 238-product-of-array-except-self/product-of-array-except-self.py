class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix_product = 1
        suffix_product = 1
        resultant_array = [1]*N


        for i in range(1, N):
            prefix_product = prefix_product*nums[i-1]
            resultant_array[i] = resultant_array[i]*prefix_product

            suffix_product = suffix_product*nums[N-i]
            resultant_array[N-i-1]= resultant_array[N-i-1]*suffix_product



        return resultant_array


