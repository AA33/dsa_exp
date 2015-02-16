__author__ = 'aanurag'

import sys


class ListNode:
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.node = None
        self.length = 0

    def insert(self, val):
        new_node = ListNode()
        new_node.val = val
        new_node.next = self.node
        self.node = new_node
        self.length += 1

    def ordered_insert(self, val):
        new_node = ListNode()
        new_node.val = val
        cur_node = self.node
        while cur_node:
            if cur_node.val <= val:
                new_node.next = cur_node
                cur_node = new_node
                break
            cur_node = cur_node.next
        self.length += 1

    def delete(self):
        if self.node is not None:
            self.node = self.node.next
            self.length -= 1

    def print_all_elems(self):
        cur_node = self.node
        i = 0
        while cur_node != None and i < 25:
            sys.stdout.write(str(cur_node.val) + ' ')
            cur_node = cur_node.next
            i += 1
        if i == 25:
            print('...')
        else:
            print

    def force_cycle(self):
        at = self.length - 5
        at_node = self.node
        for i in range(1, at):
            at_node = at_node.next
        last_node = self.node
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = at_node

    def has_cycle(self):
        hare = turtle = self.node
        while hare.next is not None:
            hare = hare.next.next
            if hare == turtle: return LinkedList.find_cycle_length(hare)
            turtle = turtle.next
            if hare == turtle: return LinkedList.find_cycle_length(hare)
        return 0

    @staticmethod
    def find_cycle_length(hare):
        cycle_length = 1
        start = hare
        hare = hare.next
        while hare != start:
            hare = hare.next
            cycle_length += 1
        return cycle_length

    def reverse(self):
        reverse = self.node
        current = reverse.next
        reverse.next = None
        while current:
            next_node = current.next
            current.next = reverse
            reverse = current
            current = next_node
        self.node = reverse

    def reverse_without_temp(self):
        reverse = self.node
        current = reverse.next
        reverse.next = None
        while self.node.next:
            next_node = current.next
            current.next = reverse
            reverse = current
            current = next_node
        self.node = reverse


# Main
def main():
    linked_list = LinkedList()
    for i in range(10):
        linked_list.insert(i)
    linked_list.print_all_elems()
    linked_list.reverse()
    linked_list.print_all_elems()
    linked_list.delete()
    print("Deleted list:")
    linked_list.print_all_elems()
    print("Length:" + str(linked_list.length))
    print("Cycle length:" + str(linked_list.has_cycle()))
    linked_list.force_cycle()
    linked_list.print_all_elems()
    print("Cycle length:" + str(linked_list.has_cycle()))


if __name__ == "__main__":
    sys.exit(main())

