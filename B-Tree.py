
class Entity(object):
    '''数据实体'''

    def __init__(self,key,value):
        self.key = key
        self.value = value

class Node(object):
    '''B树的节点'''

    def __init__(self):
        self.parent = None
        self.entitys = []
        self.childs = []

    def find(self,key):
        '''通过key查找并返回一个数据实体'''

        for e in self.entitys:
            if key == e.key:
                return e


    def delete(self,key):
        '''通过key删除一个数据实体,并返回它和它的下标(下标,实体)'''
        for i,e in enumerate(self.entitys):
            if e.key == key:
                del self.entitys[i]
                return (i,e)


    def isLeaf(self):
        '''判断该节点是否是一个叶子节点'''

        return len(self.childs) == 0


    def addEntity(self,entity):
        '''添加一个数据实体'''

        self.entitys.append(entity)
        self.entitys.sort(key=lambda x:x.key)


    def addChild(self,node):
        '''添加一个子节点'''

        self.childs.append(node)
        node.parent = self
        self.childs.sort(key=lambda x:x.entitys[0].key)

class Tree(object):
    '''B树'''

    def __init__(self,size=6):
        self.size = size
        self.root = None
        self.length = 0


    def add(self,key,value=None):
        '''插入一条数据到B树'''

        self.length += 1

        if self.root:
            current = self.root

            while not current.isLeaf():
                for i,e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[i]
                        break
                    elif e.key == key:
                        e.value = value
                        self.length -= 1
                        return
                else:
                    current = current.childs[-1]

            current.addEntity(Entity(key,value))

            if len(current.entitys) > self.size:
                self.__spilt(current)
        else:
            self.root = Node()
            self.root.addEntity(Entity(key,value))


    def get(self,key):
        '''通过key查询一个数据'''

        node = self.__findNode(key)

        if node:
            return node.find(key).value


    def delete(self,key):
        '''通过key删除一个数据项并返回它'''

        node = self.__findNode(key)

        if node:
            i,e = node.delete(key)

            #在节点不是叶子节点时需要做修复(取对应下标的子节点的最大的一个数据项来补)
            if not node.isLeaf():
                child = node.childs[i]
                j,entity = child.delete(child.entitys[-1].key)
                node.addEntity(entity)

                while not child.isLeaf():
                    node = child
                    child = child.childs[j]
                    j,entity = child.delete(child.entitys[-1].key)
                    node.addEntity(entity)

            self.length -= 1
            return e.value


    def isEmpty(self):
        return self.length == 0


    def __findNode(self, key):
        '''通过key值查询一个数据在哪个节点,找到就返回该节点'''

        if self.root:
            current = self.root

            while not current.isLeaf():
                for i, e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[i]
                        break
                    elif e.key == key:
                        return current
                else:
                    current = current.childs[-1]

            if current.find(key):
                return current


    def __spilt(self,node):
        '''
        分裂一个节点，规则为:
        1、中间的数据项移到父节点
        2、新建一个右兄弟节点，将中间节点右边的数据项移到新节点
        '''

        middle = len(node.entitys) / 2

        top = node.entitys[int(middle)]

        right = Node()

        for e in node.entitys[middle + 1:]:
            right.addEntity(e)

        for n in node.childs[middle + 1:]:
            right.addChild(n)

        node.entitys = node.entitys[:middle]
        node.childs = node.childs[:middle + 1]

        parent = node.parent

        if parent:
            parent.addEntity(top)
            parent.addChild(right)

            if len(parent.entitys) > self.size:
                self.__spilt(parent)
        else:
            self.root = Node()
            self.root.addEntity(top)
            self.root.addChild(node)
            self.root.addChild(right)

if __name__ == '__main__':
    t = Tree(4)
    t.add(20)
    t.add(40)
    t.add(60)
    t.add(70,'c')
    t.add(80)
    t.add(10)
    t.add(30)
    t.add(15,'python')
    t.add(75,'java')
    t.add(85)
    t.add(90)
    t.add(25)
    t.add(35,'c#')
    t.add(50)
    t.add(22,'c++')
    t.add(27)
    t.add(32)

    print(t.get(15))
    print(t.get(75))
    print(t.delete(35))
    print(t.delete(22))
    t.add((22,'lua'))
    print(t.get(22))
    print(t.length)
