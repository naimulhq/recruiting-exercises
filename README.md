# Inventory Allocator Exercise by Naimul Hoque
This program implements an Inventory Allocator class to handle an order given by the customer. The program takes a string as an input where one portion of the string represents the customer order and the other portion represents the possible warehouses that could be used to make the necessary shipment.

An example of the input and output is shown:

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[{ owd: { apple: 1 } }]`

The input must be given in the following format in order for the program to extract the data properly. The output will be formatted to give a result similar to that shown in the output on top. The program will take the customer order and return the necessary warehouses to complete the shipment. It is assummed that the warehouses are pre-sorted from least cost to greatest cost. The program is capable of returning a string indicating which set of warehouses will result in the least amount of cost. In addition, in some instances, shipments from multiple warehouses are required to complete an order. The program is capable of handling such splits to determining the warehouses needed to complete shipment. 

The Inventory Allocator has been tested for a variety of cases using the unittest library in Python and has proven to output the cheapest shipment necessary and handle splits across warehouses. It is completely possible that I am missing certain cases that I am not aware of. However, out of the 23 tests that I have designed, each test has passed. An example of a test that I have run is the following:

Input: `{ apple: 5, banana: 7, orange: 5, pomegranate: 3, mango: 2}, [{ name: owd, inventory: { apple: 5, banana: 3, orange: 3 } }, { name: dm, inventory: { banana: 4, orange: 2 } }, { name: ic, inventory: { pomegranate: 3, mango: 2 } }]`

Output: `{ owd: { apple: 5, banana: 3, orange: 3 } }, { dm: { banana: 4, orange: 2 } }, { ic: { pomegranate: 3, mango: 2 } }`




This program is a working product but has room for improvement. Although it works properly, it is not the most efficient implementation. Due to time constraints and other tasks on the side, I haven't had the time to make more improvements on the efficiency. The program will run fast but if given a very large order i.e an order of 1,000 different items or given a large warehouse space to search for i.e, a total of 1000 different warehouses, the program could take longer than expected.
