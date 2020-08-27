# Naimul Hoque



# Develop Inventory Allocator Class
class InventoryAllocator:
    def __init__(self,department, item, itemAmount):
        self.department = department # String holding the specific department
        self.item = item # List of Strings representing the items in inventory
        self.itemAmount = itemAmount # List of integers representing the amount of a specific item. 

    # This function is in charge of printing the output in the specified format
    def printOutput(inventoryContains):
        # Construct the initial portion of the string.
        rangeValue = 0
        if(type(inventoryContains[1]) is list):
            rangeValue = len(inventoryContains)
        else:
            rangeValue = 1

        inventoryString = "{ " + inventoryContains[0] + ": { "
        # Use a for loop to construct remaining portion depending on total items in inventory
        for i in range(rangeValue):
            if(i == rangeValue - 1):
                if(rangeValue == 1):
                    inventoryString = inventoryString + (inventoryContains[1]) + ": " + (inventoryContains[2]) + " } }"
                else:
                    inventoryString = inventoryString + (inventoryContains[1])[i] + ": " + (inventoryContains[2])[i] + " } }"
            else:
                inventoryString = inventoryString + (inventoryContains[1])[i] + ": " + (inventoryContains[2])[i] + ", "
        return inventoryString

    # This function checks first to see if item is in inventory
    def isItemInInventory(self, item):
        found = False
        index = -1
        for i in range(len(self.item)):
            if(item == self.item[i]):
                found = True
                index = i
        return found, index

    # This function checks to see if there is enough inventory for order
    def isEnoughInventory(self, amount, index):
        enough = False
        if(amount <= self.itemAmount[index]):
            enough = True
        return enough



    # This function will check inventory of multiple departments to see if order is possible
    def checkInventory(inventoryList, item, amount):
        i_inventroyAllocator = iter(inventoryList)
        inventoryContains = []
        while True:
            try:
                myInventory = next(i_inventroyAllocator)
                for i in range(len(item)):
                    found, index = myInventory.isItemInInventory(item[i])
                    if(found == True):
                        enough = myInventory.isEnoughInventory(amount[i], index)
                        if(enough == True):
                            inventoryContains.append([myInventory.department, item[i], amount[i]])
                            break
                
            except StopIteration:
                break
        return inventoryContains






# Since the user will enter two different inputs, it would be easy to work with data by seperating into two different strings. This function fulfills this purpose.
def obtainStringsInput(userInput):
    # First, find the indexes necessary to split the two inputs.
    firstStart = userInput.find("{")
    firstStop = userInput.find("}")
    secondStart = userInput.find("[")
    secondStop = userInput.find("]")

    # Second, split the inputs to two different strings
    firstInput = (userInput[firstStart+1:firstStop+1]).replace(" ","")
    secondInput = (userInput[secondStart+1:secondStop+1]).replace(" ", "")

    return firstInput,secondInput # Return the seperated strings

def decodeFirstString(firstInput):
    # Iterate through each character in the string.
    item = [] # Holds the item that is being ordered
    value = [] # Holds the total number of the specific item being ordered

    # Using the sliding window method to extract the data from the string
    initialIndex = 0 
    currentIndex = 0
    while(firstInput[currentIndex] != '}'): # If a closing brace occurs, this indicates end of first string
        if(firstInput[currentIndex] == ':'): # If a colon occurs, indicates end of item name and beginning of total number of ordered item
            item.append(firstInput[initialIndex:currentIndex]) 
            initialIndex = currentIndex + 1 # We want initialIndex to start after colon
            currentIndex += 1 # We want currentIndex to start after colon
        elif(firstInput[currentIndex] == ","): # If a comma occurs, this indicates that there are more items being ordered.
            value.append(firstInput[initialIndex:currentIndex])
            initialIndex = currentIndex + 1 # We want initialIndex to start after comma
            currentIndex += 1 # We want currentIndex to start after comma
        else:
            currentIndex += 1 # If none of the above occurs, increase currentIndex by 1

    value.append(firstInput[initialIndex:currentIndex]) # This ensures last value is obtained since the loop is exited after a closing brace
    return item,value

