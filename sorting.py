class Sort:

    def __init__(self, elements):
        self.original_elements = elements
        self.bubble_elements = None
        self.insertion_elements = None
        self.merge_elements = self.original_elements.copy()
        self.quick_elements = self.original_elements.copy()
        self.merge_elements_count = 0

    def bubble_sort(self):
        self.bubble_elements = self.original_elements.copy()
        # ^ it's not needed, this operation can be easily done on the original_elements

        for i in range(0, len(self.bubble_elements) - 1):
            for j in range(i + 1, len(self.bubble_elements) - i):
                if self.bubble_elements[i] > self.bubble_elements[j]:
                    self.bubble_elements[i], self.bubble_elements[j] = self.bubble_elements[j], self.bubble_elements[i]

        print(self.bubble_elements)

    def insertion_sort(self):
        self.insertion_elements = self.original_elements.copy()
        # ^ it's not needed, this operation can be easily done on the original_elements

        for i in range(0, len(self.insertion_elements)):
            for j in range(0, i):
                if self.insertion_elements[i] < self.insertion_elements[j]:
                    self.insertion_elements[i], self.insertion_elements[j] = self.insertion_elements[j], \
                        self.insertion_elements[i]

        print(self.insertion_elements)

    def merge(self, left_elements, right_elements, elements):
        left_elements_size = len(left_elements)
        right_elements_size = len(elements) - left_elements_size
        i = 0
        l = 0
        r = 0
        while l < left_elements_size and r < right_elements_size:
            if left_elements[l] < right_elements[r]:
                elements[i] = left_elements[l]
                l += 1
            else:
                elements[i] = right_elements[r]
                r += 1
            i += 1

        while l < left_elements_size:
            elements[i] = left_elements[l]
            l += 1
            i += 1

        while r < right_elements_size:
            elements[i] = right_elements[r]
            r += 1
            i += 1

    def merge_sort(self, elements=None):
        if not elements:
            elements = self.merge_elements
        if len(elements) == 1:
            return
        middle = int(len(elements) / 2)
        left_elements = elements[:middle]
        right_elements = elements[middle:]
        self.merge_sort(left_elements)
        self.merge_sort(right_elements)
        self.merge(left_elements, right_elements, elements)

    def partition(self, array, start, end):
        if len(array) <= 1:
            return 0
        i = start - 1
        pivot = array[end]

        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1

    def quick_sort(self, array_elements=None, start=None, end=None):

        if not array_elements:
            array_elements = self.quick_elements

        if start is None:
            start = 0
        if end is None:
            end = len(array_elements) - 1

        if end <= start:
            return

        pivot_position = self.partition(array_elements, start, end)
        self.quick_sort(array_elements, start, pivot_position - 1)
        self.quick_sort(array_elements, pivot_position + 1, end)


elements = [1, 3, 2, 6, 7, 8, 4, 5, 9]
s1 = Sort(elements)
print(f"Input {elements}")
s1.bubble_sort()
s1.insertion_sort()
s1.merge_sort()
print(s1.merge_elements)
s1.quick_sort()
print(s1.quick_elements)
