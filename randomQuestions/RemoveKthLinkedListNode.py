
def removeKthLinkedListNode(head, k):
    dummy = SinglyLinkedListNode(0)
    # created a dummy node point to head and two pointers
    dummy.next = head
    slow = dummy
    fast = dummy

    # Advances first pointer so that the gap between first and second is k nodes apart
    # 这个部分我不是很懂这个写法？ 我的理解目的是要让fast先跑出去和slow保持距离(it aims to move fast k times)
    for i in range(k):
        if not fast:  # not fast means the fast is a valid node, not None
            return head
        fast = fast.next

    # Move slow to the end, maintaining the gap
    while fast.next:
        slow = slow.next
        fast = fast.next

    # linked the nodes that are before and after the deleted node together /or bypass the deleted node
    slow.next = slow.next.next

    return dummy.next


# 说一个解法是one pass和two pass 是怎么分
# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.
 # we could use two pointers. The first pointer advances the list by k-1 steps from the beginning, while the second pointer starts from the beginning of the list.
 # (Since we assign fast to dummy which is a node ahead head, and we move it k times.)
 # Now, both pointers are exactly separated by k nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node.
 # We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.

# 2.when you were doing the question, what caused an issue, how did you fix it

# 3.time/space complexity of your solution?
 # Time complexity : O(n).The algorithm makes one traversal of the list of nodes.
 # Space complexity : O(1) We only used constant extra space, to store like slow, fast

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
