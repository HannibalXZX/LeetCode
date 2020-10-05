## 题目地址
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

## 题目描述（中等）
```
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```
## 相关企业(从左到右，按频率排序)
字节跳动、亚马逊、脸书、微软、谷歌、中原银行*

## 解法
### 方法一：暴力破解法(超出时间限制)
从长度为2的子串开始遍历到原字符串
时间复杂度：O(n^3) 

### 方法二：优化暴力破解法(超出时间限制)
仿照优化冒泡算法，如果有一轮全有重复字母，则后面无需判断，但超出时间限制
时间复杂度：O(n^3) 

### 方法三：最大窗口移动(超出时间限制)
用局部最大的窗口来逼近全局最大的窗口

### 方法四：窗口移动【官方解答】


参考java代码，更为简洁、高效

滑动窗口是数组/字符串问题中常用的抽象概念。
窗口通常是在数组/字符串中由开始和结束索引定义的一系列元素的集合，即 ```[i, j)```（左闭，右开）。
而滑动窗口是可以将两个边界向某一方向“滑动”的窗口。
例如，我们将``` [i, j) ```向右滑动 1 个元素，则它将变为 ```[i+1, j+1)```（左闭，右开）。

使用 HashSet 将字符存储在当前窗口 ```[i, j)```（最初 j=i）中。
然后我们向右侧滑动索引 j，如果它不在 HashSet 中，我们会继续滑动 j。
直到 s[j] 已经存在于 HashSet 中。此时，我们找到的没有重复字符的最长子字符串将会以索引 i 开头。

* 时间复杂度：`O(2n) = O(n)`，在最糟糕的情况下，每个字符将被 i 和 j 访问两次。

* 空间复杂度：`O(min(m, n))`，与之前的方法相同。滑动窗口法需要 ```O(k)``` 的空间，其中
k 表示 Set 的大小。而 Set 的大小取决于字符串 n 的大小以及字符集 / 字母 m 的大小。


### 方法五：优化后的窗口移动【官方解答】

以前的我们都没有对字符串 s 所使用的字符集进行假设。

当我们知道该字符集比较小的时侯，我们可以用一个整数数组作为直接访问表来替换 Map。

常用的表如下所示：

* int [26] 用于字母 ‘a’ - ‘z’ 或 ‘A’ - ‘Z’
* int [128] 用于ASCII码
* int [256] 用于扩展ASCII码


时间复杂度：```O(n)```，索引 jj 将会迭代 nn 次。

空间复杂度（HashMap）：```O(min(m, n))```，与之前的方法相同。

空间复杂度（Table）：```O(m)```，m是字符集的大小。

作者：LeetCode



## 代码

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}

作者：LeetCode
```
```
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        int[] index = new int[128]; // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }
}

作者：LeetCode

```