class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def helper(n, curr):
            if curr > n:    return []

            result = []
            for i in range(10):
                if curr + i > n: break
                if not curr + i: continue
                result+=[curr+i]
                result+=helper(n, (curr+i) * 10)

            return result

        return helper(n, 0)