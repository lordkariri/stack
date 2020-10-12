class Stack:
    def __init__(self, l):
        self.stack = [None for x in range (l)]
        self.pointer = 0
    def push(self, value):
        self.stack[self.pointer] = value
        self.pointer +=1
        

    def pop(self):
        del self.stack[self.pointer-1]
        self.pointer -=1
        

    def peak(self):
        return self.stack[self.pointer-1]

     
s = Stack(5)
s.push('dog')
s.push('cat')
s.push('mouse')
print (s.peak())
print (s.pop())
print (s.peak())