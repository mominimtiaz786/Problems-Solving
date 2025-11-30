class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)

        nums.sort()
        hashmap = {num:i for i, num in enumerate(nums)}

        for i in range(N-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]:  continue

            two_sum = -nums[i]

            for j in range(i+1, N-1):
                if j > i+1 and nums[j] == nums[j-1]:    continue

                target = two_sum - nums[j]
                if hashmap.get(target, -1) > j:
                    triplet = [nums[i], nums[j], target]
                    ans.append(triplet)

        
        return ans