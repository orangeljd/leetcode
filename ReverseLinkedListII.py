# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        begin = ListNode(0)
        begin.next = head
        cur, res, previous, next = head, begin, begin, head
        count = 0
        while cur:
            count += 1
            next = cur.next
            if count == m:
                begin = previous
            elif m < count < n:
                cur.next = previous
            elif count == n:
                cur.next = previous
                begin.next.next = next
                begin.next = cur
                break
            previous, cur = cur, next
        return res.next