## 题目地址
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
## 题目描述（简单）
```
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
```
## 相关企业(从左到右，按频率排序)


## 解法
### 方法一：递归
 DFS（深度优先搜索）
每个结点只访问一次，时间复杂度：O(n) 

空间复杂度：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，
递归将会被调用 NN 次（树的高度），因此保持调用栈的存储将是 O(N)O(N)。
但在最好的情况下（树是完全平衡的），树的高度将是 \log(N)log(N)。
因此，在这种情况下的空间复杂度将是 O(\log(N))O(log(N))。

### 方法二：迭代
从包含根结点且相应深度为 1 的栈开始。然后我们继续迭代：将当前结点弹出栈并推入子结点。每一步都会更新深度。

* 时间复杂度：O(N) 

* 空间复杂度：O(N)。


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