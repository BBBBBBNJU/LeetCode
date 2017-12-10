class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s)] * len(s)
        for i in range(len(dp)-1, -1, -1):
            dp[i][i] == 1
            for j in range(i+1, len(dp[0]), 1):
                if s[i] == s[j]:
                    if i + 1<= j - 1:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
