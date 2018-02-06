# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        ends = []
        starts = []
        for eachinteval in intervals:
            starts.append(eachinteval.start)
            ends.append(eachinteval.end)
        ends.sort()
        starts.sort()

        i = 0
        j = 0
        avaliable = 0
        room_num = 0
        while j < len(starts):
            if starts[j] < ends[i]:
                if avaliable == 0:
                    room_num += 1
                else:
                    avaliable -= 1
                j += 1
            else:
                while ends[i] <= starts[j]:
                    avaliable += 1
                    i += 1
        return room_num



