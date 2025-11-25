# Question 1015 (Leetcode): Smallest Integer Divisible by K - Solution 1 - Optimal

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        curr = 1
        length = 1

        prev = set()

        while curr % k != 0:
            if curr in prev:  # Cycle detection for the case if there is no such n
                return -1
            prev.add(curr)
            curr = (curr % k) * 10 + 1
            length += 1

        return length

# n = k . q + r (Reminder formula)
# We have n = 10 * n + 1 -> n = 10 * (k . q + r) + 1
# We want n % k == 0 -> Since 10 * kq is already % k = 0
# Therefore, 10 * r + 1 have to be divisible by k
# Therefore, it only depends on r (r is curr % k)