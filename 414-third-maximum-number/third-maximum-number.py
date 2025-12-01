class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        N = len(nums)

        if N<3: return nums[0]


        count=1
        for i in range(1, N):
            if nums[i]!=nums[i-1]:
                count+=1
            
            if count == 3:
                return nums[i]
                    


        return nums[0]