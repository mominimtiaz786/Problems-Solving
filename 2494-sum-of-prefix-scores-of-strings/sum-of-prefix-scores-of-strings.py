class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        counter_dict = {}

        scores = [0]*len(words)
        for word in words:
            for i in range(len(word)):
                prefix = word[:i+1]
                counter_dict[prefix] = counter_dict.get(prefix,0)+1
        
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                prefix = word[:j+1]
                scores[i]+=counter_dict[prefix]
        
        return scores