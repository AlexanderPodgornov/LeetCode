from typing import List


class Solution:
    @staticmethod
    def finalValueAfterOperations(operations: List[str]) -> int:
        x = 0
        for string in operations:
            if string == "--X" or string == "X--":
                x = x - 1
            if string == "++X" or string == "X++":
                x = x + 1
        return x

