class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
    
        for i, n in enumerate(nums):
            req = target - n
            if req in myDict:
                return [i, myDict[req]]
            myDict[n]=i
        