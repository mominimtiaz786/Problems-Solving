class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N < 2:   return N

        max_size = 1

        curr_size1, curr_size2 = 1, 1

        for i in range(N-1):

            if i % 2 == 0 and arr[i] < arr[i+1]:
                curr_size1+=1
            elif i % 2 == 1 and arr[i] > arr[i+1]:
                curr_size1+=1
            else:
                max_size = max(max_size, curr_size1)
                curr_size1 = 1

            j = i+1          
            if j % 2 == 1 and arr[j] < arr[j-1]:
                curr_size2+=1
            elif j % 2 == 0 and arr[j] > arr[j-1]:
                curr_size2+=1
            else:
                max_size = max(max_size, curr_size2)
                curr_size2 = 1  



        return max(max_size, curr_size1, curr_size2)
