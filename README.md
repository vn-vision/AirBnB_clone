# 0x00 AirBnb clone - The console

Welcome to the AirBnB clone project!

First step: Write a command interpreter to manage your AirBnB objects.
    Manage the objects of our project:
        Create a new object (ex: a new User or a new Place)
        Retrieve an object from a file, a database etc…
        Do operations on objects (count, compute stats, etc…)
        Update attributes of an object
        Destroy an object

# GUIDE 
To use the console navigate to the `airbnb_clone` root directory. 
./console

to view the list of commands: help
to get more details about a command: help <name of command> 
    help create

`vn-vision\ALX\AirBnB_clone> ./console.py`
`(hbnb) help`

`Documented commands (type help <topic>):`
`========================================`
`EOF  all  create  destroy  help  quit  show  update`

`(hbnb) help create`
Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
`(hbnb)`


Example on how to:

## create an instance: User
create User :prints id on the screen

## show their details:
show <instance> <id> "id is generated when you create an instance"
show User 12345

## delete their details
destroy User id

## show all instances saved
all - shows all instances
all User - shows all instances of User

## update an existing instance
update User id <key> <value>

update User <id> vn-vision 1234567

## exit the console
quit
Ctrl + D

enjoy the console
vn-vision :) 
