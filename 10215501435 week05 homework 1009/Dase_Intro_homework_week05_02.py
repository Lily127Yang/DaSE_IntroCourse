class Queue():
    def __init__(self):
        self.__items = []

    def size(self):  # 返回队列长度
        return len(self.__items)

    def isempty(self):  # 返回队列是否为空
        if len(self.__items) == 0:
            return True
        else:
            return False

    def push(self, element):  # 入队
        self.__items.append(element)

    def pop(self):  # 出队，注意需要处理队列为空的情况
        try:
            return self.__items.pop(0)
        except:
            print('ERROR: Queue is empty now!')

    def peek(self):  # 取队首，注意需要处理堆栈为空的情况
        try:
            return self.__items[0]
        except:
            print('ERROR: Queue is empty now!')

    def tail(self):  # 取队尾，注意需要处理堆栈为空的情况
        try:
            return self.__items[-1]
        except:
            print('ERROR: Queue is empty now!')


s = Queue()
s.push(1)  # 队列目前为 [1]
print(s.pop())  # 堆栈目前为 [ ]
print(s.pop())  # 错误，堆栈为空

print('**********')

s.push(3.5)  # 堆栈目前为[3.5]
s.push(2.7)  # 堆栈目前为[3.5, 2.7]
print(s.peek())
print(s.tail())
print(s.size())
print(s.isempty())