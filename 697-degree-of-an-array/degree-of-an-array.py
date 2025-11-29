class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        frequency = {num: 0 for num in nums}


        for num in nums:    frequency[num]+=1
        

        max_freq = max(list(frequency.values()))
        if max_freq == 1:   return 1
        
        max_freq_elems = [num for num, freq in frequency.items() if freq == max_freq]


        sub_array_length = float('inf')
        for max_freq_num in max_freq_elems:
            i = 0
            while nums[i] != max_freq_num:
                i+=1
            
            count = 0
            start = i
            while count <  max_freq:
                if nums[i] == max_freq_num:
                    count+=1
                i+=1
            

            sub_array_length = min(i - start, sub_array_length)

        return sub_array_length





        