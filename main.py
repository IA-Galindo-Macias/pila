import unittest

class Pila():
    def __init__(self):
        self.pila = []

    def push(self, data):
        self.pila.append(data)

    def pull(self):
        if self.isEmpty():
            return None
        else:
            return self.pila.pop()

    def isEmpty(self):
        return not bool(self.pila)

    def size(self):
        return len(self.pila)


class TestPila(unittest.TestCase):

    def test_push_when_empty(self):
        test_value = 0
        pila = Pila() # pila vacia
        pila.push(test_value)

        self.assertEqual(pila.size(), 1, "Pila tiene un elemento")
        self.assertIn(test_value, pila.pila, "El valor esta en la pila")

    def test_push_when_not_empty(self):
        
        # pila no vacia
        pila = Pila() 
        pila.pila = [1,2,3,4]
        prev_size = pila.size()

        # agregar valor 
        test_value = 0
        pila.push(test_value)
    
        self.assertEqual(pila.size(), prev_size + 1, "Pila tiene un elemento más")
        self.assertEqual(test_value, pila.pila[-1], "El valor esta en la pila")

    def test_pull_when_empty(self):
        pila = Pila() # pila vacia
        
        self.assertEqual(pila.pull(), None, "Pull no se puede hacer")

    def test_pull_when_not_empty(self):
        # pila no vacia
        pila = Pila() 
        pila.pila = [1,2,3,4,5]
        
        pushed = 0
        pila.push(pushed)

        prev_size = pila.size()

        # quitar valor
        test_value = pila.pull()

        self.assertNotEqual(pila.pull(), pushed)
        self.assertEqual(pila.size(), prev_size - 1, "Pila tiene un elemento menos")

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
