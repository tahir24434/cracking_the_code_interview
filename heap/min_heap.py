
class MinHeap(object):
    # Since the entire binary heap can be represented by a single list, all the constructor will do is initialize the
    # list and an attribute currentSize to keep track of the current size of the heap
    def __init__(self):
        # notice that an empty binary heap has a single zero as the first element of heapList and that this zero is not
        # used, but is there so that simple integer division can be used in later methods.
        self.heap_list = [0]
        self.size = 0

    @staticmethod
    def __get_parent(i):
        return i//2

    @staticmethod
    def __get_left(i):
        return 2 * i

    @staticmethod
    def __get_right(i):
        return 2 * i + 1

    def __swap(self, index1, index2):
        tmp = self.heap_list[index1]
        self.heap_list[index1] = self.heap_list[index2]
        self.heap_list[index2] = tmp

    def __move_up(self, i):
        parent_index = self.__get_parent(i)
        while self.heap_list[i] < self.heap_list[parent_index] and (i // 2 > 0): # try parent_index > 0
            self.__swap(i, parent_index)
            i = parent_index

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.__move_up(self.size)

    def min_child_index(self,i):
        left_index = self.__get_left(i)
        right_index = self.__get_right(i)
        if right_index > self.size:
            return left_index
        else:
            if self.heap_list[left_index] < self.heap_list[right_index]:    # Change sign for maxheap.
                return left_index
            else:
                return right_index

    def move_down(self, i):
        while i*2 <= self.size:
            child_index = self.min_child_index(i)
            if self.heap_list[i] > self.heap_list[child_index]:             # change sign for maxheap.
                self.__swap(i, child_index)
            i = child_index

    def get_min(self):
        # Get root item
        min_item = self.heap_list[1]
        # To restore root, place last item as root
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        # restore heap order property by moving root to appropriate place.
        # Swap the root with its smallest child less than the root. Keep doing this unless root becomes smaller than
        # both of his children.
        self.heap_list.pop()
        self.move_down(1)
        return min_item

    def build_heap(self, list):
        i = len(list) // 2
        self.size = len(list)
        self.heap_list = [0] + list[:]
        while i > 0:
            self.move_down(i)
            i -= 1

mh = MinHeap()
mh.build_heap([9, 5, 6, 2, 3])
print (mh.heap_list)
print(mh.get_min())
print(mh.get_min())
print(mh.get_min())
print(mh.get_min())
print(mh.get_min())

# In an integer array with N elements (N is large), find the maximum k elements.
min_heap = MinHeap()
A = [9, 5, 6, 2, 1, 7, 3, 8, 4]
K = 5
min_heap.build_heap(A[:K])
print (min_heap.heap_list)
for i in range(K, len(A)):
    if A[i] > min_heap.heap_list[1]:
        # Bring new element in.
        min_heap.heap_list[1] = A[i]
        min_heap.move_down(1)
print (min_heap.heap_list)


