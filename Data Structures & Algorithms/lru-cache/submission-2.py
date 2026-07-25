class Node:
    def __init__(self, key, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.value_map = defaultdict(int)
        self.capacity = capacity
        self.total_items = 0

    def get(self, key: int) -> int:
        node = self.value_map[key]
        if not node:
            return -1
        self.put(key, node.value)
        return node.value

    def delete_node(self, key):
        print("Del", key)
        existing_node = self.value_map[key]
        next_node = existing_node.next
        prev_node = existing_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.value_map[key]
        self.total_items -= 1 

    def add_node(self, key, value):
        print("Add", key, value)
        new_node = Node(key, value)        
        temp = self.head.next
        self.head.next = new_node
        temp.prev = new_node
        new_node.next = temp
        new_node.prev = self.head
        self.value_map[key] = new_node
        self.total_items += 1


    def put(self, key: int, value: int) -> None:
        if self.value_map[key]:
            self.delete_node(key)
        elif self.total_items == self.capacity:
            self.delete_node(self.tail.prev.key)
        self.add_node(key, value)
        print("After put")
        print(self.value_map)

