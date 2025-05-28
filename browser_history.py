class Stack:
    def __init__(self):
        self.__l = []
    
    def push(self, value):
        self.__l.append(value)
    
    def pop(self):
        return self.__l.pop()
    
    def peek(self):
        return self.__l[len(self.__l) - 1]
