class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        tuples = sorted(
            [(index,score[index]) for index in range(N)],
            key = lambda x : x[1],
            reverse = True
            )

        output = [0]*N

        for rank, (index, _) in enumerate(tuples[0:]):

            ranks = {
                1:"Gold Medal",
                2: "Silver Medal",
                3:"Bronze Medal"
            }

            output[index] = str(ranks.get(rank+1,str(rank+1)))
        
        return output

