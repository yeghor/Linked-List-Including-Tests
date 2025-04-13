from typing import List, Optional, Any


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:

    @staticmethod
    def clear_node(node: Node) -> None:
        node.prev = None
        node.next = None
        node.value = None

    def __validate_index(self, index):
        if not 0 <= index <= self.len:
            raise IndexError("Index out of range")

    class Iterator:
        def __init__(self, head, return_node=False):
            self.return_node = return_node
            self.bucket: Node = head

        def __iter__(self):
            return self
        
        def __next__(self):
            if not self.bucket:
                raise StopIteration            

            element = self.bucket
            self.bucket = self.bucket.next
            return element if self.return_node else element.value
        
        def __len__(self) -> int:
            count = 0
            current = self.bucket
            while current:
                count += 1
                current = current.next
            return count
                
    def __reset(self):
        current = self.__head_node
        while current:
            next_node = current.next
            self.__clear_node(current)
            current = next_node

        self.__head_node: Node = None
        self.__tail_node: Node = None
        self.head = None
        self.tail = None
        self.len: int = 0

    def __init__(self):
        self.__head_node: Optional[Node] = None
        self.__tail_node: Optional[Node] = None
        self.head: Optional[Any] = None
        self.tail: Optional[Any] = None
        self.len: int = 0

    def __str__(self) -> str:
        if not self.__head_node:
            return "Empty List"
        
        elements = list(str(elem) for elem in self.Iterator(head=self.__head_node, return_node=False))
        return " -> ".join(elements)

    def __iter__(self, return_node: bool = False) -> Iterator:
        return self.Iterator(head=self.__head_node, return_node=return_node)
    
    def __len__(self) -> int:
        return self.len

    def clear(self) -> None:
        self.__reset()

    def add(self, value) -> bool:
        node = Node(value)
        if not self.__head_node:
            self.__head_node = node
            self.__tail_node = node

            self.head = self.__head_node.value
            self.tail = self.__head_node.value
            self.len = 1
            return True
        
        self.__tail_node.next = node
        node.prev = self.__tail_node
        self.__tail_node = node
        self.tail = self.__tail_node.value

        self.len += 1
        return True
        
    def pop(self) -> Optional[Any]:
        if self.__head_node == None:
            return None

        if self.__head_node == self.__tail_node:
            node = self.__head_node
            self.__reset()
            return node.value

        else:
            node = self.__tail_node
            parent = self.__tail_node.prev
            parent.next = None
            self.__tail_node = parent
            self.tail = self.__tail_node.value
            self.len -= 1
            return node.value

    def delete_by_first_appeared_value(self, value) -> bool:
        if not self.__head_node:
            return False

        if self.__head_node.value == value:
            if self.__head_node.next:
                self.__head_node = self.__head_node.next
                self.head = self.__head_node.value
                self.len -= 1
                return True
            else:
                self.__reset()
                return True

        if self.__tail_node.value == value:
            if self.__head_node == self.__tail_node:
                node = self.__head_node
                self.__reset()
                return True
            else:
                self.__tail_node = self.__tail_node.prev
                self.__tail_node.next = None
                self.tail = self.__tail_node.value

                self.len -= 1
                return True  

        for item in self.Iterator(head=self.__head_node, return_node=True):
            if item.value == value:
                parent = item.prev
                next_ = item.next

                parent.next = next_
                next_.prev = parent
                self.len -= 1
                self.__clear_node(item)
                return True

        return False

    def search_by_index(self, index, return_node=False) -> Node | Any:
        self.__validate_index(index)

        if not self.head:
            return None
        
        for i, elem in enumerate(self.Iterator(head=self.__head_node, return_node=True)):
            if i == index:
                return elem if return_node else elem.value

    def insert_at_index(self, index: int, value) -> bool:
        self.__validate_index(index)
        
        new_node = Node(value)

        if index == 0:
            if not self.head:
                self.__head_node = new_node
                self.__tail_node = new_node
            else:
                new_node.next = self.__head_node
                self.__head_node.prev = new_node
                self.__head_node = new_node
            self.head = self.__head_node.value
        
        elif index == self.len:
            self.__tail_node.next = new_node
            new_node.prev = self.__tail_node
            self.__tail_node = new_node
            self.tail = self.__tail_node.value
        
        else:
            previous = self.__head_node

            for _ in range(index - 1):
                previous = previous.next

            next_ = previous.next

            previous.next = new_node
            new_node.prev = previous
            new_node.next = next_
            next_.prev = new_node
        
        self.len += 1
        return True


    def delete_by_index(self, index) -> bool:
        if not 0 <= index < self.len:
            raise IndexError("Index out of range")

        if not self.head:
            return False

        if index == 0:
            node_to_delete = self.__head_node
            if self.__head_node == self.__tail_node:
                self.clear()
            else:
                self.__head_node = self.__head_node.next
                self.__head_node.prev = None

        
        elif index == self.len - 1:
            node_to_delete = self.__tail_node
            if self.__head_node == self.__tail_node:
                self.clear()
            else:
                self.__tail_node = self.__tail_node.prev
                self.__tail_node.next = None
                
        else:
            current = self.__head_node
            for _ in range(index):
                current = current.next

            node_to_delete = current
            parent = current.prev
            child = current.next

            parent.next = child
            child.prev = parent

        self.__clear_node(node_to_delete)
        self.len -= 1
        return True
    
    def to_list(self) -> List[Any]:
        return list(value for value in self.Iterator(head=self.__head_node, return_node=False))
    
    def reverse(self) -> None:
        if not self.head:
            return
        
        array = list(value for value in self.Iterator(head=self.__head_node, return_node=False))
        array.reverse()
        self.clear()
        for value in array:
            self.add(value)
        
    def contains(self, value) -> bool:
        for item in self.Iterator(head=self.__head_node, return_node=False):
            if item == value:
                return True
        return False
    
    def index_of(self, value) -> int:
        for index, item in enumerate(self.Iterator(head=self.__head_node, return_node=False)):
            if item == value:
                return index
        return None
    
    def is_empty(self) -> bool:
        return self.len == 0
    
    def extend(self, values: List[Any]) -> None:
        for value in values:
            self.add(value)

    def count(self, value) -> int:
        count = 0
        for item in self.Iterator(head=self.head, return_node=False):
            if item == value:
                count += 1
        return count
    
    def reverse_in_place(self) -> None:
        if not self.__head_node or not self.__head_node.next:
            return
        
        if self.__head_node.next == self.__tail_node:
            self.__head_node.value, self.__tail_node.value = self.__tail_node.value, self.__head_node.value
            return

        # current_h = self.__head_node
        # current_t = self.__tail_node

        # while current_t != current_h and current_h.prev != current_t:
        #     current_h.next, current_t.value = current_t.value, current_h.value

        #     current_h = current_h.next
        #     current_t = current_t.prev

        current = self.__head_node  
        self.__head_node, self.__tail_node = self.__tail_node, self.__head_node
        

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
            
    def copy(self) -> "LinkedList":
        new_list = LinkedList()

        for item in self.Iterator(head=self.__head_node, return_node=False):
            new_list.add(item)
        return new_list

    def merge(self, list) -> None:
        if not isinstance(list, LinkedList):
            raise TypeError("Argument must be a LinkedList object")
        self.extend(list.to_list())

    def delete_all_occurances_by_value(self, value) -> None:
        while self.contains(value=value):
            self.delete_by_first_appeared_value(value)


ll = LinkedList()
for i in range(1, 11):
    ll.add(i)

print(ll)
ll.reverse_in_place()
print(ll)