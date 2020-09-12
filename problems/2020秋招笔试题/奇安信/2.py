# 获得剩余区域内的最大干净矩形面积

# 40% 的用例


# @param x1 int整型
# @param y1 int整型
# @param x2 int整型
# @param y2 int整型
# @param x3 int整型
# @param y3 int整型
# @param x4 int整型
# @param y4 int整型
# @return int整型
#

class Solution:

    def initMartix(self , x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4 ):
        martix = []
        for i in range(11):
            martix.append([1]*11)

        # 根据坐标进行赋值为1
        for i in range(x1, x2+1):
            for y in range(y1, y2+1):
                martix[i][y] = 0

            # 根据坐标进行赋值为1
        for i in range(x3, x4 + 1):
            for y in range(y3, y4 + 1):
                martix[i][y] = 0
        # print(martix)
        return martix

    def getMaxArea(self , x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4 ):
        # 构建一个二维矩阵都为0的
        martix = self.initMartix(x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4)

        print(martix)
        n = len(martix)
        m = len(martix[0])

        left = [0]*m
        right = [m]*m
        height = [0]*m

        ans = 0

        for i in range(n):
            cur_left, cur_right = 0, m
            for j in range(m):
                if martix[i][j] == 1:
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1

            for j in range(m):
                if martix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(m-1, -1, -1):
                if martix[i][j] == 1:
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = m
                    cur_right = j

            for j in range(m):
                ans = max(ans,height[j]*(right[j]+-left[j]))

        return ans

    def getMaxArea_1(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # 构建一个二维矩阵都为0的
        matrix = self.initMartix(x1, y1, x2, y2, x3, y3, x4, y4)

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        maxArea = 0
        for i in range(m):
            curleft = 0
            curright = n
            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    left[j] = max(left[j], curleft)
                else:
                    left[j] = 0
                    curleft = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 1:
                    right[j] = min(right[j], curright)
                else:
                    right[j] = n
                    curright = j
            for j in range(n):
                maxArea = max(maxArea, height[j] * (right[j] - left[j]))
        return maxArea


if __name__ == '__main__':
    s = Solution()
    x1,y1,x2,y2 = 0, 0, 1, 1
    x3, y3, x4, y4 = 9, 9, 10, 10
    # x1,y1,x2,y2 = 4, 1, 6, 9
    # x3, y3, x4, y4 = 1, 4, 9, 6

    print(s.getMaxArea(x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4))
    print(s.getMaxArea_1(x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4))