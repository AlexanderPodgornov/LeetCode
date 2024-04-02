# cringe leetcode 4+2=7 very well !
class Solution:
    @staticmethod
    def theMaximumAchievableX(num: int, t: int) -> int:
        return num + (2 * t)


num = int(input())
t = int(input())
print(Solution().theMaximumAchievableX(num, t))
