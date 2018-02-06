class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros_location = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeros_location] = nums[zeros_location], nums[i]
                zeros_location += 1