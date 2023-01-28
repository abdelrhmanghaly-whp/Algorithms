class circularQueue:

    def __init__(self):
        self.queue= list()
        self.front=0
        self.rear=0
        self.maxSize= 5 # whatever you want, make your pick, we can even make it as an input

    def calculateSize(self):
        if self.rear>=self.front:
            return self.rear - self.front
        return (self.maxSize - (self.front - self.rear))

    def addElement(self,values):
        if self.calculateSize()==self.maxSize-1:
            return "The Queue is full"
        self.queue.append(values)
        self.rear+=1 % self.maxSize
        return str(values)+" is added to the Queue " 

    def removeElement(self):
        if self.calculateSize()==0:
            return "The Queue is empty"
        values=self.queue[self.front]
        self.front+=1 % self.maxSize
        return str(values)+" is removed from the Queue "


ex = circularQueue()
print(ex.calculateSize())
print(ex.addElement(1))
print(ex.addElement(2))
print(ex.addElement(3))
print(ex.addElement(4))
print(ex.addElement(5))
print(ex.addElement(6))
print(ex.calculateSize())

print(ex.removeElement())
print(ex.removeElement())
print(ex.removeElement())
print(ex.removeElement())
print(ex.removeElement())
