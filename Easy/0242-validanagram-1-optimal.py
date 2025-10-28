#Question 242 (Leetcode): Valid Anagram - Solution 1 (Optimal)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS, counterT = {}, {} #Use hash map

        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        for c in s:
            if counterS[c] != counterT.get(c, 0):
                return False

        return True

#Solution 2
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)

#Solution 3
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)
