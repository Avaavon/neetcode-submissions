# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        take the beginning of two sorted arrays
        take the lesser of the 2 heads to add to a new linked list
        adding remaining if u reach the end of one
        while loop breaks when either array ends
        """
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next
        node.next = list1 or list2
        return dummy.next

        