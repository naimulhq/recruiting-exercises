import unittest
import os
from InventoryAllocator import main
class testInventoryAllocator(unittest.TestCase):
    def test_perfectCaseOneItemOneWarehouse(self):
        print("Test 1")
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]")
        self.assertEqual(result, "{ owd: { apple: 1 } }" )
    def test_oneWarehouseNotEnoughInventory(self):
        print("Test 2")
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]")
        self.assertEqual(result,"[]")
    def test_oneItemTwoWarehouseSplit(self):
        print("Test 3")
        result = main("{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]")
        self.assertEqual(result,"[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]")
    def test_perfectTwoItemOneWarehouse(self):
        print("Test 4")
        result = main("{ apple: 1, banana: 2 }, [{ name: owd, inventory: { apple: 1, banana: 2 } }]")
        self.assertEqual(result,"{ owd: { apple: 1, banana: 2 } }")


if __name__ == '__main__':
    unittest.main()
