# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
class Solution(object):
        def swapPairs(self, head):
            if not head or not head.next:
                return head
            dummy = ListNode(0)
            dummy.next = head
            cur = dummy

            while cur.next and cur.next.next:
                first = cur.next
                sec = cur.next.next
                cur.next = sec
                first.next = sec.next
                sec.next = first
                cur = cur.next.next
            return dummy.next
