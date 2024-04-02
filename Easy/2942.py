from typing import List


class Solution:
    @staticmethod
    def findWordsContaining(words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans


words = ["leet", "code"]
x = "e"
print(Solution.findWordsContaining(words, x))
