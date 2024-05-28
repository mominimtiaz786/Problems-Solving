class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        costArray = [
            abs(ord(s[i]) - ord(t[i]))
            for i in range(N)
        ]

        maxLength = 0
        l = 0
        currentCost = 0

        for r in range(N):
            currentCost += costArray[r]
            while currentCost > maxCost:
                currentCost -= costArray[l]
                l += 1
            maxLength = max(maxLength, r - l + 1)

        return maxLength
