class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def remove_beginning(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_at_end(self):
        if not self.head:
            return None
        
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next
        
        data = curr.next.data
        curr.next = None
        return data

    def remove_at(self, data):
        if not self.head:
            return None

        if self.head.data == data:
            return self.remove_beginning()

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                removed_data = curr.next.data
                curr.next = curr.next.next
                return removed_data
            curr = curr.next
        
        return None
