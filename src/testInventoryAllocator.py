import unittest
import os
from InventoryAllocator import main
class testInventoryAllocator(unittest.TestCase):
    def test_perfectCaseOneItemOneWarehouse(self): # Check single warehouse for one item. Perfect Match
        print("Test 1")
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]")
        self.assertEqual(result, "{ owd: { apple: 1 } }" )
    def test_oneWarehouseNotEnoughInventory(self): # Check single warehouse for one item. Not enough inventory
        print("Test 2")
        result = main("{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]")
        self.assertEqual(result,"[]")
    def test_oneItemTwoWarehouseSplit(self): # Checks for one item. Split necessary between two warehouses successful
        print("Test 3")
        result = main("{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]")
        self.assertEqual(result,"{ owd: { apple: 5 } }, { dm: { apple: 5 } }")
    def test_perfectTwoItemOneWarehouse(self): # Checks for two items in one warehouse. Perfect amount
        print("Test 4")
        result = main("{ apple: 1, banana: 2 }, [{ name: owd, inventory: { apple: 1, banana: 2 } }]")
        self.assertEqual(result,"{ owd: { apple: 1, banana: 2 } }")
    def test_oneItemTwoWarehouse(self): # Checks for one item between two warehouses. 
        print("Test 5")
        result = main("{ apple: 2 }, [{ name: owd, inventory: { apple: 2 } }, { name: dm, inventory: { banana: 3 }}]")
        self.assertEqual(result,"{ owd: { apple: 2 } }" )
    def test_oneItemTwoWarehouse2(self): # Checks for one item between two warehouse. 
        print("Test 6")
        result = main("{ banana: 3 }, [{ name: owd, inventory: { apple: 2 } }, { name: dm, inventory: { banana: 3 }}]")
        self.assertEqual(result,"{ dm: { banana: 3 } }" )
    def test_oneItemNotInEitherWarehouse(self): # Checks for one item between two warehouse. Not enough inventory
        print("Test 7")
        result = main("{ orange: 3 }, [{ name: owd, inventory: { apple: 2 } }, { name: dm, inventory: { banana: 3 }}]")
        self.assertEqual(result,"[]")
    def test_twoItemOneEachWarehouse(self): # Checks for two items, one in each warehouse success
        print("Test 8")
        result = main("{ apple: 1, banana: 2 }, [{ name: owd, inventory: { apple: 1 } }, { name: dm, inventory: { banana: 2 } }]")
        self.assertEqual(result,"{ owd: { apple: 1 } }, { dm: { banana: 2 } }")
    def test_oneItemTwoWarehouse3(self): # Checks for one item between two warehouses. Returns cheapest
        print("Test 9")
        result = main("{ apple: 2 }, [{ name: owd, inventory: { apple: 2 } }, { name: dm, inventory: { apple: 2 }}]")
        self.assertEqual(result,"{ owd: { apple: 2 } }" )
    def test_twoItemNotEnoughInventoryTwoWarehouse(self): # Checks for two items between two warehouses. Not enough inventory
        print("Test 10")
        result = main("{ apple: 1, banana: 2 }, [{ name: owd, inventory: { apple: 1 } }, { name: dm, inventory: { banana: 0 } }]")
        self.assertEqual(result,"[]")
    def test_threeItemTwoWarehouse(self): # Checks for three items between two warehouses. Success
        print("Test 11")
        result = main("{ apple: 1, banana: 2, orange: 5 }, [{ name: owd, inventory: { apple: 1, orange: 7 } }, { name: dm, inventory: { banana: 2 } }]")
        self.assertEqual(result,"{ owd: { apple: 1, orange: 5 } }, { dm: { banana: 2 } }")
    def test_threeItemTwoWarehouseNotEnough(self): # Checks for three items between two warehouses. Not successful
        print("Test 12")
        result = main("{ apple: 1, banana: 2, orange: 5 }, [{ name: owd, inventory: { apple: 1, orange: 3 } }, { name: dm, inventory: { banana: 2 } }]")
        self.assertEqual(result,"[]")
    def test_twoItemTwoWarehouseSplit(self): # Checks for two items between two warehouses. Need two warehouses to complete order
        print("Test 13")
        result = main("{ apple: 5, banana: 7}, [{ name: owd, inventory: { apple: 5, banana: 3, orange: 3 } }, { name: dm, inventory: { banana: 4 } }]")
        self.assertEqual(result,"{ owd: { apple: 5, banana: 3 } }, { dm: { banana: 4 } }")
    def test_twoItemTwoWarehouseSplitNotEnough(self): # Checks for two items between two warehouses. Even with split, not enough inventory
        print("Test 14")
        result = main("{ apple: 5, banana: 7}, [{ name: owd, inventory: { apple: 5, banana: 3, orange: 3 } }, { name: dm, inventory: { banana: 3 } }]")
        self.assertEqual(result,"[]")
    def test_complexTest1(self): # Checks for 5 items between three warehouses. Need all three warehouse to complete shipment
        print("Test 15")
        result = main("{ apple: 5, banana: 7, orange:5, pomegranate: 3, mango: 2}, [{ name: owd, inventory: { apple: 5, banana: 3, orange: 3 } }, { name: dm, inventory: { banana: 4, orange: 2 } }, { name: ic, inventory: { pomegranate: 3, mango: 2 } }]")
        self.assertEqual(result,"{ owd: { apple: 5, banana: 3, orange: 3 } }, { dm: { banana: 4, orange: 2 } }, { ic: { pomegranate: 3, mango: 2 } }")
    def test_complexTest2(self): # Checks for 5 items between three warehouses. Only first two warehouses needed to complete shipment
        print("Test 16")
        result = main("{ apple: 5, banana: 7, orange:5, pomegranate: 3, mango: 2}, [{ name: owd, inventory: { apple: 5, banana: 3, orange: 3 } }, { name: dm, inventory: { banana: 4, orange: 2, pomegranate: 3, mango: 2 } }, { name: ic, inventory: { pomegranate: 3, mango: 2 } }]")
        self.assertEqual(result, "{ owd: { apple: 5, banana: 3, orange: 3 } }, { dm: { banana: 4, orange: 2, pomegranate: 3, mango: 2 } }")
    def test_complexTest3(self):
        print("Test 17")
        result = main("{ apple: 5, orange: 3}, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { bread: 5 } }, { name: ic, inventory: { orange: 3 } }]")
        self.assertEqual(result, "{ owd: { apple: 5 } }, { ic: { orange: 3 } }")
if __name__ == '__main__':
    unittest.main()