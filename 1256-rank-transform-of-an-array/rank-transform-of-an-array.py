class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        hashmap = {}

        rank = 1
        for ele in sorted_arr:
            if not ele in hashmap:
                hashmap[ele] = rank
                rank+=1
        
        return [
           hashmap[ele]
           for ele in arr 
        ]
