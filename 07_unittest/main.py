import unittest

# Funções para serem testadas
def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrai(a, b):
    """Retorna a subtração de a por b."""
    return a - b

# Testes usando unittest
class TestMathFunctions(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)
        self.assertEqual(subtrai(0, 1), -1)
        self.assertEqual(subtrai(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
