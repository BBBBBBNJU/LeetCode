class Solution(object):
    def _mul(self, num1, num2, digit):
        return int(num1) * int(num2) * 10 ** digit

    def _multiply(self, num1, num2, digit):
        temp = 0
        for i in range(len(num1)):
            temp += self._mul(num1[-(i+1)], num2, i)
        return temp * 10 ** digit

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = 0
        for i in range(len(num2)):
            temp += self._multiply(num1, num2[-(i+1)], i)
        return str(temp)