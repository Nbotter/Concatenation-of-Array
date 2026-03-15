class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # heightsをソートして新しいリストを作る
        expected = sorted(heights)
        # ここで並ぶべき順番に並んでいない要素数をカウントする
        Sums_Of_different_number = 0
        #両リストを先頭から比較していく
        for i in range(0,len(heights)):
            if heights[i] != expected[i]:
                Sums_Of_different_number += 1
        return Sums_Of_different_number
