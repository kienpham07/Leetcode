# Question 14 (Leetcode): LongestCommonPrefix - Solution 1 (Optimal)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range (len(strs[0])):
            for word in strs:
                if len(word) == i or word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res