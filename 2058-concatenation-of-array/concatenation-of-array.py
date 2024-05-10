class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = nums.copy()
        for n in nums:
            output.append(n)
        
        return output