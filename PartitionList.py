# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small, big = ListNode(0), ListNode(0)
        smallBegin, bigBegin, cur = small, big, head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        small.next, big.next = bigBegin.next, None
        return smallBegin.next