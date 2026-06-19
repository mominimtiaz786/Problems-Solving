class Solution:
    FACTORIALS = [1]

    def get_factorial(self,n):
        L =len(self.FACTORIALS) 
        if L<n+1:
            for i in range(L, n+1):
                self.FACTORIALS.append(
                    self.FACTORIALS[-1] * i
                    )
        return self.FACTORIALS[n]


    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        numbers_set = set([i+1 for i in range(n)])
        N = n
        
        def helper(n,k):
            if N == len(ans):
                return
    
            fact = self.get_factorial(n-1)
    
            choosen_index = 0
            while k > fact:
                choosen_index+=1
                k-=fact
            choosen_number = list(numbers_set)[choosen_index]
            ans.append(choosen_number)
            n-=1
            numbers_set.remove(choosen_number)
            
            return helper(n,k)
        
        helper(n,k)

        return "".join([str(x) for x in ans])