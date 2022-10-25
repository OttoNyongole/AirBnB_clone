# 0x00. AirBnB clone - The console
The console is the is the command line interpreter, in our project the AirBnB Clone its is limited to a specifict cases. through this console we want to be eble to manage the objects of our projectslike 
- Create a new object(i.e a new user or a New place)
- Retrieve an object from a file, database etc.
- Do operations on objects (count, compute stats, etc)
- Update attributes of an objects
- Destroy an object

# Console usage
- Clone this repository: git clone <this repository>
- Locate the file console.py
- In interactive mode type: ./console.py hit enter
- In non interactive mode: echo "<command>" | ./console.py

# File discriptios
for the now the console contains the following commands
- quit - exit the console
- create - create a new istance of Basemode class and save it to JSON file and print the id
- destroy - Delete an instance based on the class name and id and save the changes into JSON file.
- shaw - Prints the string representation of an instance based on the class name and id
- update - update an instance based on the class name and idby adding or updating attributes(save the changes to JSON file)
- all - Print all string representation of instances based or not on the class name
