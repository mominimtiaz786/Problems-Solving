class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix_product, suffix_product = 1,1
        resultant_array = [1]*N

        i,j=1,N-2

        while i<N:
            prefix_product = prefix_product*nums[i-1]
            resultant_array[i] = resultant_array[i]*prefix_product

            suffix_product = suffix_product*nums[j+1]
            resultant_array[j]= resultant_array[j]*suffix_product
            i+=1
            j-=1



        return resultant_array


