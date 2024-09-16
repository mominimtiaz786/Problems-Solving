class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(tp.split(':')[0]) * 60 + int(tp.split(':')[1]) for tp in timePoints]
        timePoints = sorted(timePoints)

        minDifference = 24*60

        N = len(timePoints)
        for i in range(1, N):
            minDifference = min(minDifference, timePoints[i] - timePoints[i-1])
        
        minDifference = min(minDifference, 24*60 - timePoints[N-1] + timePoints[0])

        return minDifference