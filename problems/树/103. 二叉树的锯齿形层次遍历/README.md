## 题目地址
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

## 题目描述（中等）
```
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

```
## 相关企业(从左到右，按频率排序)


## 解法
### 方法一：BFS
该题与102题思路一样，都是层次遍历，只需要判断奇偶性即可。

python 要注意！
```
a = list()
a.reverse() 该函数没有返回值
所以list.append(a.reverse())添加的是null对象
```

* 时间复杂度：O(N)，其中 N 是树中节点的数量。每个节点仅访问一次。

双端队列的插入操作为常数时间。如果使用数组或 list，头部插入需要 \mathcal{O}(K)O(K) 的时间，其中 KK 是数组或 list 的长度。

* 空间复杂度：O(N)，其中 N 是树中节点的数量
任何时刻，双端队列中最多只存储两层节点。因此双端队列的大小不超过 2 ⋅L，其中 L 是一层的最大节点数。
包含最多节点的层可能是完全二叉树的叶节点层，大约有 L = \frac{N}{2}L= N/2个节点。因此最坏情况下，空间复杂度为 ⋅ 2N =N


作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/er-cha-shu-de-ju-chi-xing-ceng-ci-bian-li-by-leetc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




## 代码

```
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

作者：LeetCode
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
作者：LeetCode
```
```
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

作者：LeetCode
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```