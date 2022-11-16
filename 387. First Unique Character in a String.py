"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1."""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for char in s:
            if counter[char] == 1:
                return s.index(char)
        return -1
