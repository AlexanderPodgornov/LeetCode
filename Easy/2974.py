from typing import List


class Solution:
    @staticmethod
    def numberGame(nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums)-1,2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums


nums = [5,4,2,3]
print(Solution.numberGame(nums))