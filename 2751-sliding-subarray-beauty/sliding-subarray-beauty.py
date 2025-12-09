from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = {i:0 for i in range(-50,51)}
        ans = []
        n = len(nums)

        neg_count = 0

        for i, val in enumerate(nums):
            freq[val] += 1
            if val < 0:
                neg_count += 1

            if i >= k:
                out = nums[i - k]
                freq[out] -= 1
                if out < 0:
                    neg_count -= 1

            if i + 1 >= k:
                if neg_count < x:
                    ans.append(0)
                else:
                    # find x-th smallest negative
                    need = x
                    beauty = 0
                    for v in range(-50, 0):  # only negatives
                        if not freq[v]: continue
                        if freq[v] >= need:
                            beauty = v
                            break
                        else:
                            need -= freq[v]
                    ans.append(beauty)

        return ans
