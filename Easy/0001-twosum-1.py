#Question 1 (Leetcode): Two Sum -  Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                  result += [i, j]
                  return result
                    #Return [i, j] also works