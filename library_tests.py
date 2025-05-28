import unittest
from library_reservation import *

class LibraryTests(unittest.TestCase):
    def test_enqueue_peek(self):
        reservations = Queue()
        reservations.enqueue(Reservation("John Pork", "1984"))

        self.assertEqual(reservations.peek().user_name, "John Pork")
        self.assertEqual(reservations.peek().book_title, "1984")

        reservations.enqueue(Reservation("Jane Doe", "Witcher"))

        self.assertEqual(reservations.peek().user_name, "John Pork")
        self.assertEqual(reservations.peek().book_title, "1984")

    def test_dequeue_peek(self):
        reservations = Queue()

        reservations.enqueue(Reservation("John Doe", "Harry Potter"))
        reservations.enqueue(Reservation("Tomasz Problem", "Chemia Nowej Ery"))

        self.assertEqual(reservations.peek().user_name, "John Doe")
        self.assertEqual(reservations.peek().book_title, "Harry Potter")

        dequeued = reservations.dequeue()

        self.assertEqual(dequeued.user_name, "John Doe")
        self.assertEqual(dequeued.book_title, "Harry Potter")

        self.assertEqual(reservations.peek().user_name, "Tomasz Problem")
        self.assertEqual(reservations.peek().book_title, "Chemia Nowej Ery")

if __name__ == "__main__":
    unittest.main()
