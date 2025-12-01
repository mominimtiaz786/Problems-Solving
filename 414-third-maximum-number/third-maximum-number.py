class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)
        N = len(nums)

        return nums[0] if N < 3 else nums[2]
        