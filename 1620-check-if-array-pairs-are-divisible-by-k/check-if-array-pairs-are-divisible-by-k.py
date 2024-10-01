class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        hashmap = [0]*k
        
        for x in arr:
            hashmap[(x % k)]+=1
        

        for i in range(1, k//2 + 1):
            if hashmap[i] != hashmap[k-i]:
                return False

        return hashmap[0] % 2 == 0
        