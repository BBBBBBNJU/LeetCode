class Solution(object):
    def _search(self, start, target):
        low = start 
        high = len(self.numbers)-1
        while low <= high:
            mid = (low + high) / 2
            if self.numbers[mid] == target:
                return mid
            elif self.numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.numbers = numbers 
        for i in range(len(self.numbers)):
            j = self._search(i+1, target - self.numbers[i])
            if j != -1:
                return [i+1,j+1]
