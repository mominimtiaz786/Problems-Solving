class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [-1] * (2*N)
        for i in range(N):
            output[i] =  output[i+N] = nums[i]
        return output