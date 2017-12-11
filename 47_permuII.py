class Solution(object):
    def _perm(self, all_num):
        if len(all_num) == 0:
            self.allresult.append(copy.deepcopy(self.stack))
        for eachone in all_num:
            self.stack.append(eachone)
            self.dict_num[eachone] -= 1
            new_all_num = copy.deepcopy(all_num)
            if self.dict_num[eachone] == 0:
                new_all_num.remove(eachone)
            self._perm(new_all_num)
            self.dict_num[eachone] += 1
            self.stack.pop()
            
                
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_num = list(set(nums))
        self.dict_num = {}
        self.allresult = []
        self.stack = []
        
        for each in nums:
            if self.dict_num.has_key(each):
                self.dict_num[each] += 1
            else:
                self.dict_num[each] = 1
                
        self._perm(all_num)
        return self.allresult
        
