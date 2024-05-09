class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        allXORs = []

        def backTrack(XOR,index):
            if index == N:  return

            for i in range(index,N):
                curr = XOR ^ nums[i]
                allXORs.append(curr)
                backTrack(curr, i+1)
                
        backTrack(0,0)
        return sum(allXORs)