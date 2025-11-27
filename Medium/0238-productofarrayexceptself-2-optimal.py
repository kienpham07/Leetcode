# Question 238 (Leetcode): Product of array except self - Solution 2 - Optimal

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

# Time complexity: O(n)
# Space Complexity: O(1)
