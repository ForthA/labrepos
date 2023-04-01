class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_parent(self, index):
        return (index - 1) // 2

    def get_left_child(self, index):
        return 2 * index + 1

    def get_right_child(self, index):
        return 2 * index + 2

    def insert(self, element):
        self.heap.append(element)
        self.sift_up(self.size)
        self.size += 1

    def extract_min(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop(self.size - 1)
        self.size -= 1
        self.sift_down(0)
        return min_element

    def sift_up(self, index):
        parent = self.get_parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)

    def sift_down(self, index):
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size and right >= self.size:
            return
        if right >= self.size:
            min_index = left if self.heap[left] < self.heap[index] else index
        else:
            min_index = left if self.heap[left] < self.heap[right] else right
            min_index = min_index if self.heap[min_index] < self.heap[index] else index
        if min_index != index:
            self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
            self.sift_down(min_index)

    def __str__(self):
        return str(self.heap)

