class MedianFinder:
    def __init__(self):
        self.nums = []
        self.l = 0
        self.r = 0

    def addNum(self, num: int) -> None:
        if self.nums:
            if self.l != self.r:
                self.l+=1
            else:
                self.r+=1
            self.insertElement(num)
        else:
            self.nums.append(num)

    def insertElement(self, elem):
        N = len(self.nums)
        l,r = 0, N - 1

        while l <= r:
            mid = (l+r)//2
            if elem <= self.nums[mid] and (not mid or elem > self.nums[mid-1]):
                self.nums.insert(mid,elem)
                return

            elif elem >= self.nums[mid] and (mid+1==N or elem < self.nums[mid+1]):
                self.nums.insert(mid+1,elem)
                return

            elif elem < self.nums[mid]:
                r = mid -1
            else:
                l = mid+1

    def findMedian(self) -> float:
        return (self.nums[self.l] + self.nums[self.r])/2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()