class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key= lambda x: (x[0], x[1]))

        non_overlapping_ranges = [ranges.pop(0)]

        while ranges:
            range_to_append = ranges.pop(0)

            if non_overlapping_ranges[-1][1] >= range_to_append[0]:
                non_overlapping_ranges[-1][1] = max(range_to_append[1], non_overlapping_ranges[-1][1])
            else:
                non_overlapping_ranges.append(range_to_append)
        
        count = len(non_overlapping_ranges)

        return (2**count) % ((10**9) + 7)

        
        