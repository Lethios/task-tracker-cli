"""
Task Tracker CLI

A command-line interface (CLI) application for managing tasks.
Users can add, update, delete, list, and modify the status of tasks.
Tasks are stored in a JSON file (data.json) and persist between runs.

Author: Lethios
Date: 27-3-2025
"""

import sys
import os
import json
from datetime import datetime

DATA_FILE = "data.json"

HELP_MESSAGE = f"""
Welcome to Task Tracker CLI!
Usage: python {sys.argv[0]} <command>

Available commands:
  add <task>                  - Add a new task
  update <task_id> <task>     - Update an existing task
  delete <task_id>            - Delete a task
  list [status]               - List all tasks
  mark-in-progress <task_id>  - Mark a task as in progress
  mark-done <task_id>         - Mark a task as done
  help                        - Show this help message
"""

def load_tasks():
    """
    Load tasks from the data file.

    Reads the JSON file containing task data and returns a list of tasks.
    If the file is empty or doesn't exist, it initializes an empty list.

    Returns:
        list: A list of task dictionaries.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = file.read()
        return json.loads(data) if data else []

def save_tasks(tasks):
    """
    Saves the list of tasks to the data file in JSON format.

    Args:
        tasks (list): A list of task dictionaries to be saved.

    This function writes the provided list of tasks to 'data.json', 
    ensuring the data is stored persistently. The file is truncated 
    before writing to prevent any leftover data.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

if len(sys.argv) == 1:
    print(HELP_MESSAGE)
    sys.exit(1)

ACTION = str(sys.argv[1])

task = None
task_id = None

if len(sys.argv) > 2:
    if len(sys.argv) == 3:
        if sys.argv[2].isdigit():            
            task_id = int(sys.argv[2])
        else:
            task = str(sys.argv[2])
    else:
        task = str(sys.argv[3])
        task_id = int(sys.argv[2])
else:
    task = None

if ACTION == "help":
    print(HELP_MESSAGE)
    sys.exit(1)

elif ACTION == "add":
    tasks = load_tasks()
    NEW_ID = tasks[-1]["task_id"] + 1 if tasks else 1
    date_now = datetime.now().strftime("%d-%m-%Y")
    tasks.append({"status": "todo", "task_id": NEW_ID, "task": task, "created_on": date_now})
    save_tasks(tasks)
    print(f"Task added successfully. (Task ID: {NEW_ID})")

elif ACTION == "update":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)

    TASK_FOUND = False
    for task in tasks:
        if task["task_id"] == task_id:
            task["task"] = str(sys.argv[3])
            date_now = datetime.now().strftime("%d-%m-%Y")
            task["updated_on"] = date_now
            TASK_FOUND = True
            break

    if not TASK_FOUND:
        print(f"No tasks found with ID {task_id}.")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

elif ACTION == "delete":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)

    TASK_FOUND = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            tasks.remove(task)
            TASK_FOUND = True
            break

    if not TASK_FOUND:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")

elif ACTION == "mark-in-progress":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)

    TASK_FOUND = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            task["status"] = "in-progress"
            TASK_FOUND = True
            break

    if not TASK_FOUND:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} marked in-progress successfully.")

elif ACTION == "mark-done":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)

    TASK_FOUND = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            task["status"] = "done"
            TASK_FOUND = True
            break

    if not TASK_FOUND:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} marked done successfully.")

elif ACTION == "list":
    if len(sys.argv) == 2:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            sys.exit(1)

        for task in tasks:
            print(f"Task {task["task_id"]}: {task["task"]}  (Status: {task["status"]})")

        save_tasks(tasks)

    elif len(sys.argv) == 3:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            sys.exit(1)

        TASK_FOUND = False

        if sys.argv[2] == "todo":
            for task in tasks:
                if task["status"] == "todo":
                    print(f"Task {task["task_id"]}: {task["task"]}")
                    TASK_FOUND = True

        elif sys.argv[2] == "in-progress":
            for task in tasks:
                if task["status"] == "in-progress":
                    print(f"Task {task["task_id"]}: {task["task"]}")
                    TASK_FOUND = True

        elif sys.argv[2] == "done":
            for task in tasks:
                if task["status"] == "done":
                    print(f"Task {task["task_id"]}: {task["task"]}")
                    TASK_FOUND = True

        else:
            print("Invalid argument.")
            sys.exit(1)

        if not TASK_FOUND:
            print(f"No tasks found with status {sys.argv[2]}.")
            sys.exit(1)

else:
    print("Invalid arguments.")
    sys.exit(1)
