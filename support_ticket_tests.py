import unittest
from support_ticket import *

class SupportTicketTests(unittest.TestCase):
    def test_enqueue(self):
        incoming = IncomingTickets()

        incoming.enqueue(Ticket("123", "PC no work"))

        self.assertEqual(incoming.peek().ticket_id, "123")
        self.assertEqual(incoming.peek().issue_description, "PC no work")
    
    def test_dequeue_process(self):
        incoming = IncomingTickets()
        processed = ProcessedTickets()

        incoming.enqueue(Ticket("123", "PC no work"))

        self.assertEqual(incoming.peek().ticket_id, "123")
        self.assertEqual(incoming.peek().issue_description, "PC no work")

        processed.push(incoming.dequeue())

        self.assertEqual(processed.peek().ticket_id, "123")
        self.assertEqual(processed.peek().issue_description, "PC no work")

    def test_pop(self):
        processed = ProcessedTickets()

        processed.push(Ticket("123", "PC no work"))
        processed.push(Ticket("321", "Wifi no work"))

        self.assertEqual(processed.peek().ticket_id, "321")
        self.assertEqual(processed.peek().issue_description, "Wifi no work")

        popped = processed.pop()

        self.assertEqual(popped.ticket_id, "321")
        self.assertEqual(popped.issue_description, "Wifi no work")

        self.assertEqual(processed.peek().ticket_id, "123")
        self.assertEqual(processed.peek().issue_description, "PC no work")

if __name__ == "__main__":
    unittest.main()
