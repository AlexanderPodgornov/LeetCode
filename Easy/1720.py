from typing import List


class Solution:
    @staticmethod
    def decode(encoded: List[int], first: int) -> List[int]:
        ans = [first ^ encoded[0]]
        for i in range(1, len(encoded)):
            ans.append(encoded[i] ^ ans[i - 1])
        ans.insert(0, first)
        print(ans)
        return ans


encoded = [6,2,7,3]
first = 4
print(Solution.decode(encoded, first))
