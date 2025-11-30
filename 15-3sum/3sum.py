class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)

        nums.sort()

        for i in range(N-2):

            if nums[i] > 0: break
            if i and nums[i-1] == nums[i]:  continue

            target = -nums[i]

            j = i+1
            k = N-1

            while j<k:
                
                if nums[j] + nums[k] == target:
                    ans.append([-target, nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                    
                elif nums[j] + nums[k] < target:
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                else:
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                
        return ans
        