class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)

        placed = 0
        for i in range(0,N,2):
            if flowerbed[i] == 0 and (not i or flowerbed[i-1] == 0) and (i+1 == N or flowerbed[i+1] == 0):
                placed+=1

        if placed >= n: return True


        placed = 0
        for i in range(1,N,2):
            if flowerbed[i] == 0 and (flowerbed[i-1] == 0) and (i+1 == N or flowerbed[i+1] == 0):
                placed+=1

        return  placed >= n
