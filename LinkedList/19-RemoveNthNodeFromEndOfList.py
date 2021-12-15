# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node strategy
        dummyNode = ListNode()
        dummyNode.next = head
        # Twist: 2 ptr strategy
        p1 = dummyNode
        p2 = dummyNode

        for i in range(n):
            # advance only p2 n times
            p2 = p2.next

        # at this point, p2 is n nodes away from p2

        while p2.next:
            # now, bots ptrs advance until p2.next is None
            p1 = p1.next
            p2 = p2.next

        # at this point p1 is guaranteed to be n+1 nodes away from the end
        # i.e, exactly where we want to be
        p1.next = p1.next.next
        # eliminate node

        # Time Complexity: O(n)
        # Space Complexity O(1)

        return dummyNode.next
