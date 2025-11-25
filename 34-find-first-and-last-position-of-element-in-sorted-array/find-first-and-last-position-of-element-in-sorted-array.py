class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        start, end = 0, N-1
        l,r = 0, N-1

        if not N or target < nums[l] or target> nums[r]:
            return [-1,-1]


        def _searchTarget(left, right, target):
            while left <= right:
                mid = (left+right) // 2

                if target == nums[mid]:
                    return mid
                
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            
            return -1

        
        result = _searchTarget(start, end, target)
        print("POINT1",result)
        if result == -1:    return [-1, -1]


        def _findSmaller(left, right, target):
            while left<=right:
                mid = (left+right) // 2
                if target == nums[mid] and (mid==0 or nums[mid-1]<target):
                    return mid
                
                elif nums[mid] < target:
                    left = mid+1
                
                else:
                    right = mid-1
            
            return right
            

        range_start = _findSmaller(start, result, target)
        
        def _findLarger(left, right, target):
            while left<=right:
                mid = (left+right) // 2
                if target == nums[mid] and (mid+1==N or nums[mid+1]>target):
                    return mid
                
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1

            return left
        range_end = _findLarger(result, end, target)


        return [range_start, range_end]
