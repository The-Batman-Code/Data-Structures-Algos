class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(
        self, index, value
    ):  # Edge cases here are insertion at first[index 0], negative index and index more than the available index
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(
                index - 1
            ):  # TC of this loop is O(n) in worst case. All others operations have TC of O(1)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True


# Overall time complexity of insert function is O(n) due to the for loop. SC is O(1) as no additional memory is required to do this operation

newlinkedlist = LinkedList()
newlinkedlist.append(10)
newlinkedlist.append(20)
newlinkedlist.append(30)
print(newlinkedlist)
newlinkedlist.prepend(5)
print(newlinkedlist)
newlinkedlist.insert(1, 69)
print(newlinkedlist)
