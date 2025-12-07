class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for s in strs:
            freq_map = [0]*26
            for k in s: 
                freq_map[ord(k)-ord('a')]+=1
            
            key = tuple([(i,n) for i,n in enumerate(freq_map) if n])
            hashmap[key].append(s)

        return list(hashmap.values())

        