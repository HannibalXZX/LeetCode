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

### 方法：二分搜索法
* 时间复杂度：O(m∗log(mn))
* 空间复杂度：O(1)

这道题可能有人会想着先构造出这个乘法表，然后再去搜索，但这样是行不通的，
因为m、n的取值可能非常大，非常耗内存。首先我们知道在m、n的乘法表中取值范围为[1, m * n]，
那么我们可不可以使用使用二分搜索呢？

首先观察乘法表我们会发现，由于构造关系，决定了他每一行都是递增的。

如果我们需要在第i行中寻找大于num的个数，我们只要```min(num / i, n)```，
其中（i是这一行的行号，n是矩阵的列数）num / i代表的是如果num也在第i行，
它存在的列数，所以只要取最小值就是第i行不大于num的个数。
（比如例题1中，我们需要知道第2行，不大于4的个数，```min(4 / 2, 3) == 2个（就是2， 4）```）

那么如果我们需要确定这个乘法表中不大于num的个数就非常简单了，我们只要将每一行
不大于num的个数累加即可。（比如例题1中，我们需要知道乘法表中不大于4的个数，
第一行3个、第二行2个，第三行1个）

现在我们就可以使用二分搜索了，初始化```left = 1， right = n * m + 1，
mid = （left + right） / 2```，在m，n的乘法表中寻找不超过mid的个数。
--------------------- 
作者：hestyle [csdn原文](https://blog.csdn.net/qq_41855420/article/details/89397884) 

很多人担心最终返回的值不在乘法表内，这是不用担心的。

二分搜索和值其实无关，只是帮你快速地缩小范围。退出while循环时，一定是letft = right。而此时letf和right值相等，就是乘法表中某个具体的值，无论是多少，都能取到的。

## 代码   
python:
```
  # 在m*n乘法表中比num小的数字的数目
    def count_smaller_than_num(self,m, n, num):
        '''
        :type m: int
        :type n: int
        :type num: int
        :return: count int
        '''
        count = 0
        for i in range(1, m+1):
            count += min(int(num/i), n)
        return count

 # 在m*n乘法表中寻找第k小的数, 二分法, 错误解法
    def findKthNumber_wrong(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # 处理边界问题
        if k == 1:
            return 1
        elif k == m*n:
            return m*n
        else:
            left = 1
            right = m*n
            while(left < right):
                mid = int((left + right) >> 1)
                count_smaller_than_mid = self.count_smaller_than_num(m, n, mid)
                # 这里不能返回，因为此时的mid可能不在乘法表中
                if count_smaller_than_mid == k:
                    return mid
                elif count_smaller_than_mid < k:
                    left = mid + 1
                else:
                    right = mid

            return right

    # 在m*n乘法表中寻找第k小的数, 二分法
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # 处理边界问题
        if k == 1:
            return 1
        elif k == m*n:
            return m*n
        else:
            left = 1
            right = m*n
            while(left < right):
                mid = int((left + right) >> 1)
                count_smaller_than_mid = self.count_smaller_than_num(m, n, mid)
                if count_smaller_than_mid < k:
                    left = mid + 1
                else:
                    right = mid

            return right

 # 在m*n乘法表中寻找第k小的数, 二分法
 def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # 处理边界问题
        if k == 1:
            return 1
        elif k == m*n:
            return m*n
        else:
            left = 1
            right = m*n
            while(left < right):
                mid = int((left + right) >> 1)
                count_smaller_than_mid = self.count_smaller_than_num(m, n, mid)
                if count_smaller_than_mid < k:
                    left = mid + 1
                else:
                    right = mid

            return right

```

java
```
class Solution {
public:
    //Binary Search for value
    //跟普通二分不一样 普通二分把下标来当作边界，而这里的二分则是把值来当作边界
    int fun(int m, int n, int num) {//函数功能：获得在m*n的乘法表中，找出有多少个值 <= num。返回满足条件的值的数量
        int count = 0;
        for(int i = 1; i<=m; ++i) {//行从第一行开始
            count += min(num/i, n);//此表达式的含义：num这个值在当前第i行，有多少个值不比它大（<=num的个数）
        }
        return count;
    }
    int findKthNumber(int m, int n, int k) {
        if(k == 1) return 1;
        if(k == m*n) return m*n;
        int left = 1, right = m*n, mid;//值来当作边界，乘法表（m*n）最小是1，最大是m*n
        while(left < right) {
            mid = (left+right) >> 1;
            int temp = fun(m, n, mid);//得到在乘法表中 值 <= mid 的数量
            if(temp < k) {
                left = mid+1;//如果temp < k, 说明当前mid这个值在目标值的左边（比目标值小），所以可以缩小边界
            }
            else right = mid;//temp >= k， 在temp>k时，为什么不取 right = mid-1，而是right = mid。因为我们的目标值可能存在重复，比如 123334，如果我选择要找第3小的数，而mid当前恰好=3，那么temp得到的结果会是5（<=mid）。如果我们选择right = mid-1=2。那么将会运行错误导致结果错误。在temp = k时，为什么不能立马返回结果呢，而是继续运行缩小边界？因为我们当前的mid可能是一个不在乘法表中的值，毕竟mid=(left+right) >> 1; 所以立即返回可能返回错误答案。所以一定收缩范围 直到left=right。最终返回的一定是正确值（若答案t的temp = k， 而某一非表值x的temp也=k， 那么t一定比x小，最终x也会被right缩小导致出局）。
        }
        return left;
    }
};

```