#Question 242 (Leetcode): Valid Anagram - Solution 2 (Optimal)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if freq[i] != 0:
                return False

        return True


#Solution 3: Using defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        count = defaultdict(int)

        for letter in s:
            count[letter] += 1

        for letter in t:
            count[letter] -= 1
            if count[letter] < 0:
                return False

        return True
