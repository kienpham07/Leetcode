# Question 3754 (Leetcode): Concatenate Non-Zero Digits and Multiply by Sum I - Solution 1 - Optimal

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        temp = n
        res = 0
        total = 0

        while (temp > 0):
            last_digit = temp % 10
            if (last_digit != 0):
                res = res * 10 + last_digit
            total += last_digit
            temp = temp // 10

        final_res = 0
        while (res > 0):
            last_digit2 = res % 10
            final_res = final_res * 10 + last_digit2
            res = res // 10

        return final_res * total

# Time complexity: O(n)
# Space complexity: O(1)

#Technique: We are reversing twice (once implicitly by constructing backward, then flipping back).