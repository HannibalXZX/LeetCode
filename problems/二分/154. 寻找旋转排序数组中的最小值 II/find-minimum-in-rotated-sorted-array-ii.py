# -*- coding:utf-8 -*-
#@Time  :    2020/7/25 9:12 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    find-minimum-in-rotated-sorted-array-ii.py
#@Description： https://leetcode-cn.com/problems/ff/

from typing import List
class Solution:
    ## 这里用low有问题，逻辑要更复杂，因为
    def minArray_error(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = (low + high) // 2
            if nums[mid] > nums[low]:
                low = mid
            # 这里的逻辑其实是错误的，针对1，2，3，4，5
            elif nums[mid] < nums[low]:
                high = mid
            else:
                if nums[low] == nums[high]:
                    high -= 1
                elif nums[low] > nums[high]:
                    low = mid + 1
                else:
                    break
        return nums[low]

    def minArray(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low=mid+1
            elif nums[mid] < nums[high]:
                high=mid
            else:
                # 这里很巧妙
                high -= 1
        return nums[low]

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while (left < right):
            mid = left + (right - left) // 2
            if rotateArray[right] > rotateArray[mid]:
                right = mid
            elif rotateArray[right] == rotateArray[mid]:
                right = right - 1
            else:
                left = mid + 1
        return rotateArray[left]

    # 这里使用的是low
    def minNumberInRotateArray_2(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        mid = low
        while(rotateArray[low]>= rotateArray[high]):
            mid = low + (high - low)//2
            if high - low == 1:
                mid = high
                break
            if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
                return min(rotateArray[low:high+1])
            elif rotateArray[mid] >= rotateArray[low]:
                low = mid
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid
        return rotateArray[mid]


if __name__ == '__main__':
    s = Solution()
    numbers = [3, 4, 5, 1, 2]
    numbers = [2,2,2,0,1]
    # numbers = [10,1,10,10,10]
    # numbers = [4,5,6,7,0,1,2]
    print(s.minArray_error(numbers))
