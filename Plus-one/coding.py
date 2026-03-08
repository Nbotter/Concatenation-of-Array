class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #iは配列のindex
        i = len(digits) - 1
        # (すべて・一部の桁に)9が含まれる場合
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        # 9が含まれない場合
        if i >= 0:
            digits[i] += 1
            return digits
        # すべての桁が9の場合にのみここに来る
        return [1] + digits
