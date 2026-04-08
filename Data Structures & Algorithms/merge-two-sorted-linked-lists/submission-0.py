# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode(0)
        curr = newlist
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            elif list2.val > list1.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = ListNode(list1.val)
                curr = curr.next
                curr.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return newlist.next
                



