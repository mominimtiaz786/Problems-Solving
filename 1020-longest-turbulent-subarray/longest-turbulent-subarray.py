class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1:   return N

        max_size = 1
        curr_size = 1

        smaller = True


        for i in range(N-1):

            if arr[i] < arr[i+1] and smaller:
                curr_size+=1
                smaller = not smaller
            
            elif arr[i] > arr[i+1] and not smaller:
                curr_size+=1
                smaller = not smaller
            
            else:
                max_size = max(max_size, curr_size)
                curr_size = 2
                if arr[i] == arr[i+1]:
                    curr_size = 1


        return max(max_size, curr_size)
