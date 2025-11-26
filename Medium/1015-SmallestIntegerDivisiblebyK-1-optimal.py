# Question 1015 (Leetcode): Smallest Integer Divisible by K - Solution 1 - Optimal

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        if (k % 2 == 0 or k % 5 == 0): # Number that ends with 1 cannot be divisible by 2 or 5
            return -1

        val = 1
        length = 1

        while(True):
            if val % k == 0:
                return length

            val = (val * 10 + 1) % k # To avoid overflow
            length += 1

            if val == 0:
                return length

# n = k . q + r (Reminder formula)
# We have n = 10 * n + 1 -> n = 10 * (k . q + r) + 1
# We want n % k == 0 -> Since 10 * kq is already % k = 0
# Therefore, 10 * r + 1 have to be divisible by k
# Therefore, it only depends on r (r is curr % k)