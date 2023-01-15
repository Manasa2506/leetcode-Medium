# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry

            # example 15
            # carry = 1
            carry = val // 10
            # remainder = 5 which is the value we keep
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next
