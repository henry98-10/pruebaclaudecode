import unittest

from saludo import main, saludar


class TestSaludo(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(saludar("Henry"), "¡Hola, Henry!")

    def test_saludar_recorta_espacios(self):
        self.assertEqual(saludar("  Ana "), "¡Hola, Ana!")

    def test_saludar_vacio(self):
        with self.assertRaises(ValueError):
            saludar("   ")

    def test_main_sin_argumentos(self):
        self.assertEqual(main(["saludo.py"]), 1)

    def test_main_ok(self):
        self.assertEqual(main(["saludo.py", "Henry"]), 0)


if __name__ == "__main__":
    unittest.main()
