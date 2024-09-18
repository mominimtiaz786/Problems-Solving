class Solution:
    def findGreater(self, n1, n2):
        s1,s2 = str(n1), str(n2)
        
        return n1 if s1+s2 > s2+s1 else n2


    def largestNumber(self, nums: List[int]) -> str:
        nums_dict = {}

        for n in nums:
            nums_dict[n] = nums_dict.get(n,0) + 1
        
        req_str = ''

        while nums_dict:
            largest = -1

            for n in nums_dict:
                largest = self.findGreater(n, largest)
            
            req_str+=str(largest)
            nums_dict[largest]-=1

            if not nums_dict[largest]:
                del  nums_dict[largest]
        

        return str(int(req_str))