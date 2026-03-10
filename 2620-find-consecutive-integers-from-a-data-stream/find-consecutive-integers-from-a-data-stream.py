class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.queue = deque()
        self.num_of = 0
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if len(self.queue) > self.k:
            if self.queue.popleft() == self.val:
                self.num_of -= 1
        if num == self.val:
            self.num_of += 1
        if len(self.queue) == self.k:
            if self.num_of == self.k:
                return True
            else:
                return False
        else:
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)