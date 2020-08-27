import unittest
import os
from InventoryAllocator import main
class testInventoryAllocator(unittest.TestCase):
    def test_perfectCaseOneItemOneWarehouse(self):
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]")
        self.assertEqual(result, "{ owd: { apple: 1 } }" )
    def test_oneWarehouseNotEnoughInventory(self):
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]")
        self.assertEqual(result,"[]")

if __name__ == '__main__':
    unittest.main()
