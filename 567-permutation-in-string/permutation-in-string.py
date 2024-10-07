class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = {}
        for c in s1:    hashMap[c] = hashMap.get(c,0)+1
            

        n = len(s1)
        for k in range(len(s2)-n+1):
            hashMap2= {}
            for c in s2[k:k+n]:
                hashMap2[c] = hashMap2.get(c,0)+1
            if hashMap == hashMap2:
                return True
        return False
        