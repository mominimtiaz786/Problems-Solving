class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:

        res = 0
        N = len(nums)
        DIGITS_COUNT = len(str(nums[0])) 


        nums = [str(n) for n in nums]
        
        for k in range(DIGITS_COUNT):
            counts = [0]*10
            for n in nums:
                counts[int(n[k])]+=1

            res+=sum([c*(N-c) for c in counts if c])
        

        return res//2
        