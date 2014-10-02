import sys


class Entry:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.before = None
        self.after = None


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Entry('head_key','head_val')
        self.head.after = self.head
        self.head.before = self.head
        self.dict = {}
        self.size = 0


    # @return an integer
    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            exist = self.dict[key]
            # Make it's neighbours join hands
            before = exist.before
            after = exist.after
            before.after = after
            after.before = before
            #Move it to after head
            after = self.head.after
            after.before = exist
            exist.before = self.head
            exist.after = after
            self.head.after = exist
            return exist.val


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        entry = Entry(key, value)
        if self.size + 1 > self.capacity and key not in self.dict:
            self.remove_eldest()
        self.make_entry(entry)


    def make_entry(self, entry):
        if entry.key in self.dict:
            exist = self.dict[entry.key]
            before = exist.before
            after = exist.after
            before.after = after
            after.before = before
            self.size -= 1
        self.dict[entry.key] = entry
        after = self.head.after
        after.before = entry
        entry.before = self.head
        entry.after = after
        self.head.after = entry
        self.size += 1

    def remove_eldest(self):
        eldest = self.head.before
        before = eldest.before
        after = eldest.after
        before.after = after
        after.before = before
        del self.dict[eldest.key]
        self.size -= 1


def main():
    cache = LRUCache(3)
    cache.set(1, 1)
    cache.set(2, 2)
    print cache.get(2)
    print cache.get(4)
    cache.set(3, 3)
    cache.set(4, 4)
    print cache.get(4)
    print cache.get(1)
    cache.set(4, 9)
    print cache.get(3)

    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(2, 2)
    print cache.get(2)
    cache.set(1, 1)
    cache.set(4, 1)
    print cache.get(2)



if __name__ == "__main__":
    sys.exit(main())