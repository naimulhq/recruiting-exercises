# Naimul Hoque

# Develop Inventory Allocator Class
class InventoryAllocator:
    def __init__(self,warehouse, item, itemAmount):
        self.warehouse = warehouse # String holding the specific department
        self.item = item # List of Strings representing the items in inventory
        self.itemAmount = itemAmount # List of integers representing the amount of a specific item. 

    # This function is in charge of printing the output in the specified format
    def printOutput(inventoryContains):
        # RangeValue holds length of items in specific warehouses needed for shipment, itemList and amountList gets the two sublists within inventoryContains
        rangeValue = 0 
        itemList = []
        amountList = []

        # If there exist a sublist, assign it to itemList and amountList and take note of length of itemList
        if(type(inventoryContains[1]) is list):
            rangeValue = len(inventoryContains[1])
            itemList = inventoryContains[1]
            amountList = inventoryContains[2]
        else:
            rangeValue = 1
            itemList.append(inventoryContains[1])
            amountList.append(inventoryContains[2])

        inventoryString = "{ " + inventoryContains[0] + ": { "
        # Use a for loop to construct remaining portion depending on total items in inventory
        for i in range(rangeValue):
            if(i == rangeValue - 1):
                if(rangeValue == 1):
                    inventoryString = inventoryString + (itemList[0]) + ": " + (amountList[0]) + " } }"
                else:
                    inventoryString = inventoryString + itemList[i] + ": " + amountList[i] + " } }"
            else:
                inventoryString = inventoryString + itemList[i] + ": " + amountList[i] + ", "
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
        if(int(amount) <= int(self.itemAmount[index])):
            enough = True
        return enough

    # This function will check inventory of multiple departments to see if order is possible
    def checkInventory(inventoryList, item, amount):
        i_inventroyAllocator = iter(inventoryList)
        inventoryContains = []   # holds the possible warehouses
        containDept = False # Determines if two different items share same warehouse
        inventoryHas = [False]*len(item) # This will determine if order is complete
        while True:
            try:
                myInventory = next(i_inventroyAllocator) # Iterate through list of inventory allocator objects
                  # Loop through each item
                for i in range(len(item)):
                    # Checks if item is warehouse and gives index
                    containDept = False
                    found, index = myInventory.isItemInInventory(item[i])
                    # If found, check if there is enough of that inventory. Else go to next item
                    if(found == True):
                        enough = myInventory.isEnoughInventory(amount[i], index)
                        # If there is enough, add to inventoryContains List
                        if(enough == True):
                            # Checks if this is first item in List
                            if(len(inventoryContains) == 0):
                                inventoryHas[i] = True # This tells that a specific item order has been met
                                inventoryContains.append([myInventory.warehouse, [item[i]], [amount[i]]])
                            else:
                                # If not, check to see if the list contains same warehouse. If it does. dont add new entry. JUst add item and amount
                                for j in range(len(inventoryContains)):
                                    # If same warehouse, append and signify that item is complete and belong to same warehouse already in list
                                    if(inventoryContains[j][0] == myInventory.warehouse):
                                        containDept = True
                                        inventoryHas[i] = True
                                        inventoryContains[j][1].append(item[i])
                                        inventoryContains[j][2].append(amount[i])
                                # If not true, indicate that item is complete and appened to list
                                if(containDept == False):
                                    inventoryHas[i] = True
                                    inventoryContains.append([myInventory.warehouse, [item[i]], [amount[i]]])
                        # If there is not enough, still add to list. It is possible that it could be split between different warehouses
                        else:
                            # Same process as previous. However, we do not set inventoryHas to true since item is not complete
                            if(len(inventoryContains) == 0):
                                inventoryContains.append([myInventory.warehouse, [item[i]], [myInventory.itemAmount[index]]])
                            else:
                                for j in range(len(inventoryContains)):
                                    if(inventoryContains[j][0] == myInventory.warehouse):
                                        inventoryContains[j][1].append(item[i])
                                        inventoryContains[j][2].append(myInventory.itemAmount[index])
                                    else:
                                        inventoryContains.append([myInventory.warehouse, item[i], myInventory.itemAmount[index]])
                            # This changes the amount in the inventory. This is necessary to determine if split is possible
                            amount[i] = str(int(amount[i]) - int(myInventory.itemAmount[index]))
                # If the order has been completed, break loop to get least amount of warehouses
                if(all(inventoryHas) == True):
                    break
            except StopIteration:
                break
        # If not complete, return empty list
        if(all(inventoryHas) == False):
            return []
        else:
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
        indexValue = secondInput.find("},{", currentIndex) # Checks for specific character to split on
        indexOccurences.append(indexValue)
        inventory.append(secondInput[currentIndex:indexValue]) # Puts the warehouse string into inventory list
        currentIndex = indexValue + 2
    # If len = 0, there exists only one warehouse
    if(len(indexOccurences) == 0):
        inventory = [secondInput]
    else:
        # This adds the last warehouse information before end of string
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
    # For each warehouse, extract the data
    for i in inventory:
        # This portion extracts warehouse name
        nameIndex = i.find("name:") + 5
        endIndex = i.find(",",nameIndex)
        warehouseName = i[nameIndex:endIndex]
        # This portion ges the inventory items and amount content within string
        item, amount = getInventoryWithinString(i)
        # Use the retrieved information to create an object and store in list.
        myInventoryAllocator = InventoryAllocator(warehouseName, item, amount)
        inventoryAllocatorList.append(myInventoryAllocator)
    return inventoryAllocatorList


############################################################################ Main Program ###############################################################################################
def main(userInput):
    firstInput, secondInput = obtainStringsInput(userInput) # Calls function which returns both inputs seperated into two strings
    itemNames, itemTotal = decodeFirstString(firstInput) # Calls function which returns a list of item being ordered and total number of the specific item that was ordered
    inventory = seperateSecondInput(secondInput)  # Multiple inventories can be inputted. This function call seperates each inventory
    inventoryAllocatorList = extractInventoryData(inventory) # This function call extract data from each inventory and returns it as a list of InventoryAllocator object
    inventoryContains = InventoryAllocator.checkInventory(inventoryAllocatorList, itemNames, itemTotal) # Returns which warehouses are needed to complete shipment
    # If there is no warehouse which can complete shipment, [] is returned.
    inventoryString = []
    if(len(inventoryContains) == 0):
        return "[]"
    # Use a for loop to construct the list of different warehouses which are necessary to completing shipment
    for i in range(len(inventoryContains)):
        inventoryString.append(InventoryAllocator.printOutput(inventoryContains[i]))

    # The bottom loop will reconstruct the string to produce correct format for output
    myString = ""
    for i in range(len(inventoryString)):
        if((len(inventoryString) > 0 and i == 0) or (len(inventoryString) == i-1)):
            myString = myString + inventoryString[i]
        else:
            myString = myString + ", " + inventoryString[i]

    return myString