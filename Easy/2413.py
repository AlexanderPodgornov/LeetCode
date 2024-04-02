class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (1 + n % 2) * n