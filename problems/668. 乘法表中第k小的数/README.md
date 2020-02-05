## 题目地址
https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/

## 题目描述（困难）
几乎每一个人都用乘法表。但是你能在乘法表中快速找到第k小的数字吗？
给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
```
示例 1:
输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).

示例 2:
输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).

注意：
m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。
```

## 相关企业(从左到右，按频率排序)
拼多多

## 解法
### 方法一：比较法
遍历数组，逻辑判断
时间复杂度：O(n) 
**耗时：36 ms 内存消耗：12.4 MB**

### 方法二：二分查找
每次根据 ```nums[mid]``` 和 target 之间的大小进行判断，相等则直接返回下标，
```nums[mid] < target ```则 left 右移，```nums[mid] > target``` 则 right 左移
查找结束如果没有相等值则返回 left，该值为插入位置
时间复杂度：O(logn) 

**为避免边界条件出错，直接套用模板**
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