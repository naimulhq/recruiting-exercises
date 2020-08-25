# Naimul Hoque


# Develop Inventory Allocator Class
class InventoryAllocator:
    def __init__(self):
        self.department = department # String holding the specific department
        self.item = [] # List of Strings representing the items in inventory
        self.itemAmount = [] # List of integers representing the amount of a specific item. 

# Main Program

# Get user input. Necessary for testing purposes.
# { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
userInput = input("Enter shipment information: ") # Gathers user input

# After recieving input, we need to be able to break it down to apply the information to the program

# First, find the indexes necessary to split the two inputs.
firstStart = userInput.find("{")
firstStop = userInput.find("}")
secondStart = userInput.find("[")
secondStop = userInput.find("]")

# Second, split the inputs to two different strings
firstInput = (userInput[firstStart:firstStop+1]).replace(" ","")
secondInput = (userInput[secondStart:secondStop+1]).replace(" ", "")

# Third, since we have seperated input to two strings, we can handle each input seperatly.
# It would be best to handle the second string which holds information regarding warehouse name and inventory amounts
print(firstInput)







