from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if dict.get(difference) is not None:
                return [dict.get(difference), i]
            dict[nums[i]] = i
        return []


nums = [3, 2, 4]
target = 6
print(Solution.twoSum(nums, target))
