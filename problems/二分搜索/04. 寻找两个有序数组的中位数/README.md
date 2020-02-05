## 题目地址
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

## 题目描述（困难）
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
```
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```

## 相关企业(从左到右，按频率排序)
字节跳动、亚马逊、阿里巴巴、谷歌

## 解法
### 方法一：暴力破解法
遍历，直到两个值的和与target相等
时间复杂度：O(n^2) 
空间复杂度：O(1)
**耗时：2952 ms 内存消耗：12.6 MB**

### 方法二：哈希表法1
在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
然后，在第二次迭代中，我们将检查每个元素所对应的目标元素
```（target - nums[i]）```是否存在于表中。
注意，该目标元素不能是 ```nums[i] ```本身！
时间复杂度：O(n) 
空间复杂度：O(n)
**耗时：44 ms 内存消耗：13.4 MB**

### 方法三：哈希表法2
在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
如果它存在，那我们已经找到了对应解，并立即将其返回。
时间复杂度：O(n) 
空间复杂度：O(n)
**耗时：40 ms 内存消耗：13.2 MB**

## 代码
python:
```
   def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for index, value in enumerate(nums):
            if target - value in dct:
                return [dct[target - value], index]
            dct[value] = index
};
```

Java
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

```
