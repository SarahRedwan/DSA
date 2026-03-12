class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.front=0
        self.rare=-1
        self.arr=[0]*k
        self.size=0
        

    def insertFront(self, value: int) -> bool:
        if self.size==self.k:
            return False
        self.front=(self.front-1+self.k)%self.k
        self.arr[self.front]=value
        self.size+=1

        return True
    def insertLast(self, value: int) -> bool:
        if self.size==self.k:
            return False
        self.rare=(self.rare+1)%self.k
        self.arr[self.rare]=value
        self.size+=1
        return True
        

    def deleteFront(self) -> bool:
        if self.size==0:
            return False
        self.front=(self.front+1)%self.k
        self.size-=1
        return True
        

    def deleteLast(self) -> bool:
        if self.size==0:
            return False
        self.rare=(self.rare-1+self.k)%self.k
        self.size-=1
        return True
        

    def getFront(self) -> int:
        if self.size==0:
            return -1
        return self.arr[self.front]
        

    def getRear(self) -> int:
        if self.size==0:
            return -1
        return self.arr[self.rare]
        
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()