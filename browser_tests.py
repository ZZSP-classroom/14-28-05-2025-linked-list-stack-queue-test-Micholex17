import unittest
from browser_history import *

class BrowserTests(unittest.TestCase):
    def test_push(self):
        history = Stack()

        history.push("https://www.google.com/")
        
        self.assertEqual(history.peek(), "https://www.google.com/")

    def test_pop(self):
        history = Stack()

        history.push("https://www.google.com/")
        history.push("https://www.youtube.com/")

        self.assertEqual(history.peek(), "https://www.youtube.com/")

        self.assertEqual(history.pop(), "https://www.youtube.com/")
        self.assertEqual(history.peek(), "https://www.google.com/")

if __name__ == "__main__":
    unittest.main()
