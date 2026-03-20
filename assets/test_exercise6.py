import unittest
import test_exercise6 

class TestVentas(unittest.TestCase):

    def test_total_ventas(self):
        lista = [
            {"price": 100, "quantity": 5, "customer": "normal", "status": "ok"},
            {"price": 200, "quantity": 10, "customer": "normal", "status": "ok"},
            {"price": 300, "quantity": 10, "customer": "vip", "status": "ok"},
            {"price": 50, "quantity": 2, "customer": "normal", "status": "error"},
        ]

        total = test_exercise6.calcular_total_ventas(lista)
        self.assertEqual(total, 4850)


if __name__ == "__main__":
    unittest.main()