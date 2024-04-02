class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        array = [0] * 26
        for i in s:
            array[ord(i)-ord('a')] += 1
        for i in t:
            array[ord(i)-ord('a')] -= 1
        for i in array:
            if i != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
print(Solution.isAnagram(s, t))
