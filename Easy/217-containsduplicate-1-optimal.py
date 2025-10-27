#Question 217 (Leetcode): Contains Duplicate - Solution 1 (Optimal)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()

        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        return False


#Another solution -Use hash_map
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = 1
        return False
