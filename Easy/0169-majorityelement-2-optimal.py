# Question 169 (Leetcode): Container with Most Water - Solution 2 - Optimal
# Use the "Boyer-Moore Voting" algorithm to solve



# Time complexity: O(n)
# Space complexity: O(1)

# Another solution: Using hashmap technique
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        container = defaultdict(int)

        for num in nums:
            container[num] += 1

        requirement = len(nums) / 2
        max_res = 0
        res = 0
        for key, values in container.items():
            if values > max_res and values > requirement:
                max_res = values
                res = key

        return res

# Time complexity: O(n)
# Space complexity: O(n)