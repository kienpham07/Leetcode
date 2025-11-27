# Question 238 (Leetcode): Product of array except self - Solution 1

# TLE - Time Limit Exceed Error
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            start_index = 0
            end_index = len(nums) - 1
            left_res = 1
            right_res = 1

            while (start_index < i):
                left_res *= nums[start_index]
                start_index += 1

            while (end_index > start_index):
                right_res *= nums[end_index]
                end_index -= 1

            res.append(left_res * right_res)

        return res

# Time complexity: O(n ^ 2)
# Space complexity: O(1)