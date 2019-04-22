## think of linked list

class StackWithMax: 
    def __init__(self): 
          
        # main stack  
        self.mainStack = []  
      
        # tack to keep track of 
        # max element  
        self.trackStack = [] 
  
    def push(self, x): 
        self.mainStack.append(x)  
        if (len(self.mainStack) == 1): 
            self.trackStack.append(x)  
            return
  
        # If current element is greater than  
        # the top element of track stack,  
        # append the current element to track  
        # stack otherwise append the element  
        # at top of track stack again into it.  
        if (x > self.trackStack[-1]):  
            self.trackStack.append(x)  
        else: 
            self.trackStack.append(self.trackStack[-1]) 
  
    def getMax(self): 
        return self.trackStack[-1] 
  
    def pop(self): 
        self.mainStack.pop()  
        self.trackStack.pop() 
    
    
b = StackWithMax()
b.push(5)
# b.push(7)
# b.push(10)
b.push(2)
b.pop()


class MaxStack:
    
    def __init__(self):
        self.main_stack = []
        self.track_stack = []

    def push(self, val):
        self.main_stack.append(val)
        if len(self.main_stack) == 1:
            self.track_stack.append(val)
            return
        if val > self.track_stack[-1]:
            self.track_stack.append(val)
        else:
            self.track_stack.append(self.track_stack[-1])

    def pop(self):
        self.main_stack.pop()
        self.track_stack.pop()