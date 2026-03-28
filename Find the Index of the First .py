class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle  = len(needle)

        # needle が空文字の場合(implicit falseを使用)
        if  not len_needle == 0:
            return 0

        # 比較開始位置を順番に試す
        for i in range(len_needle - len_haystack + 1):
            if haystack[i:i + len_haystack] == needle:
                return i

        return -1
