import random

class RandomizedSet:

    def __init__(self):
        self.data_map = {}   
        self.data = []       
    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False

        idx = self.data_map[val]
        last_val = self.data[-1]

        self.data[idx] = last_val
        self.data_map[last_val] = idx

        self.data.pop()
        del self.data_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)