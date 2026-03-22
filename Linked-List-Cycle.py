class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head

        # ここで今のノードと次のノードが存在することを保証
        while fast_pointer is not None and fast_pointer.next is not None:
            # slowなポインタは1つだけ進む
            slow_pointer = slow_pointer.next
            # fastなポインタは2つ進む
            fast_pointer = fast_pointer.next.next
            # 追いついたらループあり
            if slow_pointer is fast_pointer:
                return True

        return False
