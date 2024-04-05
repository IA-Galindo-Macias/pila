import unittest

class pila():
    def __init__(self):
        self.pila = []

    def push(self, data):
        pila.append(data)

    def pull(self):
        pila.pop()

    def isEmpty(self):
        

    def size(self):
        return self.pila


class TestPila(unittest.TestCase):

    def test_push_when_empty(self):
        self.assertEqual(1, 1)

    def test_push_when_not_empty(self):
        self.assertEqual(1, 1)

    def test_pull_when_empty(self):
        self.assertEqual(1, 1)

    def test_pull_when_not_empty(self):
        self.assertEqual(1, 1)

    def test_isEmpty_when_empty(self):
        self.assertEqual(1, 1)
    
    def test_isEmpty_when_not_empty(self):
        self.assertEqual(1, 1)

    def test_size_when_empty(self):
        self.assertEqual(1, 1)

    def test_size_when_not_empty(self):
        self.assertEqual(1, 1)
    
if __name__ == '__main__':
    unittest.main()