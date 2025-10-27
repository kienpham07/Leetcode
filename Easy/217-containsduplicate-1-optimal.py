# Question 36 (217): Contains Duplicate - Solution 1 (Optimal)
# Use hash set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()

        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        return False