## Step1  
リストexpectedと比較したときに違うものを抜き出して、その個数を出せばよい  
ということで二つのリストを順番に一つずつ比較していけばよいので単にfor文でループを1個回せばよいという発想になる
そこで以下のコードを書きくだした
```
different number = 0
for i in range(0, len(heights)-1)
    if height checker[i] != expected[i]:
        different number += 1
        i += 1
    else:
        i += 1
return different number
```
## Step2
ここで文法ミス、expectedが作られていないとのことなのでそれらを修正して
```
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
```
