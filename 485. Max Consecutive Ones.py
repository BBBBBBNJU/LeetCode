class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        temp = 0
        start_record = False
        for eachone in nums:
            if eachone == 1:
                start_record = True
            else:
                start_record = False
                temp = 0
            if start_record:
                temp += 1
            if temp >= max:
                max = temp
        return max
