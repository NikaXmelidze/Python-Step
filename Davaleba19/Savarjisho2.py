class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self, data, index):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0

        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    #davalebis metodi
    def remove_index(self, index):
        
        if self.head is None:
            return None
        
        if index == 0:
            self.head = self.head.next
        
        current_node = self.head
        current_index = 0

        while current_node.next and current_index < index-1:
            current_node = current_node.next
            current_index += 1

    
        current_node.next = current_node.next.next



    def display_info(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(4)
linked_list.append(4)
linked_list.append(11)
linked_list.append(25)
linked_list.display_info()
linked_list.insert("Irakli", 3)
linked_list.insert(10.1, 5)
linked_list.display_info()
linked_list.remove("Irakli")
linked_list.remove(3)
linked_list.display_info()
#washlis magaliti
linked_list.remove_index(4)
linked_list.display_info()