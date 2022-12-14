class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev, self.next = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.size = capacity, 0
        self.dic = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def __insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.__remove(node)
        self.__insert(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            node = self.dic[key]
            self.__remove(node)
            node.value = value
            self.__insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self.__remove(discard)
                del self.dic[discard.key]
                self.size -= 1
            node = self.Node(key, value)
            self.dic[key] = node
            self.__insert(node)
            self.size += 1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)