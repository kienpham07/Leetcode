#Question 31 (Leetcode): Next Permutation -  Solution 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if (index < 0):
            nums.reverse()
            return

        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        nums[index + 1:] = reversed(nums[index + 1:]) #Another solution for reverse below
        return

#Another solution for reverse the order is the order is already sorted from smallest to largest:
while (left < right):
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1