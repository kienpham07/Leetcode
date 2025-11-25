# Question 1018 (Leetcode): Binary Prefix Divisible by 5 - Solution 1 - Optimal
# Use math technique

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        val = 0
        for bit in nums:
            val = (val * 2 + bit) % 5
            ans.append(val == 0)
        return ans
