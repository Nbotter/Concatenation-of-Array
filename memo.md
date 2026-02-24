# 思考ログ
35. Search Insert Position

## Step 1
線形探索すれば良さそう

以下が疑似コード(のような何か)

```
pointer
index =0
for i in range(len(Array))
    if Array [index] == target:
        return i
    else
```
ここまで書いてAIにヒントを聞いてみた
するとそもそも計算量がO(n)になるからダメだという
また、ソートされているなら全部見る必要もないだろう　とのこと

そこで私は、
「二分探索したいんから真ん中の値取りたいけど、偶数と奇数でArrayの取るべきindex変わっちゃうのでは？」
と聞いた

がしかし、そもそも中央をとるのではなく探索範囲を半分にすることが本質とのこと
従って、問題ない
奇数の場合はどちらかに寄らせればよいので

## Step2
```
if Array[mid] < target:
    ???
else:
    ???
```
という形まで特定した
ここで
```
if Array[mid] < target:
```
では左側、elseでは右側を捨てればよいことに気付く(昇順なので)

##Step3
ここで観念してAIに解答を聞いてみた
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

##Step4
命名やコメントを工夫してみる

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    #配列numsの左端のindexをnums_left,右端のindexをnums_right
        nums_left = 0
        nums_right = len(nums) - 1

    #nums_leftとnums_rightの間が少なくとも1文字以上取る間
        while nums_left <= nums_right:
            nums_mid = (nums_left + nums_right) // 2
    #
            if nums[nums_mid] == target:
                return nums_mid
    #半分より右側にあるのは確定なのでnums_leftを+1して次回から見るのは右側のみに絞る
            elif nums[nums_mid] < target:
                nums_left = nums_mid + 1
    #半分より左側にあるのは確定なのでnums_rightを-1して次回から見るのは左側のみに絞る
            else:
                nums_right = nums_mid - 1

        return nums_left
