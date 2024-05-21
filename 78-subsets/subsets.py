class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        output = []
        for i in range(2**N):
            temporaryOutput = []
            while i:
                elem = math.floor(math.log2(i))
                temporaryOutput.append(nums[elem])
                i^=1<<elem
            output.append(temporaryOutput)
        
        return output