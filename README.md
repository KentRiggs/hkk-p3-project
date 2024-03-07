How A Spud Got Away! 

**Overview**

This project is a Python application designed to showcase the skills and topics learned in phase 3 of the Flatiron School. It includes an Object-Relational Mapping (ORM) system for database management and a Command-Line Interface (CLI) for user interaction. 

The application allows users to play a game where they question NPCs via a CLI in the terminal to arrive at an accusation hopefully correctly deducing which of the NPCs is the killer to win the game. Players are only afforded one guess. Choose wisely!

**Deliverables Met:**

ORM Requirements:

 - The application utilizes Python ORM methods for database creation and
   modification. 
   
 - Data model includes at least 2 model classes.

 

 - Datamodel includes at least 1 one-to-many relationship.

   

 - Property methods are defined to add appropriate constraints to each
   model class.

 

 - Each model class includes ORM methods for create, delete, get all,
   and    find by id operations.

CLI Requirements:

 - The CLI displays menus for user interaction.
 - Loops are used to keep the user in the application until they choose
   to exit.
 - For each class in the data model, the CLI includes options to create
   an object, delete an object, display all objects, view related objects, and find an object by attribute.
 - The CLI validates user input and object creations/deletions,
   providing informative errors to the user.

Additional Requirements:

 - Project code follows Object-Oriented Programming (OOP) best
   practices.
 - The Pipfile contains all needed dependencies and no unneeded
   dependencies.
 - Imports are used in files only where necessary.
 - Project folders, files, and modules are organized and follow
   appropriate naming conventions.

**Setup:**   

To play How a Spud Got Away:

 1. Clone this repository to your local environment
 2. cd into the root directory of hkk-p3-project
 3. Install additional dependencies with pipenv install once in the root
    directory
 4. Use pipenv shell to ensure you're in the virtual environment cd into
    the lib folder
 5. use the command python detective-game.py to run the game


**Usage:** 

Once the game is running in your terminal you are able to navigate menus via number choices on screen. 

To begin the game initially enter your name or press 1 to enter the admin menu to adjust the game environment. 

When in menus the "4" option typically will go back and ultimately "5" will exit the game. 

Ask as many questions as you like and remember you only get one guess once you've deduced the killer. Good luck!

Contributors:
Hunter Matyi, Kent Riggs, and Kairi Wright
