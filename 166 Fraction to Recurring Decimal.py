class Solution(object):
    def getOneStep(self, num, den):
        singDigit = int(math.floor(num / den))
        remain = num % den
        return singDigit, remain

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        give = 0
        pastRemains = []
        otherDigits = []
        nega = False
        if numerator * denominator == 0:
            return '0'
        if numerator * denominator < 0:
            nega = True
        if numerator < 0:
            numerator *= -1
        if denominator < 0:
            denominator *= -1

        firstDigit = str(numerator/denominator)
        remain = numerator % denominator
        remain *= 10
        pastRemains.append(remain)
        repeatFlag=False

        while remain != 0:
            singDigit, remain = self.getOneStep(remain, denominator)
            otherDigits.append(str(singDigit))
            remain *= 10
            if remain in pastRemains:
                repeatFlag=True
                break
            pastRemains.append(remain)

        if repeatFlag:
            locIdx = pastRemains.index(remain)

        if len(otherDigits) == 0:
            finalResult = firstDigit
        else:
            if not repeatFlag:
                finalResult = firstDigit + '.' + ''.join(otherDigits)
            else:
                finalResult = firstDigit + '.' + ''.join(otherDigits[0:locIdx]) + '(' + ''.join(otherDigits[locIdx:None]) + ')'
        if nega:
            return '-'+finalResult
        else:
            return finalResult




