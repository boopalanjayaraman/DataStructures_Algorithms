# ordered dictionary preserves the order of items in which they were inserted
# To know the least accessed item, we can remove the item and re-add it whenever it is accessed
# In that way, even unaccessed items will be ordered in the least-used fashion
from collections import OrderedDict

class LRU_cache(object):

    def __init__(self, capacity = 10):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache.keys():
            #update the existing order since the item is accessed
            self.update_existing_order(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache.keys():
            #update the existing order since the item is accessed
            self.cache.pop(key)
            self.cache[key] = value
        else:    
            #check if the dictionary has reached its limit, and if yes, remove the last accessed (first added) item
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            
            self.cache[key] = value
        

    def update_existing_order(self, key):
        # since the item already exists, we need to re-insert the item into the cache
        # a redundant step to achieve LRU functionality
        value = self.cache.pop(key, -1)
        if (value != -1):
            self.cache[key] = value
        
    def __str__(self):
        return str(self.cache)

if __name__ == '__main__':
    # test cases
    our_cache = LRU_cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache) #prints whole cache

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    print(our_cache) #prints whole cache, without 3

    #additional test cases
    our_cache.get(2)
    our_cache.get(2)
    our_cache.get(2)
    our_cache.get(2)
    our_cache.get(2)
    our_cache.get(2)

    #does not remove any item and cache is intact, except the order. Item 2 has been shifted to the last (latest) in order
    print(our_cache)