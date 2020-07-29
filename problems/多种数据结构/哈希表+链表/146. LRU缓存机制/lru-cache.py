# -*- coding:utf-8 -*-
#@Time  :    2020/7/27 6:23 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    lru-cache.py
#@Description：  https://leetcode-cn.com/problems/lru-cache/

import collections

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

class DLinkedNode:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity:int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        # 记录当前缓存中元素的数量。
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # 如果key存在，取值
        node = self.cache[key]
        value = node.value

        # 移动到头节点
        # 1、先删除该节点 2、移动到头节点
        self.moveToHead(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至
            self.addToHead(node)
            self.size += 1
            ## 这里要考虑是否超出容量
            if self.size > self.capacity:
                removed_node = self.removeTail()
                self.cache.pop(removed_node.key)
                self.size -= 1

        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            # 这里包含着更新
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node:DLinkedNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node:DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node:DLinkedNode):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node







