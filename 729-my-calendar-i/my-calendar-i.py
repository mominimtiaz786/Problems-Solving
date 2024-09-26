class MyCalendar:

    def __init__(self):
        self.intervals = []        

    def book(self, start: int, end: int) -> bool:
        N = len(self.intervals)
        if not N:
            self.intervals.append((start, end))
            return True
        
        # booking check 
        for i, interval in enumerate(self.intervals):
            if interval[0] <= start and start < interval[1]:
                return False
            elif interval[0] <  end and end <= interval[1]:
                return False
            elif start <= interval[0] and end >= interval[1]:
                return False
            

        self.intervals.append((start,end))
        self.intervals.sort(key=lambda x: x[0])
        return True







# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)