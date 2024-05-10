class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pairs = []
        N = len(arr)
        for i in range(N-1):
            for j in range(i+1, N):
                pairs.append((arr[i], arr[j]))
        
        pairs.sort(
            key = lambda x : x[0] / x[1]
        )
        return pairs[k-1]