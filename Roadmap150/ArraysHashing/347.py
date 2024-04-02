from typing import List


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        dict = {}
        arr = []
        for num in nums:
            if dict.get(num) is None:
                dict[num] = 1
            else:
                dict[num] += 1
        for key, value in dict.items():
            if value >= k:
                arr.append(key)
        return arr


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution.topKFrequent(nums, k))
