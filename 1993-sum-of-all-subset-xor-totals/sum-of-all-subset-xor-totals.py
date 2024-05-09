class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        xorSum = 0

        def backTrack(XOR,index):
            nonlocal xorSum 
            if index == N:  return

            for i in range(index,N):
                curr = XOR ^ nums[i]
                xorSum+=curr
                backTrack(curr, i+1)

        backTrack(0,0)
        return xorSum