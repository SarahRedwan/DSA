from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.num_count = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        old = self.num_count[number]
        new = old + 1
        
        self.num_count[number] = new
        
        self.freq_count[old] -= 1
        self.freq_count[new] += 1

    def deleteOne(self, number: int) -> None:
        if self.num_count[number] == 0:
            return
        
        old = self.num_count[number]
        new = old - 1
        
        self.num_count[number] = new
        
        self.freq_count[old] -= 1
        self.freq_count[new] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0