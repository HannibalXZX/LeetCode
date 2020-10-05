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
    # 采用这个算法了
    # https://www.jianshu.com/p/2b2f1f79984e
    def quick_Sort_11(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 分区
        def Partition(L, left, right):
            pivotkey =L[left]
            while left < right:
                while left < right and L[right] >= pivotkey:
                    right -= 1
                L[left] = L[right]
                while left < right and L[left] <= pivotkey:
                    left += 1
                L[right] = L[left]
            L[left] = pivotkey
            return left

        # 快排
        def q_sort(nums, left, right):
            if left < right:
                pIndex = Partition(nums, left, right)
                q_sort(nums, left, pIndex-1)
                q_sort(nums, pIndex+1, right)
            return nums

        return q_sort(nums, 0, n-1)

    # 针对上一个快排的精简版
    def sortArray_quick(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def partition(left, right):
            pivot_key = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot_key:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot_key:
                    left += 1
                nums[right] = nums[left]

            nums[left] = pivot_key

            return left

        def quick_sort(left, right):
            if left < right:
                mid = partition(left, right)
                quick_sort(left, mid - 1)
                quick_sort(mid + 1, right)
            else:
                return

        quick_sort(0, n - 1)
        return nums

    def sortArray_1(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def merge(low, mid, high):
            i, j = low, mid + 1
            tmp = []
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1

            if i <= mid:
                tmp.extend(nums[i:mid + 1])

            if j <= high:
                tmp.extend(nums[j:high + 1])

            nums[low:high + 1] = tmp

        def merge_sort(low, high):
            if low < high:
                #  mid = low + ((high-low)>>1)
                mid = low + (high - low) // 2
                merge_sort(low, mid)
                merge_sort(mid + 1, high)
                merge(low, mid, high)
            else:
                return
        merge_sort(0, n - 1)
        return nums


if __name__ == '__main__':
    s = Solution()
    # nums = [51, 13, 76, 43, 26, 57, 23, 69]
    # nums = [0]
    # nums = [5, 1, 1, 2, 0, 0]
    # nums = [4, 2, 1, 5, 6, 7, 11, 9]
    nums = [0,1]
    # print(s.sortArray(nums))
    # print(s.sortArray(nums))
    # print(s.sortArray_QuickSort(nums))
    print(s.sortArray_333(nums))
    # print(s.sortArray_bubleSort(nums))
    # print(s.sortArray_insertionSort(nums))
    # print(s.sortArray_SelectionSort(nums))
    # print(s.sortArray_MergeSort(nums))
    # print(s.sortArray_QuickSort(nums))