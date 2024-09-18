class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums_dict = {}

        for n in nums:
            nums_dict[n] = nums_dict.get(n,0) + 1
        
        req_str = ''

        while nums_dict:
            largest = "0"

            for n in nums_dict:
                largest = largest if largest + n > n + largest else n
            
            req_str+=largest
            nums_dict[largest]-=1

            if not nums_dict[largest]:
                del nums_dict[largest]
        

        return str(int(req_str))
