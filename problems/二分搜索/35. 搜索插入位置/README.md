## 题目地址
https://leetcode-cn.com/problems/search-insert-position/

## 题目描述（简单）
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
```
示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
```
## 相关企业(从左到右，按频率排序)
字节跳动、谷歌

## 解法
### 方法一：比较法
遍历数组，逻辑判断
时间复杂度：O(n) 

### 方法二：二分查找
每次根据 ```nums[mid]``` 和 target 之间的大小进行判断，相等则直接返回下标，
```nums[mid] < target ```则 left 右移，```nums[mid] > target``` 则 right 左移
查找结束如果没有相等值则返回 left，该值为插入位置
时间复杂度：O(logn) 

* 为避免边界条件出错，直接套用模板
* left+1,是因为下取整，如果是上取整，则right-1。这样才能保证left = right，跳出循环
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1; // 注意
        while(left <= right) { // 注意
            int mid = (left + right) / 2; // 注意
            if(nums[mid] == target) { // 注意
                // 相关逻辑
            } else if(nums[mid] < target) {
                left = mid + 1; // 注意
            } else {
                right = mid - 1; // 注意
            }
        }
        // 相关返回值
        return 0;
    }
}
```
## 代码
python:
```
   def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

```
java
```
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while(left <= right) {
            int mid = (left + right) / 2;
            if(nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```