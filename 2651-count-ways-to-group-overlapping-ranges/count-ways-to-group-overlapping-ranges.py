class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key= lambda x: (x[0], x[1]))

        last_range = ranges.pop(0)
        count = 1

        while ranges:
            range_to_append = ranges.pop(0)

            if last_range[1] >= range_to_append[0]:
                last_range[1] = max(range_to_append[1], last_range[1])
            else:
                last_range = range_to_append
                count+=1
        

        return (2**count) % (10**9 + 7)

        
        