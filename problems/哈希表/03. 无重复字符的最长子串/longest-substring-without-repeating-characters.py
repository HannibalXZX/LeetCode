# -*- coding:utf-8 -*-
# @Time  :    2020/2/7 10:32
# @Author:    Shaw
# @mail  :    shaw@bupt.edu.cn
# @File  :    longest-substring-without-repeating-characters.py
# @Description：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution(object):

    # 判断是否有重复的字母
    def has_repeated_char(self, str):
        str_list = []
        repeate_falg = 0
        for i in str:
            if i in str_list:
                repeate_falg = 1
            str_list.append(i)
        return repeate_falg

    # 暴力破解法-超出时间限制
    def lengthOfLongestSubstring_01(self, s):
        """
        :type s: str
        :rtype: int
        range 和 str 都是左闭右开区间
        """
        length = len(s)
        result = 1
        # 注意空字符串
        if length == 0:
            return 0
        for count in range(1, length):
            for i in range(0, length):
                if (i + count) >= length:
                    break
                else:
                    current_string = s[i:i + count + 1]
                    print(current_string)
                    if self.has_repeated_char(current_string):
                        continue
                    else:
                        result = count + 1
        return result

    # 提前判断，稍作优化，如果有一轮全有重复字母，则后面无需判断，但超出时间限制
    def lengthOfLongestSubstring_02(self, s):
        """
        :type s: str
        :rtype: int
        range 和 str 都是左闭右开区间
        """
        length = len(s)
        result = 1
        # 注意空字符串
        if length == 0:
            return 0
        for count in range(1, length):
            all_repeat_flag = 1
            for i in range(0, length):
                if (i + count) >= length:
                    break
                else:
                    current_string = s[i:i + count + 1]
                    print(current_string)
                    if self.has_repeated_char(current_string):
                        continue
                    else:
                        all_repeat_flag = 0
                        result = count + 1
            if all_repeat_flag == 1:
                break
        return result

    # 取最大值
    def lengthOfLongestSubstring_03(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        # 注意空字符串
        if length == 0:
            return 0
        # 最大长度值
        max_length = 1
        # 间距
        count = 1
        for i in range(0, length):
            while (i + count) <= length - 1:
                current_string = s[i:i + count + 1]
                if self.has_repeated_char(current_string):
                    break  # 遇到有重复的则退出
                else:
                    count += 1
            if count > max_length:
                max_length = count

        return max_length

    # 滑动窗口来做
    def lengthOfLongestSubstring_04(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        slide_window = list() # 不允许有重复的对象
        length = len(s)
        max_length = 0
        count = 0
        # 双指针操作
        for i in range(0, length):
            if s[i] in slide_window:
                if count > max_length:
                    max_length = count
                # 从左边去除滑动窗口内与s[i]相等的元素
                while slide_window and s[i] != slide_window[0]:
                    slide_window.remove(slide_window[0])
                # 细节
                slide_window.remove(slide_window[0])
                slide_window.append(s[i])
            else:
                slide_window.append(s[i])
                # print(slide_window)
                count = len(slide_window)
            if count > max_length:
                max_length = count
        return max_length

if __name__ == '__main__':
    s = Solution()
    str = "abcbd"
    # print(s.has_repeated_char(str))
    print(s.lengthOfLongestSubstring_04(str))
