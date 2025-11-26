# Question 1929 (Leetcode): Concatenation of array - Solution 1 - Optimal

# Solution 1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Solution 2 (smart)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))

        index = 0
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans