# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev
        prev = None
        # cur
        cur = head

        while cur: 
            # get next before reverse
            temp = cur.next
            # update next to prev
            cur.next = prev
            # update prev to cur
            prev = cur
            # and cur to temp
            cur = temp

        # prev sits at last node (or new head)
        return prev

# time: O(n)
# space: O(1)
