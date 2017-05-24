# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        privious, cur = res, head
        while cur:
            while cur.next and cur.val == cur.next.val: cur = cur.next
            if privious.next is not cur: cur = privious.next = cur.next
            else: privious, cur = cur, cur.next
        return res.next