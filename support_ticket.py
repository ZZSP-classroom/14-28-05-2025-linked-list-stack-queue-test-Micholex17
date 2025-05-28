class IncomingTickets:
    def __init__(self):
        self.__l = []
    
    def enqueue(self, value):
        self.__l.append(value)
    
    def dequeue(self):
        return self.__l.pop(0)

    def peek(self):
        return self.__l[0]
    
class ProcessedTickets:
    def __init__(self):
        self.__l = []
    
    def push(self, value):
        self.__l.append(value)
    
    def pop(self):
        return self.__l.pop()
    
    def peek(self):
        return self.__l[len(self.__l) - 1]

class Ticket:
    def __init__(self, ticket_id, issue_description) -> None:
        self.ticket_id = ticket_id
        self.issue_description = issue_description
