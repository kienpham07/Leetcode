# Question 169 (Leetcode): Container with Most Water - Solution 2 - Optimal
# Use the "Boyer-Moore Voting" algorithm to solve

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]

        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = num
                    count += 1
        return res

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