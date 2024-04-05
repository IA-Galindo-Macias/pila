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

        # agregar valor 
        test_value = 0
        pila.push(test_value)
    
        self.assertEqual(pila.size(), 5, "Pila tiene un elemento")
        self.assertIn(test_value, pila.pila, "El valor esta en la pila")

    def test_pull_when_empty(self):
        pila = Pila() # pila vacia
        pila.pull()

        self.assertEqual(pila.size(), 0, "Pila esta vacía")
        

    def test_pull_when_not_empty(self):
        # pila no vacia
        pila = Pila() 
        pila.pila = [1,2,3,4,5]

        # quitar valor
        test_value = pila.pull()

        self.assertEqual(pila.size(), 4, "Pila tiene un elemento")
        self.assertNotIn(test_value, pila.pila, "El valor ya no está en la pila")

    def test_isEmpty_when_empty(self):
        pila = Pila()

        self.assertTrue(pila.isEmpty(), "La pila NO esta vacía")

    
    def test_isEmpty_when_not_empty(self):
        pila = Pila()
        pila.push(1)
        pila.push(2)
        pila.push(3)

        self.assertFalse(pila.isEmpty(), "La pila esta vacía")


    def test_size_when_empty(self):
        pila = Pila()
        pila.pila = []
        self.assertEqual(pila.size(), 0, "Pila vacia")

    def test_size_when_not_empty(self):
        pila = Pila()
        pila.pila = [1,2,3,4]
        self.assertEqual(pila.size(), 4, "Pila no vacia")
        self.assertEqual(1, 1)
    
if __name__ == '__main__':
    unittest.main()