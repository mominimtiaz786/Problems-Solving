class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()
        MAX_N = 2**31 

        while n not in my_set and n<MAX_N:
            if n == 1:  return True
            my_set.add(n)

            x = n
            n = 0
            while x:
                n+=((x%10)**2)
                x//=10


        return False

        