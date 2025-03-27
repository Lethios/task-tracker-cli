import sys
import os
import json
from datetime import datetime

data_file = "data.json"

def load_tasks():
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r") as file:
        data = file.read()
        return json.loads(data) if data else []

def save_tasks(tasks):
    with open(data_file, "w") as file:
        json.dump(tasks, file, indent=4)

if len(sys.argv) == 1:
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [args]")
    print("Commands: add, update.")
    sys.exit(1)

action = str(sys.argv[1])

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

if action == "help":
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [args]")
    print("Commands: add, update.")

elif action == "add":
    tasks = load_tasks()
    new_id = tasks[-1]["task_id"] + 1 if tasks else 1
    tasks.append({"status": "todo", "task_id": new_id, "task": task, "created_on": datetime.now().strftime("%d-%m-%Y")})
    save_tasks(tasks)
    print(f"Task added successfully. (Task ID: {new_id})")

elif action == "update":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)
    
    task_found = False
    for task in tasks:
        if task["task_id"] == task_id:
            task["task"] = str(sys.argv[3])
            task["updated_on"] = datetime.now().strftime("%d-%m-%Y")
            task_found = True
            break

    if not task_found:
        print(f"No tasks found with ID {task_id}.")
        sys.exit(1)
    
    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

elif action == "delete":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)
    
    task_found = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            tasks.remove(task)
            task_found = True
            break

    if not task_found:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)
    
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")

elif action == "mark-in-progress":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        sys.exit(1)

    task_found = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            task["status"] = "in-progress"
            task_found = True
            break

    if not task_found:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} marked in-progress successfully.")

elif action == "mark-done":
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")

    task_found = False
    for task in tasks:
        if task["task_id"] == int(task_id):
            task["status"] = "done"
            task_found = True
            break

    if not task_found:
        print(f"No tasks found with ID {task_id}")
        sys.exit(1)

    save_tasks(tasks)
    print(f"Task {task_id} marked done successfully.")
