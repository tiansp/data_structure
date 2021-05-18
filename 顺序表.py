class SeqList(object):
    def __init__(self, max=10):
        self.max = max  # 默认顺序表最多容纳10个元素
        # 初始化顺序表数组
        self.num = 0
        self.data = [None] * self.max  # 占位了10个

    def is_empty(self):  # 判断线性表是否为空
        return self.num is 0

    def is_full(self):  # 判断线性表是否全满
        return self.num is self.max

    def __getitem__(self, index):  # 获取线性表中某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):  # 修改线性表中的某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            self.data[index] = value
        else:
            raise IndexError

    def locate_item(self, value):  # 按值查找第一个等于该值得索引
        for i in range(self.num):
            if self.data[i] == value:
                return i
        return -1

    def count(self):  # 返回线性表中元素的个数
        return self.num

    def append_last(self, value):  # 在表尾部插入一个元素
        if self.num > self.max:
            print("list is full")
        else:
            self.data[self.num] = value
            self.num += 1

    def insert(self, index, value):  # 在表中任意位置插入一个元素
        if self.num >= self.max:
            print("list is full")
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or index > self.num:
            raise IndexError
        print('num :', self.num)
        for i in range(self.num, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.num += 1

    def remove(self, index):  # 删除表中某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or index >= self.num:
            raise IndexError
        for i in range(index, self.num):
            self.data[i] = self.data[i + 1]
        self.num -= 1

    def print_list(self):  # 输出操作
        for i in range(0, self.num):
            print(self.data[i])

    def destroy(self):
        self.__init__()


if __name__ == '__main__':
    seqlist = SeqList()
    print(seqlist.is_empty())
    print(seqlist[3])
    seqlist[2] = 5
    print(seqlist[2])
    seqlist.append_last(7)
    seqlist.append_last(4)
    seqlist.append_last(6)
    seqlist.append_last(3)
    seqlist.insert(3, 11)
    #     seqlist.remove(3)

    print("---------")
    seqlist.print_list()
    print("---------")
    for x in seqlist:
        print(x)
    print("---------")
    seqlist.destroy()
    #     for x in seqlist:
    #         print(x)
    seqlist.print_list()
