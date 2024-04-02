class Solution:
    @staticmethod
    def subtractProductAndSum(n: int) -> int:
        product = 1
        summ = 0
        while n > 0:
            product = product * (n % 10)
            summ = summ + (n % 10)
            n = n // 10
        return product - summ


n = int(input())
print(Solution().subtractProductAndSum(n))
