import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = ("Usted tiene ", 24, " años")
        valor_actual = evaluar(1, 1, 2000)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2005julio1(self):
        valor_esperado = ('Usted tiene ', 18, ' años')
        valor_actual = evaluar(2, 7, 2005)
        self.assertEqual(valor_esperado, valor_actual)
    def test2005mayo4(self):
        valor_esperado = ('Usted tiene ', 18, ' años')
        valor_actual = evaluar(4, 5, 2005)
        self.assertEqual(valor_esperado, valor_actual)
    def test1969febrero1(self):
        valor_esperado = ('Usted tiene ', 55, ' años')
        valor_actual = evaluar(1, 2, 1969)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
