__author__ = 'aanurag'

from linked_list import *
import random

class SkipListNode(ListNode):
    def __init__(self):
        ListNode.__init__(self)
        self.up =None
        self.down = None
        self.previous = None

class SkipList():

    def __init__(self):
        self.lists = [LinkedList]
        self.lists[0].node = SkipListNode()

    #inserts in order in the lowest level array: O(1) with closest node,O(n) without it
    def orderedInsert(self,new_node,closest_node=None):
        if closest_node:
            L0_node = closest_node
        else:
            L0_node = self.lists[0].node
        if L0_node.next:
            L0_node = L0_node.next
        while L0_node:
            if L0_node.val and L0_node.val > new_node.val:
                if L0_node.previous:
                    previous_node = L0_node.previous
                    previous_node.next = new_node
                    new_node.next = L0_node
                    new_node.previous = previous_node
                    L0_node.previous = new_node
                    break
            elif not L0_node.val or not L0_node.next:
                L0_node.next = new_node
                new_node.previous = L0_node
                break
            L0_node = L0_node.next

    #inserts key into the lowest level list and then promotes it upwards based on coin flips
    def insert(self,key):
        new_node = SkipListNode()
        new_node.val = key
        self.orderedInsert(new_node,self.search(key,True))
        flip = random.randint(0,1)
        level = 0
        level_node= new_node
        while flip == 1:
            level_up_node = SkipListNode()
            level_up_node.val = key
            #see if an upper level exists, if not create it
            if(len(self.lists)-1<=level):
                self.lists.append(LinkedList())
                up_list = self.lists[level+1]
                up_list.node = SkipListNode()
                level_list = self.lists[level]
                level_list.node.up =  up_list.node
                up_list.node.down = level_list.node
                #insert level_up_node at the end of newly created level
                up_list.node.next = level_up_node
                level_up_node.previous = up_list.node
            #upper level exists, move back find the first element with an up
            #insert new node as it's next
            else:
                junction_node = level_node
                while junction_node.up == None:
                    junction_node = junction_node.previous
                upper_junction = junction_node.up
                upper_junction_next = upper_junction.next
                upper_junction.next = level_up_node
                level_up_node.previous = upper_junction
                level_up_node.next = upper_junction_next
                if upper_junction_next:
                    upper_junction_next.previous = level_up_node
            level_node.up = level_up_node
            level_up_node.down = level_node
            level_node = level_up_node
            level +=1
            flip = random.randint(0,1)

    def delete(self,key):
        found_on_node = self.search(key)
        while found_on_node:
            next_node = found_on_node.next
            found_on_node.previous.next = next_node
            if next_node:
                next_node.previous = found_on_node.previous
            found_on_node = found_on_node.down

    #searches for a given key, returns the node if found else returns None or closest node based on param
    def search(self,key,returnClosestIfNotFound=False):
        found = False
        list_num = len(self.lists)-1
        cur_node = self.lists[list_num].node.next
        prev_node = None
        while not found and list_num>=0 and cur_node:
                while cur_node and cur_node.val <= key:
                    if cur_node.val == key:
                        found = True
                        print found
                        return cur_node
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.next
                if not cur_node:
                    cur_node = prev_node
                if not found and cur_node:
                    if cur_node.val > key:
                        previous = cur_node.previous
                        cur_node = previous.down
                        if not cur_node and returnClosestIfNotFound:
                            print found
                            return previous
                    else:
                        cur_node= cur_node.down
                    list_num-=1
        print found


    def print_all_elems(self,verbose=False):
        print '-------------------------'
        print '-------------------------'
        for j in range(len(self.lists)-1,-1,-1):
            print "List "+str(j)+":"
            skip_list = self.lists[j]
            cur_node = skip_list.node
            i = 0
            while cur_node != None and i < 25:
                if verbose:
                    if cur_node.next and cur_node.previous:
                        sys.stdout.write(str(cur_node.val) + '['+str(cur_node.next.val)+'/'+str(cur_node.previous.val)+'] ')
                    elif cur_node.next:
                        sys.stdout.write(str(cur_node.val) + '['+str(cur_node.next.val)+'/] ')
                    elif cur_node.previous:
                        sys.stdout.write(str(cur_node.val) + '[/'+str(cur_node.previous.val)+'] ')
                    else:
                        sys.stdout.write(str(cur_node.val) + '[] ')
                else:
                    sys.stdout.write(str(cur_node.val)+', ')
                cur_node = cur_node.next
                i += 1
            if i == 25:
                print('...')
            else:
                print
            print '-------------------------'



#Main
def main():
    linked_list = SkipList()
    for i in range(10):
        linked_list.insert((i+1)*5)
        # linked_list.print_all_elems()
    linked_list.print_all_elems()
    linked_list.search(45)
    linked_list.delete(45)
    linked_list.print_all_elems()
    linked_list.search(45)
    linked_list.print_all_elems()
    linked_list.insert(46)
    linked_list.print_all_elems()
    linked_list.insert(7)
    linked_list.print_all_elems()
    linked_list.delete(5)
    linked_list.print_all_elems()


if __name__ == "__main__":
    sys.exit(main())
