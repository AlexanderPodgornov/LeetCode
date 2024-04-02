class Solution:
    @staticmethod
    def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
        k = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                k = k + 1
        return k
