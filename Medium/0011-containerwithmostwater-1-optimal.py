# #Question 11 (Leetcode): Container with Most Water - Solution 1 - Optimal
# Use two pointer technique

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_res = 0
        area = 0
        while (i < j):
            if height[i] <= height[j]:
                area = height[i] * (j - i)
                if area > max_res:
                    max_res = area
                i += 1
            else:
                area = height[j] * (j - i)
                if area > max_res:
                    max_res = area
                j -= 1

        return max_res
