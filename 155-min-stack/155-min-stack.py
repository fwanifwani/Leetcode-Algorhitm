class MinStack(object):
    #
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, x):
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
        
    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minStack[-1]:
            self.minStack.pop()  
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()