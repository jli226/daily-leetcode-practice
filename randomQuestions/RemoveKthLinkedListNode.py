
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

# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.

# 2.when you were doing the question, what caused an issue, how did you fix it

# 3.time/space complexity of your solution?

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
