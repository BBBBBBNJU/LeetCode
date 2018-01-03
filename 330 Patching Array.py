class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patchNum = 0
        maxP = 0
        i = 0
        while maxP < n:
            if i < len(nums):
                while maxP < nums[i] - 1 and maxP < n:
                    maxP = 2 * maxP + 1
                    patchNum += 1
                maxP += nums[i]
                i += 1
            else:
                maxP = 2 * maxP + 1
                patchNum += 1
        return patchNum
