# Question 128 (Leetcode): Longest Consecutive sequence - Solution 2 - Optimal

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                current = num
                while (current + 1 in num_set):
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length

# Time complexity: O(n)
# Space complexity: O(n)

# Technique for this problem: If num - 1 is not exist in the list, then that num is
# the start of the sequence.