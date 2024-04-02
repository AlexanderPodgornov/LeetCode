class Solution:
    @staticmethod
    def containsDuplicate(nums: [int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) is None:
                dict[nums[i]] = 1
            else:
                return True
        return False


nums = [1, 2, 3, 4]
print(Solution.containsDuplicate(nums))
