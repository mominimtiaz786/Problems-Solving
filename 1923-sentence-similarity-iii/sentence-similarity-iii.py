class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:  return True
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')

        minLen = min(len(words1), len(words2))
        longest_common_prefix = []
        longest_common_suffix = []

        for i in range(minLen):
            if words1[i] == words2[i]:
                longest_common_prefix.append(words1[i])
            else:
                break
        
        for i in range(1, minLen+1):
            if words1[-1*i] == words2[-1*i]:
                longest_common_suffix.append(words1[-1*i])
            else:
                break


        return minLen <= len(longest_common_prefix) + len(longest_common_suffix) 