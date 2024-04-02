from typing import List


class Solution:
    @staticmethod
    def numIdenticalPairs(nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    k = k + 1
        return k


nums = [1, 2, 3, 1, 1, 3]
print(Solution().numIdenticalPairs(nums))
