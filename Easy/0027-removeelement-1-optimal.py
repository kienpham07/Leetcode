class Solution(object):
    def removeElement(self, nums, val):

        k = 0  # For each element that we found is different from val, we will put them
        # in the first slot k postion and move k + 1 for each time we found

        for i in range(len(nums)):
            if nums[i] != val:  # Found the number that is different from val
                nums[k] = nums[i]  # Then change the element in the k position to the element that is different from val
                k += 1

        return k
# We want to use k because if we found a nums[i] that is equal to val,
# then we would stop k at that position (the one that is equal to val),
# so that in the next i iteration in a loop, if we found a nums[i] that
# is different from val we would put it in the k position that we
# stop previously. So that every elements that is different from val
# will be in some of the first position in the list/