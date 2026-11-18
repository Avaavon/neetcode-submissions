# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # create a slow and fast pointer
        # once fast reaches end, slow is half point
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now we are at half point

        # we have first half
        # now we create second half in reverse order
        prev = None
        head2 = cur = slow.next
        slow.next = None # sever end

        # stop at last val
        # reverse as we go
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head2 = prev

        new_head = head
        while head2:
            temp = head.next
            head.next = head2
            temp2 = head2.next
            head2.next = temp
            head2 = temp2
            head = temp
        