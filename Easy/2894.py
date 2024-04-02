class Solution:
    @staticmethod
    def differenceOfSums(n: int, m: int) -> int:
        k = 0
        for i in range(1, n + 1):
            k = k - i
            k = k + i * 2 * (i % m != 0)
        return k


n = int(input())
m = int(input())
print(Solution().differenceOfSums(n, m))
