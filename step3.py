class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        sum_binary_digit = 0
        node = head
        while node is not None:
            sum_binary_digit = (sum_binary_digit << 1) | node.val
            node = node.next

        return sum_binary_digit
