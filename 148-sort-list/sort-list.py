# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next
        
        values.sort()
        head=ListNode(values[0])
        temp=head
        i=1
        while i<len(values):
            temp.next=ListNode(values[i])
            temp=temp.next
            i+=1
        
        
        return head