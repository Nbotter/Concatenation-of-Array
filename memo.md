# 思考ログ
58. Length of Last Word

## Step 1
前から走査してsに文字があるときのみカウントする  
しかし、これが最後の単語であることを判別するには？

AIにヒントを聞いてみた
## Step2
最後尾から線形探索すれば、これが最後の単語なのかという問題もクリアされるのでそれで疑似コード書いてみた
```
length_counter = 0
for i in range(0, len(s),-1)
    if nums [i] == "":
        length_counter += 0
    else:
        length_counter += 1
    elif
```
しかし、単語の操作を終えた際にどうすればいいか分からない
またAIに聞いてみた
## Step3
フラグを持てとのこと  
それでbreak処理をしてカウントを終わらせればいいらしい  
あと、rangeの書き方、空白は" "(スペースを空ける) で一文字であるらしい  
```
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
```
ただ素朴な疑問なのだが、これで最後尾あたりに空白きたらいきなりif処理のほうに入って正しくカウントできないのでは？  
とも思ったが初期値はspace_flag = False なので問題なさそう  
