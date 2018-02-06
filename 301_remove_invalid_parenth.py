class Solution(object):
    def isvalid(self, s):
        if s[0] == '(':
            stack_list = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack_list.append('(')
                elif s[i] == ')':
                    if len(stack_list) == 0:
                        return False
                    else:
                        stack_list.pop()
            if len(stack_list) == 0:
                return True
        return False

    def _generate_next_leve(self, s):
        temp_list = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                temp_list.append(s[0:i] + s[i+1:None])
        return temp_list

    def _remove_test(self, remainLists):
        next_level_remainList = []
        sucessList = []
        for eachone in remainLists:
            if self.isvalid(eachone):
                sucessList.append(eachone)
            else:
                next_level_remainList += self._generate_next_leve(eachone)
        if len(sucessList) != 0:
            return sucessList, True
        else:
            return next_level_remainList, False

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        remainList = [s]
        flag = False
        while not flag:
            remainList, flag = self._remove_test(remainList)
        if len(remainList) == 0:
            remainList = [""]
        return remainList
