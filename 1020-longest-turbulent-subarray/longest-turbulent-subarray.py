class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N < 2:   return N

        max_size = 1

        curr_size = 1
        for i in range(N-1):
            if i % 2 == 0 and arr[i] < arr[i+1]:
                curr_size+=1
            elif i % 2 == 1 and arr[i] > arr[i+1]:
                curr_size+=1
            else:
                max_size = max(max_size, curr_size)
                curr_size = 1

        max_size = max(max_size, curr_size)

        curr_size = 1
        for i in range(1, N):
            if i % 2 == 1 and arr[i] < arr[i-1]:
                curr_size+=1
            elif i % 2 == 0 and arr[i] > arr[i-1]:
                curr_size+=1
            else:
                max_size = max(max_size, curr_size)
                curr_size = 1
        
        max_size = max(max_size, curr_size)

        return max_size


        