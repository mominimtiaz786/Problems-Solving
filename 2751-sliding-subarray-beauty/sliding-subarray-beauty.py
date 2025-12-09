class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums) 
        neg_count =0
        freq = {}
        ans = []

        for i,n in enumerate(nums):
            if n < 0:   neg_count+=1
            freq[n] = freq.get(n,0) + 1


            if i>=k:
                elem = nums[i-k]
                freq[elem]-=1
                if elem < 0:    neg_count-=1

            if i+1>=k:            
                if neg_count < x:
                    ans.append(0)
                    continue

                arr = sorted(
                    [(key,val) for key,val in freq.items() if val],
                    key= lambda x: (x[0], x[1])
                )

                j = 0
                xi = x
                while xi > arr[j][1]:
                    xi-=arr[j][1]
                    j+=1
                ans.append(arr[j][0])
                    

        return ans