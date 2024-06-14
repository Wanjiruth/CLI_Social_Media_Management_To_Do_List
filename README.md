# SOCIAL_MEDIA_MANAGER_TODO_LIST

# 0verview
This project is a CLI (Command Line Interface) application designed to help social media managers organize their tasks and projects efficiently. The application allows users to create, delete, and view tasks and projects, leveraging an ORM to manage the data.

## Features 
- Create, delete, and view tasks
- Create, delete, and view projects
- View tasks related to a specific project
- Use an ORM for database management

## Project Structure
social_media_todo/
├── models/
│   ├── __init__.py       # Initializes the models module
│   ├── task.py           # Defines the Task model
│   └── project.py        # Defines the Project model
├── cli/
│   ├── __init__.py       # Initializes the CLI module
│   └── main.py           # Contains the main CLI application logic
├── db/
│   ├── __init__.py       # Initializes the database module
│   └── base.py           # Sets up the database connection and tables
├── Pipfile               # Pipenv dependencies file
├── Pipfile.lock          # Pipenv locked dependencies file
├── README.md             # This README file
        

## Requirements

-Python 3.9 or higher
-SQLite database (or any other supported database)
-"pipenv" for managing dependencies
-Tkinter (included in the Python standard library)

## Installation

1. Clone the repository: `git clone https://github.com/your-username/Brain_Storm.git`
2. Navigate to the project directory: `cd Social-media-todo`
3. Install the required packages: `pipenv install`


## Usage
## Usage

1. The CLI application will launch, displaying the main menu.
2. From the main menu, you can create a new task, delete a task, display all tasks, view related tasks, or find a task by attribute.
3. To create a new task, select the corresponding option from the menu and follow the prompts to provide task details.
4. To delete a task, select the option to delete a task from the menu and enter the task ID when prompted.
5. To display all tasks, choose the option to display all tasks from the menu.
6. To view related tasks, select the option to view related tasks from the menu and follow the prompts to specify the related attribute.
7. To find a task by attribute, select the option to find a task by attribute from the menu and follow the prompts to specify the attribute and its value.
8. The application will provide informative error messages if invalid input is provided or if an operation fails.


## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
5. Wait for your pull request to be reviewed and merged

Contributions are welcome! If you have any ideas for new features or bug fixes, please submit an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

