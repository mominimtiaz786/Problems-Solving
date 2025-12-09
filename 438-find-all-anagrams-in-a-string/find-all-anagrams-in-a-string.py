class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        NP = len(p)
        NS = len(s)
        if NS < NP:   return []
        ans = []

        sliding_freq = {ch:0 for ch in s}
        p_freq = {ch:0 for ch in s+p}
        for ch in p:    p_freq[ch]+=1

        i=0
        for j in range(NS):
            sliding_freq[s[j]]+=1

            if j>= NP:
                sliding_freq[s[i]]-=1
                i+=1
                
            if sliding_freq == p_freq:
                ans.append(i)

        return ans


        