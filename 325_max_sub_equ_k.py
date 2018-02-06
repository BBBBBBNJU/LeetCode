class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict_temp = {0:-1}
        accumu = 0
        max_len = 0
        for indx in range(len(nums)):
            accumu += nums[indx]
            if accumu not in dict_temp:
                dict_temp[accumu] = indx
            if accumu - k in dict_temp:
                max_len = max(max_len, indx - dict_temp[accumu-k])
        return max_len
