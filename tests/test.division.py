import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionnoExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionExacta(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 4\n" \
                         "Residuo: 0"
        valor_actual = evaluar(8, 2)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivisionnoExacta1(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 1\n" \
                         "Residuo: 2"
        valor_actual = evaluar(9, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivisionExacta2(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 10\n" \
                         "Residuo: 0"
        valor_actual = evaluar(20, 2)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivisionnoExacta2(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 78\n" \
                         "Residuo: 4"
        valor_actual = evaluar(550, 7)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
