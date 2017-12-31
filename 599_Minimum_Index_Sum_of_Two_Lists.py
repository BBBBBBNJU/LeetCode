class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        totalD_1 = {}
        for i in range(len(list1)):
            totalD_1[list1[i]] = i
        totalD_2 = {}
        for i in range(len(list2)):
            if totalD_1.has_key(list2[i]):
                totalD_2[list2[i]] = i + totalD_1[list2[i]]
        maxi = 100000000000000
        validList = []
        for key, value in totalD_2.iteritems():
            if value < maxi:
                validList = [key]
                maxi = value
            elif value == maxi:
                validList.append(key)
        return validList
