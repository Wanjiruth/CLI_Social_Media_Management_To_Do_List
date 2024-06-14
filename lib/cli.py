# lib/cli.py

import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers import exit_program
from models.task import Task
from models.project import Project


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_project()
        elif choice == "2":
            create_task()
        elif choice == "3":
            view_projects()
        elif choice == "4":
            view_tasks()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new project")
    print("2. Create a new task")
    print("3. View all projects")
    print("4. View all tasks")

def create_project():
    name = input("Enter the project name: ")
    project = Project(name)
    project.save()
    print("Project created.")

def create_task():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    project_id = input("Enter the project ID: ")
    task = Task(title, description, project_id)
    task.save()
    print("Task created.")

def view_projects():
    projects = Project.get_all()
    for project in projects:
        print(f"Project ID: {project.id}, Name: {project.name}")
    print("Returning to menu from view_projects.")
3

def view_tasks():
    tasks = Task.get_all()
    for task in tasks:
        print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}, Project ID: {task.project_id}")
    print("Returning to menu from view_tasks.")


if __name__ == "__main__":
    main()
