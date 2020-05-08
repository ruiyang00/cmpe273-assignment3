from DoubleLinkedlist import DoubleLinkedlist


class LRUCache():

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.map = dict()
        self.list = DoubleLinkedlist()

    def get(self, key):
        # print(key)
        if key in self.map.keys():
            node = self.map[key]
            self.list.addFront(node)
            if self.list.get_size() > 1:
                self.list.removeTail
            return node.value
        else:
            return None

    def set(self, key, value):
        self.list.addFront(value)
        self.map[key] = self.list.head.next
        print(self.list.head.next.value)
        if self.list.get_size() > self.maxSize:
            self.list.removeTail

    def getTail(self):
        return self.list.tail.pre.value

    def getHead(self):
        return self.list.head.next.value.value

    # def getFirst(self):
    #     print(self.list.head.next.value)


cache = LRUCache(5)
data1 = {'name': 'Brad Pitt', 'email': 'bpitt@gmail.com', 'age': 30}
data2 = {'name': 'Wall Bran', 'email': 'wbran@gmail.com', 'age': 18}
data3 = {'name': 'Robert Jennifer', 'email': 'rjennifer@gmail.com', 'age': 24}
# data4 = {'name': 'Matthew Lisa', 'email': 'mlisa@gmail.com', 'age': 32}
# data5 = {'name': 'Joseph Jessica', 'email': 'mlinda@gmail.com', 'age': 53}

cache.set("0802ee7e22b162891d6d4f45087aceb3", data1)
cache.set("42fb5671f4cdea22e894d5b77db8ac2f", data2)
cache.set("71fce5174c7ec7657710a1e5726af04e", data3)

a = cache.get("0802ee7e22b162891d6d4f45087aceb3")
# b = cache.get("42fb5671f4cdea22e894d5b77db8ac2f")
# c = cache.get("42f15671f4cdea22e894d5b77db8ac2f")

# print(a)
head = cache.getHead()
tail = cache.getTail()
# print("head: ", head)
print("head: ", cache.list.head.next.value.value)

# print(c)
