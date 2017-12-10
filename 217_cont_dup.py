class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicti = {}
        for eachone in nums:
            if dicti.has_key(eachone):
                return True
            else:
                dicti[eachone]  = 1
        return False
