# Design a data structure that supports all following operations in average O(1) time.

 

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

class RandomizedSet:

    def __init__(self):
        self.key_index_map = dict()
        self.data = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.key_index_map: return False
        
        self.key_index_map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.key_index_map: return False
        
        remove_index = self.key_index_map[val]
        last_index = len(self.data) - 1
        
        self.key_index_map[self.data[last_index]] = remove_index
        self.data[remove_index], self.data[last_index] = self.data[last_index], self.data[remove_index]
        self.data.pop()
        del self.key_index_map[val]
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)