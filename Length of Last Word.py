class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 単語の長さを測る
        length_counter = 0
        # 単語の長さを測り終えた後にTrueに切り替えて全体の処理を終了するためのFlag
        space_flag = False
        # 逆から走査する
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if space_flag:
                    break
            else:
                space_flag = True
                length_counter += 1

        return length_counter
