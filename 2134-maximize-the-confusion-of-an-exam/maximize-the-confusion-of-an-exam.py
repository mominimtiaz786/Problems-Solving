class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        if N <= 2:  return N

        max_count = 0
        for elem in ['F','T']:
            i = 0
            wrong = 0   

            for j, ch in enumerate(answerKey):
                if ch != elem:
                    wrong += 1

                while wrong > k:
                    if answerKey[i] != elem:
                        wrong -= 1
                    i += 1

                max_count = max(max_count, j - i + 1)            

        return max_count