# This function is designed to extract the second input which contains the warehouse and inventory
def seperateSecondInput(secondInput):
    indexOccurences = []
    inventory = []
    currentIndex = 0
    # If there exist more than one warehouse, code will be able to seperate each warehouse and store in inventory
    while(secondInput.find("},{", currentIndex) != -1):
        indexValue = secondInput.find("},{") 
        indexOccurences.append(indexValue)
        currentIndex = indexValue + 2
        inventory.append(secondInput[:indexValue])
    if(len(indexOccurences) == 0):
        inventory = [secondInput]
    else:
        inventory.append(secondInput[indexOccurences[len(indexOccurences)-1]+2:])

    return inventory

# Retrieves the inventory portion of the string
def getInventoryWithinString(inventoryString):

    inventoryIndex = inventoryString.find("inventory:") + 11 # Retrieves the beginning index and add by 11 to get beginning of inventory
    endIndex = inventoryString.find("}", inventoryIndex) # Get index of where inventory ends
    inventoryString = inventoryString[inventoryIndex:endIndex] # Get string which contains all the inventory
    # Item will hold item and value will hold amount of specific item
    item = []
    value = []
    # Use a while loop to extract the item name and amount from string
    initialIndex = 0 
    currentIndex = 0
    while(currentIndex != len(inventoryString)): # If a closing brace occurs, this indicates end of first string
        if(inventoryString[currentIndex] == ':'): # If a colon occurs, indicates end of item name and beginning of total number of ordered item
            item.append(inventoryString[initialIndex:currentIndex]) 
            initialIndex = currentIndex + 1 # We want initialIndex to start after colon
            currentIndex += 1 # We want currentIndex to start after colon
        elif(inventoryString[currentIndex] == ","): # If a comma occurs, this indicates that there are more items being ordered.
            value.append(inventoryString[initialIndex:currentIndex])
            initialIndex = currentIndex + 1 # We want initialIndex to start after comma
            currentIndex += 1 # We want currentIndex to start after comma
        else:
            currentIndex += 1 # If none of the above occurs, increase currentIndex by 1

    value.append(inventoryString[initialIndex:currentIndex]) # This ensures last value is obtained since the loop is exited after a closing brace

    return item, value


def extractInventoryData(inventory):
    # This for loop will extract all the data from second input and create InventoryAllocator Objects
    inventoryAllocatorList = [] # This list will hold all InventoryAllocator Objects
    for i in inventory:
        nameIndex = i.find("name:") + 5
        endIndex = i.find(",",nameIndex)
        warehouseName = i[nameIndex:endIndex]
        item, amount = getInventoryWithinString(i)
        myInventoryAllocator = InventoryAllocator(warehouseName, item, amount)
        inventoryAllocatorList.append(myInventoryAllocator)

    return inventoryAllocatorList



############################################################################ Main Program ###############################################################################################
# Get user input. Necessary for testing purposes.
# First  Total Input { apple: 1}, [{ name: owd, inventory: { apple: 1} }]
# Second Total Input { apple: 10 }, [{ name: owd, inventory: { apple: 5, banana: 2 } }, { name: dm, inventory: { apple: 5 }}]
def main(userInput):
    #userInput = input("Enter shipment information: ") # Gathers user input
    firstInput, secondInput = obtainStringsInput(userInput) # Calls function which returns both inputs seperated into two strings
    itemNames, itemTotal = decodeFirstString(firstInput) # Calls function which returns a list of item being ordered and total number of the specific item that was ordered
    inventory = seperateSecondInput(secondInput)  # Second Input can have multiple parts. This is seperate to a list of strings
    inventoryAllocatorList = extractInventoryData(inventory) 
    inventoryContains = InventoryAllocator.checkInventory(inventoryAllocatorList, itemNames, itemTotal)
    if(len(inventoryContains) == 0):
        return "[]"
    for i in range(len(inventoryContains)):
        inventoryString = InventoryAllocator.printOutput(inventoryContains[i])
    return inventoryString


