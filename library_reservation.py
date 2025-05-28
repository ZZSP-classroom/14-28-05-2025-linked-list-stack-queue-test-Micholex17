class Queue:
    def __init__(self):
        self.__l = []
    
    def enqueue(self, value):
        self.__l.append(value)
    
    def dequeue(self):
        return self.__l.pop(0)
    
    def peek(self):
        return self.__l[0]

class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title
