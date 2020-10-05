from typing import List

# dp[i] 表示钱为i的组合数量
# coin 是遍历
# dp[i] = max(dp[i],dp[i-coin]+1)

# 使用动态规划来，会有相同的值
def coinChange( coins: List[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(1, amount + 1):
        for coin in coins:
            if (i - coin) >= coin:
                dp[i] += dp[i-coin] + 1
    print(dp)
    return dp[amount]

def getRes(amount,arr,index):
    tmp = []
    ans = 0
    def getnum(sum,arr,index):
        nonlocal ans
        if sum < 0:
            return
        if sum == 0:
            ans += 1
        for i in range(index, len(arr)):
            tmp.append(arr[i])
            getnum(sum-arr[i], arr, i)
            tmp.pop()
    getnum(amount, arr, index)
    print(ans)

# def coinChange( coins: List[int], amount: int) -> int:
#     factor_map = {}
#     sort_list = sorted(coins,reverse=True)
#     # 给每个元素分配一个因子
#     for c in coins:
#         factor_map[c] = amount // c
#
#     # 然后便利循环因子,从大的往小减
#     total = 0
#     res = 0
#     while 1:
#         # 随机检查，
#         for c in coins:
#             total +=  c*factor_map[c]
#         if total == amount:
#             res += 1
#         if total <= amount:
#             break
        # 把字典的系数从大到小减1

# 输入用例
# 5
# 1,2,5
# 结果为4
str_money_total = input()
str_coins = input()
amount = int(str_money_total)
coins = [int(i) for i in str_coins.split(",")]
# print(str(coinChange(coins, amount)))
getRes(amount, coins,0)