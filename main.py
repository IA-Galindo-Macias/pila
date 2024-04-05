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

pila = Pila()
pila.push(56)
