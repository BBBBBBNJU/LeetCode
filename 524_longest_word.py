class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        all_satis = []
        for each_s in d:
            total_lenth = len(each_s)
            j = 0
            for each_alpha in s:
                if each_alpha == each_s[j]:
                    j += 1
                if total_lenth == j:
                    all_satis.append(each_s)
                    break
        max_length = -1
        sentence = ""
        pos = -1
        for j in range(len(all_satis)):
            if len(all_satis[j]) > max_length:
                max_length = len(all_satis[j])
                sentence = all_satis[j]
                pos = j
            elif len(all_satis[j]) == max_length:
                if all_satis[j] < sentence:
                    sentence = all_satis[j]
                    pos = j
                
        if pos >= 0:
            return all_satis[pos]
        else:
            return ""
