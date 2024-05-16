class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:  return 1
        if n == 1:  return x

        if n < 0:   
            x = 1/x
            n = -1 * n
        
        val = self.myPow(x, n//2)
        return val * val if n % 2 == 0 else val * val * x  

        