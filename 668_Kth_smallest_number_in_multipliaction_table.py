class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def satisfy(x):
            temp_sum = 0
            for i in range(1, m+1):
                temp_sum += min(x / i, n)
            return temp_sum >= k
            
        low, high = 1, m*n
        while(low < high):
            mid = (low + high) / 2
            if satisfy(mid):
                high = mid
            else:
                low = mid + 1
        return low
            
