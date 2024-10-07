class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))

        hashmap = {ele: i+1 for i, ele in enumerate(sorted_arr)}

        return [
           hashmap[ele]
           for ele in arr 
        ]
