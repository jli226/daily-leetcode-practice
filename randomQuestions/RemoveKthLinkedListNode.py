
def removeKthLinkedListNode(head, k):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(k):
        if not fast:
            return head
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
