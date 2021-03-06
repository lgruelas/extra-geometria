class EventQueue:
    """
        Implementado como una heap en lugar de un arbol binario porque en este
        caso debo agregar dos veces el mismo punto de evento, dado que uno
        puede pertenecer al conjunto azul y otro al rojo.
    """
    def __init__(self):
        self._heap_list = [None]
        self._count = 0

    def __heapify_down(self):
        idx = 1
        while self.__has_child(idx):
            greatest_child_idx = self.__get_greatest_child_idx(idx)
            if self._heap_list[idx] < self._heap_list[greatest_child_idx]:
                tmp = self._heap_list[greatest_child_idx]
                self._heap_list[greatest_child_idx] = self._heap_list[idx]
                self._heap_list[idx] = tmp
            idx = greatest_child_idx

    def __heapify_up(self):
        idx = self._count
        while self.__get_parent_idx(idx) > 0:
            if self._heap_list[self.__get_parent_idx(idx)] < self._heap_list[idx]:
                tmp = self._heap_list[self.__get_parent_idx(idx)]
                self._heap_list[self.__get_parent_idx(idx)] = self._heap_list[idx]
                self._heap_list[idx] = tmp
            idx = self.__get_parent_idx(idx)

    def __is_empty(self):
        return self._count == 0

    def is_empty(self):
        return self.__is_empty()

    def __get_parent_idx(self, idx):
        return idx // 2

    def __get_right_child_idx(self, idx):
        return  (idx * 2) + 1

    def __get_left_child_idx(self, idx):
        return idx * 2

    def __has_child(self, idx):
        return self.__get_left_child_idx(idx) <= self._count

    def __get_greatest_child_idx(self, idx):
        if self.__has_child(idx):
            right_child_idx = self.__get_right_child_idx(idx)
            if right_child_idx > self._count:
                return self.__get_left_child_idx(idx)
            left_child_idx = self.__get_left_child_idx(idx)
            if self._heap_list[left_child_idx] < self._heap_list[right_child_idx]:
                return right_child_idx
            return left_child_idx
        return None

    def add(self, element):
        self._count += 1
        self._heap_list.append(element)
        self.__heapify_up()

    def peek(self):
        if not self.__is_empty():
            return self._heap_list[1]
        return None

    def pop(self):
        if not self.__is_empty():
            max_value = self._heap_list[1]
            self._count -= 1
            if self._count == 0:
                self._heap_list.pop()
                return max_value
            self._heap_list[1] = self._heap_list.pop()
            self.__heapify_down()
            return max_value
        return None

    def __repr__(self):
        return "[ " + " ".join(map(str, self._heap_list[1:])) + " ]"