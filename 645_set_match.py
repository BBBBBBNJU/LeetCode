class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxmum = len(nums)
        dictna = {}
        dup = -1
        for eachone in nums:
            if dictna.has_key(eachone):
                dup = eachone
            else:
                dictna[eachone] = 1
        missing = (1+maxmum) * maxmum / 2 + dup - sum(nums)
        return [dup, missing]
