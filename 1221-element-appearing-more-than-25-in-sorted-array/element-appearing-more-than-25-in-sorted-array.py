class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 3:  return arr[0]

        reqCount = n//4
        candidates = {arr[i]: i for i in range(n-1, -1, -reqCount)}

        for candidate in candidates:
            i = candidates.get(candidate)
            while i!=0 and candidate  == arr[i-1]:  i-=1
            
            count = 0
            while  i != n and candidate  == arr[i]:
                count+=1
                i+=1

            if count>reqCount:  return candidate
