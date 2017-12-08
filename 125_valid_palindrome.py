class Solution(object):       
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) ==  0 or len(s) == 1:
            return True
        i = 0
        j = len(s) - 1
        while (i <= j):
            while not (s[i].isalpha() or s[i].isdigit()) and i < len(s)-1:
                i += 1
            while not (s[j].isalpha() or s[j].isdigit()) and j > 0:
                j -= 1
            if i > j:
                return True
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
