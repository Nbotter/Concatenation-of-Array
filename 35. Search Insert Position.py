class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    #配列numsの左端のindexをnums_left,右端のindexをnums_right
        nums_left = 0
        nums_right = len(nums) - 1

    #nums_leftとnums_rightの間が少なくとも1文字以上取る間
        while nums_left <= nums_right:
            nums_mid = (nums_left + nums_right) // 2
            if nums[nums_mid] == target:
                return nums_mid
    #半分より右側にあるのは確定なのでnums_leftを+1して次回から見るのは右側のみに絞る
            elif nums[nums_mid] < target:
                nums_left = nums_mid + 1
    #半分より左側にあるのは確定なのでnums_rightを-1して次回から見るのは左側のみに絞る
            else:
                nums_right = nums_mid - 1

        return nums_left
