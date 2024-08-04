from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Sol:
    def reverse_ll(self, head: [ListNode]) -> [ListNode]:
        cur = head
        prev = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


if __name__== "__main__":
    s=Sol()
    head=[1,2,3,4,5]
    
    res=s.reverse_ll(head)

#Result:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]