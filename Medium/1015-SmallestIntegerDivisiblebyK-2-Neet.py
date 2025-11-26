# Question 1015 (Leetcode): Smallest Integer Divisible by K - Solution 2 - Optimal (Solve by Neetcode)

def smallestRepunitDivByK(self, k: int) -> int:
    curr = 1
    length = 1

    prev = set()

    while curr % k != 0:
        if curr in prev:  # Cycle detection for the case if there is no such n
            return -1
        prev.add(curr)
        curr = (curr % k) * 10 + 1 # Curr % k is the remainder
        length += 1

    return length

# This solution works because the reminder is in a cycle dectection and there is no n that divisible by k,
# and we can detect the repeated number in that cycle by storing the value and then return -1