class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_number = {}
        for task in tasks:
            if task in tasks_number:
                tasks_number[task] += 1
            else:
                tasks_number[task] = 1
        maxmum = -1
        for task, number in tasks_number.iteritems():
            if number > maxmum:
                maxmum = number

        maxmum_num = 0
        for task, number in tasks_number.iteritems():
            if number == maxmum:
                maxmum_num += 1

        return max(len(tasks), (n+1) * (maxmum - 1) + maxmum_num)

solu = Solution()
print(solu.leastInterval(["A","A","A","B","B","B"], 0 ))