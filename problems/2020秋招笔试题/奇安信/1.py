
# 获取结果最大值

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# M包糖果，抛M次硬币，硬币连续n次为正面，最多能得到多少颗糖果
# @param candies int整型一维数组 每包糖果的数量
# @param coin int整型一维数组 抛硬币的结果
# @param n int整型 连续是正面的次数
# @return int整型
#

class Solution:

    def getSum(self, A, B):
        if A and B:
            sum = 0
            for i, j in zip(A, B):
                if j == 1:
                    sum += i
            return sum
        else:
            return 0

    def maxCandies(self, candies, coin, n):
        # 计算一下原始值
        length = len(candies)
        origin_max = 0
        for i in range(length):
            if coin[i] == 0:
                origin_max += candies[i]

        window_max = 0
        # 尽可能把0填充起来
        for i in range(length):
            # 求该滑动窗口的有效最大值
            end = min(length, i+n)
            tmp_max = self.getSum(candies[i:end],coin[i:end])
            window_max = max(tmp_max, window_max)
        return origin_max+window_max

if __name__ == '__main__':
    s = Solution()
    candies = [3, 5, 7, 2, 8, 8, 15, 3]
    coin = [1, 0, 1, 0, 1, 0, 1, 0]
    n = 3
    print(s.maxCandies(candies, coin, n))

