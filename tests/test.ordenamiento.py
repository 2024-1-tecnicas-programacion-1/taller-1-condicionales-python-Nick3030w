import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.ordenamiento import evaluar

class TestOrdenamiento(unittest.TestCase):
    def testNo1(self):
        valor_esperado = "0 1 6 7 "
        valor_actual = evaluar(7, 0, 6, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testNo2(self):
        valor_esperado = "6 7 8 9 "
        valor_actual = evaluar(8, 9, 6, 7)
        self.assertEqual(valor_esperado, valor_actual)
    def testNo3(self):
        valor_esperado = "123 325 685 985 "
        valor_actual = evaluar(325, 685, 985, 123)
        self.assertEqual(valor_esperado, valor_actual)
    def testNo4(self):
        valor_esperado = "1 2 3 4 "
        valor_actual = evaluar(4, 3, 2, 1)
        self.assertEqual(valor_esperado, valor_actual)
    def testNo5(self):
        valor_esperado = "0 2 4 6 "
        valor_actual = evaluar(4, 2, 0, 6)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
