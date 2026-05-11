import unittest
from stack import Stack


class StackTest(unittest.TestCase):

    def test_push_pop(self):
        s = Stack()

        s.push(10)
        s.push(20)

        self.assertEqual(s.peek(), 20)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)

    def test_empty(self):
        s = Stack()
        self.assertTrue(s.empty())


if __name__ == "__main__":
    unittest.main()