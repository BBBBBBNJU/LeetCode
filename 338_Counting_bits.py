class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        from math import *
        thisList = [0] * (num + 1)
        if num >= 1 :
            thisList[1] = 1
        if num >= 2:
            thisList[2] = 1
        for i in range(num + 1):
            if i not in [0,1,2]:
                base = int(2 ** floor(log(i) / log(2)))
                res = i - base
                if base != i:
                    thisList[i] = thisList[base] + thisList[res]
                else:
                    thisList[i] = 1
        return thisList

