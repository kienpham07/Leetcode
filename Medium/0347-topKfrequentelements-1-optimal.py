# Question 347 (Leetcode): Top K frequent Elements - Solution 1 (Optimal)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        for key, value in hash_map.items():
            count[value].append(key)

        res = []

        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if (len(res) == k):
                    return res