import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        selectedK = heapq.nlargest(k, happiness)
        total = 0
        for i in range(k):
            if selectedK[i] - i <= 0:   break
            total+=(selectedK[i] - i)
        
        return total