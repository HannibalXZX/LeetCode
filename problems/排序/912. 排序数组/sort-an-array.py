# -*- coding:utf-8 -*-
#@Time  :    2020/8/13 3:12 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    sort-an-array.py
#@Description：https://leetcode-cn.com/problems/sort-an-array/
from typing import List

import random
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        print(List.sort(nums))
        print(nums) # 改变原有的数组形式
        # return List.sort(nums) error
        return sorted(nums)

    ## 冒泡排序
    def sortArray_bubleSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums

        length = len(nums)
        for i in range(length):
            flag = True
            for j in range(i, length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    flag = False
            if flag:
                break
        return nums

    ## 插入排序
    def sortArray_insertionSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums
        length = len(nums)

        for i in range(0, length):
            j = i
            while j and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1

        return nums

    ## 选择排序
    def sortArray_SelectionSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums
        length = len(nums)

        for i in range(length):
            minIndex = i
            for j in range(i, length):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]

        return nums

    ## 归并排序
    def sortArray_MergeSort(self, nums: List[int]) -> List[int]:
        self._merge_sort_between(nums, 0, len(nums) - 1)
        return nums

    #
    def _merge(self, a:List[int], low:int, mid:int, high:int):
        i, j = low, mid+1
        tmp = []
        while i <= mid and j <= high:
            if a[i] <= a[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(a[j])
                j += 1
        start = i if i <= mid else j
        end = mid if i <= mid else high
        tmp.extend(a[start:end+1])
        a[low:high+1] = tmp

    def _merge_sort_between(self, a:List, low:int, high: int):
        if low < high:
            mid = low + (high -low) // 2
            print("%d %d %d" % (low, mid, high))
            self._merge_sort_between(a, low, mid)
            self._merge_sort_between(a, mid+1, high)
            self._merge(a, low, mid, high)

    ## 快速排序
    def sortArray_QuickSort(self,nums: List[int]) -> List[int]:
        n = len(nums)
        def _quick_sort(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] < nums[pivot]:
                    i += 1

                nums[i], nums[j] = nums[j], nums[i]

            nums[pivot], nums[j] = nums[pivot], nums[j]
            # 此时的j就是pivot，也就是基准位
            _quick_sort(left, j - 1)
            _quick_sort(j + 1, right)
            return nums

        return _quick_sort(0, n - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 3, 1]
    print(s.sortArray(nums))
    print(s.sortArray_bubleSort(nums))
    print(s.sortArray_insertionSort(nums))
    print(s.sortArray_SelectionSort(nums))
    print(s.sortArray_MergeSort(nums))
    print(s.sortArray_QuickSort(nums))