class RandomizedSet:

    def __init__(self):
        self.data_map = {} # dictionary, aka map, aka hashtable, aka hashmap
        self.data = [] # list aka array

    def insert(self, val: int) -> bool:

        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)

        # add to the list
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list
        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
