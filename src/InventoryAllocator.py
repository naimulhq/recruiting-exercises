# Naimul Hoque


# Develop Inventory Allocator Class
class InventoryAllocator:
    def __init__(self):
        self.department = department # String holding the specific department
        self.item = [] # List of Strings representing the items in inventory
        self.itemAmount = [] # List of integers representing the amount of a specific item. 


# Since the user will enter two different inputs, it would be easy to work with data by seperating into two different strings. This function fulfills this purpose.
def obtainStringsInput(userInput):
    # First, find the indexes necessary to split the two inputs.
    firstStart = userInput.find("{")
    firstStop = userInput.find("}")
    secondStart = userInput.find("[")
    secondStop = userInput.find("]")

    # Second, split the inputs to two different strings
    firstInput = (userInput[firstStart+1:firstStop+1]).replace(" ","")
    secondInput = (userInput[secondStart:secondStop+1]).replace(" ", "")

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

# Main Program
# Get user input. Necessary for testing purposes.
# { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
userInput = input("Enter shipment information: ") # Gathers user input
firstInput, secondInput = obtainStringsInput(userInput) # Calls function which returns both inputs seperated into two strings
itemNames, itemTotal = decodeFirstString(firstInput) # Calls function which returns a list of item being ordered and total number of the specific item that was ordered
print(itemNames)
print(itemTotal)






