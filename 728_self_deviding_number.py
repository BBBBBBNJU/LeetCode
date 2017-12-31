class Solution(object):
    def getdigit(self, num):
        falseFlag = False
        alldigit = list(set(str(num)))
        for i in range(len(alldigit)):
            alldigit[i] = int(alldigit[i])
            if alldigit[i] == 0:
                falseFlag = True
        return alldigit, falseFlag

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        allList = []
        for i in range(left, right+1):
            ValidFlag = True
            alldigit, falseFlag = self.getdigit(i)
            if not falseFlag:
                for eachdigit in alldigit:
                    if i % eachdigit != 0:
                        ValidFlag = False
                if ValidFlag:
                    allList.append(i)
        return allList
