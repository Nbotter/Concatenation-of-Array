class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        node = head
        while node is not None:
            result = result * 2 + node.val
            node = node.next

        return result
