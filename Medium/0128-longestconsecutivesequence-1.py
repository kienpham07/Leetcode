# Question 128 (Leetcode): Longest Consecutive sequence - Solution 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        num_set = list(set(nums))
        num_set.sort()

        max_length = 1
        length = 1
        for i in range(1, len(num_set)):
            if num_set[i - 1] == num_set[i] - 1:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1

        return max_length

# Time complexity: O(n log n)
# Space complexity: O(n)