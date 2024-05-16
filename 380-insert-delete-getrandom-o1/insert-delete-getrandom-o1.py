class RandomizedSet:

    def __init__(self):
        self.our_set = set()
        self.keys = []
        self.idxs = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.our_set:
            self.our_set.add(val)
            self.keys.append(val)
            self.idxs[val] = self.count
            self.count += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.our_set:
            self.our_set.remove(val)
            self.idxs[self.keys[-1]] = self.idxs[val]
            self.keys[self.idxs[val]], self.keys[-1] = self.keys[-1], self.keys[self.idxs[val]]
            self.keys.pop()
            self.idxs.pop(val)
            self.count -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        index = random.randint(0, self.count - 1)
        return self.keys[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()