# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # at least two nodes in list
        # Two pointer strategy

        first = head
        second = head.next
        # answer will always be the second node
        answer_head = second

        while first.next and first.next.next:

            first.next = second.next
            second.next = first

            # need to reference the second node

            first = first.next
            second = second.next  # we are in first node

            if second.next.next:
                # there is a node 2 places ahead
                second.next = second.next.next
                second = first.next
            else:
                second.next = first

        # special case: the two final nodes
        # at the end of the loop we are left with first and second
        # pointing at the final 2 nodes
        if second:
            first.next = None
            second.next = first

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        return answer_head
