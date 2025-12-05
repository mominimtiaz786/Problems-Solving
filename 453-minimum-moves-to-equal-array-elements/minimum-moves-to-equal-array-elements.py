class Solution:
    def minMoves(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:  return 0
        # moves = 0
        # nums.sort()
        # max_n = max(nums)
        min_n = min(nums)
        # max_i = nums.index(max(nums))

        # while min_n != max_n:
        #     diff = max_n - min_n
        #     tmp_i = max_i
        #     for i in range(N):
        #         if i != max_i:  
        #             nums[i]+=1
        #         if nums[i] > max_n:
        #             tmp_i, max_n = i, nums[i]

        #     max_i = tmp_i
        #     min_n+=1
        #     moves+=1
        
        # return moves

        # # nums.sort()
        # for i in range(N):
        #     moves+=(nums[i]-min_n)

        moves = sum(nums) - min_n*N
        return moves