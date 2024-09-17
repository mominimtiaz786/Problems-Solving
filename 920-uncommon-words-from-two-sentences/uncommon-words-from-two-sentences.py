class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash_table = {}

        for word in s1.split():
            hash_table[word] =  hash_table.get(word, 0) + 1
        
        for word in s2.split():
            hash_table[word] =  hash_table.get(word, 0) + 1
        
        return [
            word
            for word, count in hash_table.items()
            if count == 1
        ]