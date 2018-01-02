class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numDict = {}
        self.numList = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.numDict.has_key(val):
            return False
        else:
            self.numDict[val] = len(self.numList)
            self.numList.append(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.numDict.has_key(val):
            pos = self.numDict[val]
            temp_val = self.numList.pop(len(self.numList)-1)
            if pos < len(self.numList):
                self.numDict[temp_val] = pos
                self.numList[pos] = temp_val
            del self.numDict[val]
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        randIndex = random.randint(0,len(self.numList)-1)
        return self.numList[randIndex]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()