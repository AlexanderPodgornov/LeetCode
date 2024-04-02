from typing import List


class Solution:
    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(Solution.shuffle(nums, n))
