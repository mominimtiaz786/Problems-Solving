class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)

        l,r = 0, N-1
        if nums[l] < nums[r] or N == 1: return nums[l]

        while l<=r:
            mid = (l+r)//2

            if mid+1 < N and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            elif mid and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            elif nums[mid] < nums[0]:
                r = mid-1
            
            else:
                l=mid+1
        
        return -1




        