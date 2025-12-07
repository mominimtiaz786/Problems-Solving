class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            freq_map = [0]*26
            for k in s: 
                freq_map[ord(k)-ord('a')]+=1
            
            key = tuple([(i,n) for i,n in enumerate(freq_map) if n])
            if key not in hashmap:
                hashmap[key]=[]

            hashmap[key].append(s)

        return list(hashmap.values())

        