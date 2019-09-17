class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += "\n"
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def enumerate(self):
        node = self.head
        while node:
            yield node.value
            node = node.next


def union(llist_1, llist_2):
    # Your Solution Here
    union_set = set()
    for item in llist_1.enumerate():
        union_set.add(item)
    for item in llist_2.enumerate():
        union_set.add(item)

    union_linked_list = LinkedList()
    for item in union_set:
        union_linked_list.append(item)

    return union_linked_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1 = set()
    set_result = set()
    #first, convert the first linked list to set
    for item in llist_1.enumerate():
        set_1.add(item)
    #then, check this against items of second linked list
    for item in llist_2.enumerate():
        if item in set_1:
            set_result.add(item)

    intersect_linked_list = LinkedList()
    for item in set_result:
        intersect_linked_list.append(item)

    return intersect_linked_list


if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    print (intersection(linked_list_1,linked_list_2)) # 4 -> 21 -> 6 ->

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4)) #prints 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    print (intersection(linked_list_3,linked_list_4)) #prints nothing

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6]
    element_2 = [6, 5, 4, 3, 2, 1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print (union(linked_list_5,linked_list_6)) #1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
    print (intersection(linked_list_5,linked_list_6)) #1 -> 2 -> 3 -> 4 -> 5 -> 6 ->