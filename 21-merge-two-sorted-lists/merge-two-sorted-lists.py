class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to start the merged list
        curr = dummy  # Pointer to build the new list
        while l1 and l2:  # Iterate until one list is exhausted
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next  # Move to the next node
        
        # Attach the remaining nodes of the non-empty list
        curr.next = l1 if l1 else l2  
        return dummy.next  # Return the merged list (excluding dummy node)