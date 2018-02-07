# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        q = PriorityQueue()
        for eachlistNodev in lists:
            node = eachlistNodev
            if node:
                q.put((node.val, node))
        dumy = ListNode(0)
        node = dumy
        while not q.empty():
            node.next = q.get()[1]
            node = node.next
            if node.next != None:
                q.put((node.next.val, node.next))
        return dumy.next