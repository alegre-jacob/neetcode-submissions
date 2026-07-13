# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        while True:
            if f:
                f = f.next
                if f:
                    f = f.next
                else:
                    break
                s = s.next
            else:
                return False
            if f == s:
                return True
        return False
