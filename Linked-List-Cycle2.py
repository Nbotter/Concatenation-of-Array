class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # サイクルがあるか判定（衝突点を見つける）
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                # 1つをheadに戻す
                slow = head

                # 同じ速度で進める
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next

                # 出会った場所がサイクル開始点
                return slow

        # サイクルなし
        return None
