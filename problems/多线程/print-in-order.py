# -*- coding:utf-8 -*-
#@Time  :    2020/8/25 2:45 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    print-in-order.py
#@Description：https://leetcode-cn.com/problems/print-in-order/

import threading
from typing import Callable

## pv信号灯
class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.s2.acquire()
        printThird()


def printFirst():
    print("printFirst")

def printSecond():
    print("printSecond")

def printThird():
    print("printThird")

if __name__ == '__main__':
    nums = [3,2,1]
    f = Foo()
    for num in nums:
        if num == 1:
            t = threading.Thread(target=f.first, args=(printFirst,))
            t.start()
        elif num == 2:
            t = threading.Thread(target=f.second, args=(printSecond,))
            t.start()
        elif num == 3:
            t = threading.Thread(target=f.third, args=(printThird,))
            t.start()
        else:
            break
