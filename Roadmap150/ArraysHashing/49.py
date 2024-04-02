from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)):
            arr = [0] * 26
            for j in range(len(strs[i])):
                arr[ord(strs[i][j]) - ord('a')] += 1
            a = tuple(arr)
            if dict.get(a) is None:
                dict[a] = [strs[i]]
            else:
                dict[a].append(strs[i])
        return list(dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution.groupAnagrams(strs))
