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
    """

    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = file.read()
        return json.loads(data) if data else []

def save_tasks(task_data):
    """
    Saves tasks to the data file in JSON format.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(task_data, file, indent=4)

if len(sys.argv) == 1:
    print(HELP_MESSAGE)
    sys.exit(1)

ACTION = sys.argv[1]
TASK = None
TASK_ID = None

if len(sys.argv) > 2:
    if sys.argv[2].isdigit():
        TASK_ID = int(sys.argv[2])
    else:
        TASK = sys.argv[2]
    if len(sys.argv) > 3:
        TASK = " ".join(sys.argv[3:])

if ACTION == "help":
    print(HELP_MESSAGE)
    sys.exit(0)

task_list = load_tasks()

if ACTION == "add":
    NEW_ID = task_list[-1]["task_id"] + 1 if task_list else 1
    date_now = datetime.now().strftime("%d-%m-%Y")
    task_list.append({"status": "todo", "task_id": NEW_ID, "task": TASK, "created_on": date_now})
    save_tasks(task_list)
    print(f"Task added successfully. (Task ID: {NEW_ID})")
    sys.exit(0)

elif ACTION == "update":
    for task in task_list:
        if task["task_id"] == TASK_ID:
            task["task"] = TASK
            task["updated_on"] = datetime.now().strftime("%d-%m-%Y")
            save_tasks(task_list)
            print(f"Task {TASK_ID} updated successfully.")
            sys.exit(0)
    print(f"No tasks found with ID {TASK_ID}.")
    sys.exit(1)

elif ACTION == "delete":
    task_list = [task for task in task_list if task["task_id"] != TASK_ID]
    save_tasks(task_list)
    print(f"Task {TASK_ID} deleted successfully.")
    sys.exit(0)

elif ACTION == "mark-in-progress":
    for task in task_list:
        if task["task_id"] == TASK_ID:
            task["status"] = "in-progress"
            save_tasks(task_list)
            print(f"Task {TASK_ID} marked in-progress successfully.")
            sys.exit(0)
    print(f"No tasks found with ID {TASK_ID}.")
    sys.exit(1)

elif ACTION == "mark-done":
    for task in task_list:
        if task["task_id"] == TASK_ID:
            task["status"] = "done"
            save_tasks(task_list)
            print(f"Task {TASK_ID} marked done successfully.")
            sys.exit(0)
    print(f"No tasks found with ID {TASK_ID}.")
    sys.exit(1)

elif ACTION == "list":
    if len(task_list) == 0:
        print("No tasks found.")
        sys.exit(1)

    if len(sys.argv) == 3:
        status_filter = sys.argv[2]
        filtered_tasks = []
        for task in task_list:
            if task["status"] == status_filter:
                filtered_tasks.append(task)
        if not filtered_tasks:
            print(f"No tasks found with status {status_filter}")
            sys.exit(1)

        task_list = filtered_tasks

    for task in task_list:
        print(f"Task {task['task_id']}: {task['task']} (Status: {task['status']})")

else:
    print("Invalid command.")
    print(HELP_MESSAGE)
    sys.exit(1)
