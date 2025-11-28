# Question 3754 (Leetcode): Concatenate Non-Zero Digits and Multiply by Sum I - Solution 2 - Optimal

# A more simplified version:

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        total = 0
        res = 0

        for ch in str(n):
            digit = int(ch)
            if digit != 0:
                res = res * 10 + digit
                total += digit

        return res * total

# Time complexity: O(n)
# Space complexity: O(1)