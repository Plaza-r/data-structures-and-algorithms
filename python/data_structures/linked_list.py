class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # init here
        self.head = None
        self.tail = None

    def __str__(self):
        text = ""
        current = self.head

        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            print(text)
            current = current.next
        return text + "NULL"

    def includes(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):

        new_node = Node(value)

        # start  beginning or head
        current = self.head

        while current:
            # next n/a
            if not current.next:

                current.next = new_node

                break
            else:
                # moves to next
                current = current.next

    def insert_before(self, search_value, value):
        node_two = Node(value)
        if not self.head:
            raise TargetError

        if self.head.value == search_value:
            self.insert(value)
            return

        # start  head || beginning
        current = self.head

        while current and current.next:
            # if current node has a value it looks for value
            if current.next.value == search_value:

                node_two.next = current.next

                current.next = node_two

                break
            # was told danger

            else:
                current = current.next
        else:
            raise TargetError

    def insert_after(self, search_value, value):

        current = self.head

        while current:
            if current.value == search_value:
                self.insert_before(current.next.value, value)
                return
            else:
                current = current.next
        raise TargetError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
